# -*- coding: utf-8 -*-

description = 'TOFTOF radial collimator'

group = 'optional'

tango_base = 'tango://tofhw.toftof.frm2:10000/toftof/'

devices = dict(
    rc_onoff = device('nicos.devices.tango.NamedDigitalOutput',
        description = 'Activates radial collimator',
        tangodevice = tango_base + 'rc/_rc_onoff',
        mapping = {
            'on': 1,
            'off': 0,
        },
    ),
    rc_motor = device('nicos.devices.tango.AnalogOutput',
        description = 'Radial collimator motor',
        tangodevice = tango_base + 'rc/_rc_motor',
        lowlevel = True,
    ),
)
