description = 'LakeShore 372 cryo controller'
group = 'optional'

includes = ['alias_T']

tango_base = 'tango://localhost:10000/cart/'

devices = dict(
    T_sample = device('nicos.devices.entangle.Sensor',
        description = 'sensor A: sample',
        tangodevice = tango_base + 'ls372/temp-sample',
        pollinterval = 0.7,
        maxage = 2,
    ),
    ohm_sample = device('nicos.devices.entangle.Sensor',
        description = 'raw sensor A: sample',
        tangodevice = tango_base + 'ls372/raw-sample',
        pollinterval = 2,
        maxage = 5,
    ),
    T_ch9 = device('nicos.devices.entangle.Sensor',
        description = 'sensor on channel 9',
        tangodevice = tango_base + 'ls372/temp-ch9',
        pollinterval = 0.7,
        maxage = 2,
    ),
    ohm_ch9 = device('nicos.devices.entangle.Sensor',
        description = 'raw sensor channel 9',
        tangodevice = tango_base + 'ls372/raw-ch9',
        pollinterval = 2,
        maxage = 5,
    ),
    # ohm_1k = device('nicos.devices.entangle.Sensor',
    #     description = 'raw sensor 1: 1K pot',
    #     tangodevice = tango_base + 'ls372/raw-1k',
    #     pollinterval = 2,
    #     maxage = 5,
    # ),
    # ohm_still = device('nicos.devices.entangle.Sensor',
    #     description = 'raw sensor 2: still',
    #     tangodevice = tango_base + 'ls372/raw-still',
    #     pollinterval = 2,
    #     maxage = 5,
    # ),
    # ohm_mc = device('nicos.devices.entangle.Sensor',
    #     description = 'raw sensor 3: mixing chamber',
    #     tangodevice = tango_base + 'ls372/raw-mc',
    #     pollinterval = 2,
    #     maxage = 5,
    # ),
    # ohm_chip = device('nicos.devices.entangle.Sensor',
    #     description = 'raw sensor 5: chip',
    #     tangodevice = tango_base + 'ls372/raw-chip',
    #     pollinterval = 2,
    #     maxage = 5,
    # ),
    # ohm_finger = device('nicos.devices.entangle.Sensor',
    #     description = 'raw sensor 6: finger',
    #     tangodevice = tango_base + 'ls372/raw-finger',
    #     pollinterval = 2,
    #     maxage = 5,
    # ),
    # T_1K = device('nicos.devices.entangle.Sensor',
    #     description = 'channel 1: 1K pot',
    #     tangodevice = tango_base + 'ls372/temp-1k',
    #     pollinterval = 0.7,
    #     maxage = 2,
    # ),
    # T_chip = device('nicos.devices.entangle.Sensor',
    #     description = 'channel 5: chip',
    #     tangodevice = tango_base + 'ls372/temp-chip',
    #     pollinterval = 0.7,
    #     maxage = 2,
    # ),
    # T_finger = device('nicos.devices.entangle.Sensor',
    #     description = 'channel 6: cold finger',
    #     tangodevice = tango_base + 'ls372/temp-finger',
    #     pollinterval = 0.7,
    #     maxage = 2,
    # ),
    # T_mc = device('nicos.devices.entangle.Sensor',
    #     description = 'channel 3: mixing chamber',
    #     tangodevice = tango_base + 'ls372/temp-mc',
    #     pollinterval = 0.7,
    #     maxage = 2,
    # ),
    # T_still = device('nicos.devices.entangle.Sensor',
    #     description = 'channel 2: still',
    #     tangodevice = tango_base + 'ls372/temp-still',
    #     pollinterval = 0.7,
    #     maxage = 2,
    # ),

    # T_control = device('nicos.devices.entangle.TemperatureController',
    #     description = 'channel A control',
    #     tangodevice = tango_base + 'ls372/control',
    #     pollinterval = 0.7,
    #     maxage = 2,
    # ),

    # dr_still = device('nicos.devices.entangle.AnalogOutput',
    #     description = 'heating of the Still in percent',
    #     tangodevice = tango_base + 'ls372/still',
    #     pollinterval = 2,
    #     maxage = 5,
    # ),
    # dr_heaterrange = device('nicos.devices.entangle.NamedDigitalOutput',
    #     description = 'heater range of the main control loop',
    #     tangodevice = tango_base + 'ls372/heaterrange',
    #     pollinterval = 2,
    #     maxage = 5,
    #     mapping = {
    #         'off': 0,
    #         '31.6 uA': 1,
    #         '100 uA': 2,
    #         '316 uA': 3,
    #         '1.00 mA': 4,
    #         '3.16 mA': 5,
    #         '10.0 mA': 6,
    #         '31.6 mA': 7,
    #         '100 mA': 8,
    #     },
    # ),
)

