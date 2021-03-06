description = 'Slit H2 using Beckhoff controllers'

group = 'lowlevel'

tango_base = 'tango://refsanshw.refsans.frm2.tum.de:10000/'

devices = dict(
    h2_center = device('nicos_mlz.refsans.devices.beckhoff.nok.BeckhoffMotorHSlit',
        description = 'Horizontal slit system: offset of the slit-center to the beam. towards TOFTOF is plus',
        tangodevice = tango_base + 'h2/io/modbus',
        address = 0x3020+0*10, # word address
        slope = -1000,
        unit = 'mm',
        abslimits = (-69.5, 69.5),
    ),
    h2_width = device('nicos_mlz.refsans.devices.beckhoff.nok.BeckhoffMotorHSlit',
        description = 'Horizontal slit system: opening of the slit',
        tangodevice = tango_base + 'h2/io/modbus',
        address = 0x3020+1*10, # word address
        slope = 1000,
        unit = 'mm',
        abslimits = (0.05, 69.5),
    ),
)
