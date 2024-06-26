description = 'REFSANS setup for julabo01 Presto A40'

group = 'optional'

instrument_values = configdata('instrument.values')

tango_base = instrument_values['tango_base'] + 'refsans/julabo01/'
code_base = instrument_values['code_base']

devices = dict(
    julabo_temp = device('nicos.devices.entangle.TemperatureController',
        description = 'Julabo01 temperature control',
        tangodevice = tango_base + 'control',
        fmtstr = '%.2f',
    ),
    julabo_int = device('nicos.devices.entangle.Sensor',
        description = 'Julabo01 temperature bath',
        tangodevice = tango_base + 'intsensor',
        fmtstr = '%.2f',
    ),
    julabo_ext = device('nicos.devices.entangle.Sensor',
        description = 'Julabo01 external sensor',
        tangodevice = tango_base + 'extsensor',
        fmtstr = '%.2f',
    ),
    julabo_flow = device('nicos.devices.entangle.Sensor',
        description = 'flow of julabo at PO by Sensor',
        tangodevice = 'tango://ana4gpio01:10000/test/ads/ch2',
        unit = 'l/min',
    ),
    julabo_flow_avg = device(code_base + 'avg.BaseAvg',
        description = 'avg for flow',
        dev = 'julabo_flow',
        unit = 'l/min',
    ),
)
