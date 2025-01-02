# *****************************************************************************
# NICOS, the Networked Instrument Control System of the MLZ
# Copyright (c) 2009-2024 by the NICOS contributors (see AUTHORS)
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
# Module authors:
#   Moritz Hannemann <m.hannemann@fz-juelich.de>
#
# *****************************************************************************

import json
import uuid
from datetime import datetime, timezone

import pika

from nicos import session
from nicos.core import Override, Param
from nicos.core.constants import BLOCK, MASTER, POINT, SCAN, SUBSCAN
from nicos.core.data import BaseDataset, BlockDataset, DataSink, \
    DataSinkHandler, ScanDataset


def metainfo_to_json(metainfo):
    metadata = {}
    for (dev, parm), (value, _str_value, unit, _) in metainfo.items():
        metadata.setdefault(dev, {})
        metadata[dev][parm] = value if not unit else (value, unit)
    return metadata


class Message:
    id: str  # pylint: disable=redefined-builtin
    type: str  # pylint: disable=redefined-builtin
    metadata: dict

    def __init__(
            self,
            id: uuid.UUID,  # pylint: disable=redefined-builtin
            scanid: uuid.UUID,
            blockid: uuid.UUID,
            type: str,  # pylint: disable=redefined-builtin
            started: str,
            filepaths: list,
            mapping: dict,
            metainfo: dict,
            statistics: dict,
    ):
        self.id = str(id)
        self.blockid = str(blockid) or None
        self.scanid = str(scanid) or None
        self.type = type
        self.creation_timestamp = started
        self.filepaths = filepaths
        self.mapping = mapping
        self.metadata = metainfo
        self.statistics = statistics

    def __str__(self):
        return json.dumps({**self.__dict__})


class RabbitSinkHandler(DataSinkHandler):

    ordering = 80

    def _sendMessage(self, type: str, dataset: BaseDataset,  # pylint: disable=redefined-builtin
                     scands: ScanDataset = None, blockds: BlockDataset = None):
        """Sends the metainfo, if available, and other information to the
        Queue"""
        started = (datetime.fromtimestamp(dataset.started, tz=timezone.utc)
                   .isoformat())

        def publish(message: Message):
            self.sink._channel.basic_publish(
                exchange=self.sink._exchange,
                routing_key=session.instrument.instrument,
                body=str(message),
                properties=pika.BasicProperties(
                    content_type='application/json'))

        metadata = {}
        if dataset.settype != BLOCK:
            metadata = metainfo_to_json(dataset.metainfo)
        msg = Message(
            dataset.uid,
            scands.uid if scands else None,
            blockds.uid if blockds else None,
            type,
            started,
            dataset.filepaths,
            # DEVICE_INFO_MAPPING,
            {
                'experiment': session.experiment.name,
                'sample': session.experiment.sample.name,
                'instrument': session.instrument.name,
            },
            metainfo=metadata,
            statistics=dataset.valuestats,
        )
        for retry in range(3):
            try:
                if retry > 0:  # reconnect
                    self.sink._connect()
                publish(msg)
                break
            except (pika.exceptions.AMQPChannelError,
                    pika.exceptions.AMQPConnectionError) as e:
                self.log.debug('reconnect #%d due to %r', retry + 1, e)
                exc = e
        else:
            raise exc

    def _getScanDatasetParents(self, dataset):
        """Returns a tuple of `BlockDataset`, `ScanDataset` if available.

        get parent `ScanDataset` (subscan) and `BlockDataset` for this
        `ScanDataset` if available
        """
        scands, blockds = None, None
        for ds in self.manager.iterParents(dataset, settypes=(BLOCK, SCAN)):
            if ds.settype == BLOCK:
                blockds = ds
            elif ds.settype == SCAN:
                scands = ds
        return blockds, scands

    def addSubset(self, subset):
        # do not take into account addSubset of scans to blocks
        # this is handled in `end()`.
        if subset.settype != POINT:
            return
        blockds, scands = self._getScanDatasetParents(self.dataset)
        if subset.number == 1:  # begin of ScanDataset including metainfo
            self._sendMessage(self.dataset.settype, self.dataset, scands,
                              blockds)
        self._sendMessage(subset.settype, subset, self.dataset, blockds)

    def begin(self):
        self.log.debug("begin: dataset.settype = %s", self.dataset.settype)
        # need to skip begin of ScanDataset as metainfo is not available
        # before the first point. This is handled on the first point in
        # `addSubset`.
        if self.dataset.settype not in (SCAN, SUBSCAN):
            self._sendMessage(self.dataset.settype, self.dataset)

    def end(self):
        self.log.debug("end: dataset.settype = %s", self.dataset.settype)
        blockds, scands = None, None
        if self.dataset.settype in (SCAN, SUBSCAN):
            # the `ScanDataset` has been popped from DataManager's stack before
            # dispatching `finish`. Parents are left on the stack, using
            # `iter(self.manager._stack)` though.
            blockds, scands = self._getScanDatasetParents(None)
        self._sendMessage(f'{self.dataset.settype}.end', self.dataset,
                          scands, blockds)


class RabbitSink(DataSink):
    """Creates a RabbitMQ exchange and queue on the parameterized instance
    and writes all metainfo synchronously into it for further processing.
    """
    parameters = {
        'rabbit_url': Param('RabbitMQ server url', type=str, mandatory=True)
    }

    parameter_overrides = {
        'settypes': Override(default=[SCAN, SUBSCAN, BLOCK])
    }

    handlerclass = RabbitSinkHandler
    _connection = None
    _channel = None

    def doInit(self, mode):
        if mode == MASTER:
            self._connect()
            self._prepareExchange()
            self._prepareQueue()

    def doShutdown(self):
        if self._connection is not None:
            self._connection.close()

    def _connect(self):
        """Connects to the RabbitMQ instance"""
        parameters = pika.URLParameters(self.rabbit_url)
        self._connection = pika.BlockingConnection(parameters=parameters)
        self._channel = self._connection.channel()

    def _prepareExchange(self):
        """Declares the Exchange on the RabbitMQ instance"""
        self._exchange = f'{session.instrument.instrument}'
        self._channel.exchange_declare(
            self._exchange,
            # exchange_type=ExchangeType.direct,
            durable=True,
            auto_delete=False)

    def _prepareQueue(self):
        """Declares the Queue and its bindings on the RabbitMQ instance"""
        self._queue = self._channel.queue_declare(
            f'{session.instrument.instrument}',
            exclusive=False,
            durable=True,
            auto_delete=False).method.queue

        self._channel.queue_bind(
            exchange=self._exchange,
            queue=self._queue,
            routing_key=session.instrument.instrument)
