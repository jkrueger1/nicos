# -*- coding: utf-8 -*-
# *****************************************************************************
# NICOS, the Networked Instrument Control System of the MLZ
# Copyright (c) 2018-2019 by the NICOS contributors (see AUTHORS)
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
#   Christian Felder <c.felder@fz-juelich.de>
#
# *****************************************************************************

from __future__ import absolute_import, division, print_function

from nicos.core.constants import FINAL, SLAVE
from nicos.core.params import Value
from nicos.devices.vendor.lima.andor2 import Andor2LimaCCD as BaseAndor2LimaCCD


# TODO: Remove code duplication and fix MRO issues when inheriting
#       from `nicos_mlz.jcns.devices.detector.ImageChannel` and
#       `BaseAndor2LimaCCD` which both inherit from `ImageChannelMixin`
class Andor2LimaCCD(BaseAndor2LimaCCD):
    """Andor SDK2 based camera which returns sum of all counts."""

    def doInit(self, mode):
        BaseAndor2LimaCCD.doInit(self, mode)
        if mode != SLAVE:
            self.readArray(FINAL)  # update readresult at startup

    def doReadArray(self, quality):
        narray = BaseAndor2LimaCCD.doReadArray(self, quality)
        self.readresult = [narray.sum()]
        return narray

    def valueInfo(self):
        return Value(name=self.name, type='counter', fmtstr='%d',
                     errors='sqrt', unit='cts'),
