description = 'Refsans_flipper special HW; but NOT yet!'

group = 'lowlevel'

uribase = 'tango://refsanshw.refsans.frm2:10000/test/flipper/'

devices = dict(
    guide = device('nicos.devices.tango.AnalogInput',
        description = 'Temperature of Flipping Guide',
        tangodevice = uribase + 'guide_temp',
    ),
    coil = device('nicos.devices.tango.AnalogInput',
        description = 'Temperature of Flipping Coil',
        tangodevice = uribase + 'coil_temp',
    ),
    current = device('nicos.devices.tango.WindowTimeoutAO',
        description = 'Current of Flipping Coil',
        tangodevice = uribase + 'current',
        precision = 0.1,
    ),
    frequency = device('nicos.devices.tango.AnalogInput',
        description = 'Frequency of Flipping Field',
        tangodevice = uribase + 'frequency',
    ),
    flipper = device('nicos.devices.tango.NamedDigitalOutput',
        description = 'Flipper',
        tangodevice = uribase + 'flipper',
        mapping = dict(ON = 1, OFF = 0),
    ),
)
