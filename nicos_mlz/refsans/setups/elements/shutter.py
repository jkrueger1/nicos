description = 'Instrument shutter device'

group = 'lowlevel'

tango_base = 'tango://refsanshw.refsans.frm2.tum.de:10000/shutter/shutter/'

devices = dict(
    shutter_m = device('nicos.devices.tango.Motor',
        description = 'Instrument shutter linear motor',
        tangodevice = tango_base + 'motor',
        abslimits = (0, 55),
        precision = 0.5,
        lowlevel = True,
    ),
    shutter = device('nicos_mlz.refsans.devices.shutter.Shutter',
        description = 'Instrument shutter',
        moveable = 'shutter_m',
        precision = 0.5,
        mapping = {'closed': 7,
                   'open': 65,
                   'safe':0.275,
                   },
        fallback = 'offline',
    ),
)
