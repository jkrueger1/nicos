description = 'QMesyDAQ detector devices'

group = 'lowlevel'

tango_base = 'tango://spodictrl.spodi.frm2.tum.de:10000/spodi/'
detector_base = 'tango://mesydaq.spodi.frm2.tum.de:10000/qm/qmesydaq/'

devices = dict(
    mon = device('nicos.devices.vendor.qmesydaq.tango.CounterChannel',
        description = 'Monitor',
        tangodevice = detector_base + 'counter0',
        fmtstr = '%d',
        type = 'monitor',
        visibility = (),
    ),
    tim1 = device('nicos.devices.vendor.qmesydaq.tango.TimerChannel',
        description = 'Timer',
        tangodevice = detector_base + 'timer',
        fmtstr = '%.2f',
        unit = 's',
        visibility = (),
    ),
    image = device('nicos.devices.vendor.qmesydaq.tango.ImageChannel',
        description = 'Image data device',
        tangodevice = detector_base + 'image',
        fmtstr = '%d',
        pollinterval = None,
        visibility = (),
        transpose = True,
    ),
    basedet = device('nicos.devices.generic.Detector',
        description = 'Classical detector with single channels',
        timers = ['tim1'],
        monitors = ['mon'],
        images = ['image'],
        pollinterval = None,
        visibility = (),
    ),
    adet = device('nicos_mlz.spodi.devices.Detector',
        description = 'Scanning (resolution steps) detector',
        motor = 'tths',
        detector = 'basedet',
        pollinterval = None,
        maxage = 86400,
        liveinterval = 5,
    ),
    hv_det = device('nicos.devices.entangle.PowerSupply',
        description = 'Detector high voltage',
        tangodevice = tango_base + 'hv/detector',
        requires = {'level': 'admin'},
    ),
    hv_det_current = device('nicos.devices.generic.ReadonlyParamDevice',
        description = 'Detector high voltage current',
        device = 'hv_det',
        parameter = 'current',
    ),
    hv_mon = device('nicos.devices.entangle.PowerSupply',
        description = 'Monitor high voltage',
        tangodevice = tango_base + 'hv/monitor',
        requires = {'level': 'admin'},
    ),
    hv_mon_current = device('nicos.devices.generic.ReadonlyParamDevice',
        description = 'Monitor high voltage current',
        device = 'hv_mon',
        parameter = 'current',
    ),
    histogram = device('nicos_mlz.devices.datasinks.qmesydaq.HistogramSink',
        description = 'Histogram data written via QMesyDAQ',
        image = 'image',
    ),
    listmode = device('nicos_mlz.devices.datasinks.qmesydaq.ListmodeSink',
        description = 'Listmode data written via QMesyDAQ',
        image = 'image',
    ),
    detsampledist = device('nicos.devices.generic.ManualMove',
        description = 'Distance between sample and detector',
        default = 1.117,
        abslimits = (1.117, 1.117),
        unit = 'm',
    ),
)
