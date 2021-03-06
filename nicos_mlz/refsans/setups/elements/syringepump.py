description = 'Setup for New Era Syringe pumps'

group = 'optional'

tango_base = 'tango://refsanshw.refsans.frm2:10000/refsans/'

devices = dict(
    pump0_diameter = device('nicos.devices.tango.AnalogOutput',
        description = 'Syringe diameter for first pump',
        tangodevice = tango_base + 'syringe/pump0diameter',
    ),
    pump0_rate = device('nicos.devices.tango.AnalogOutput',
        description = 'Infusion rate for first pump',
        tangodevice = tango_base + 'syringe/pump0rate',
    ),
    pump0_run = device('nicos_mlz.refsans.devices.syringepump.PumpAnalogOutput',
        description = 'Move to volume to infuse (positive) or withdraw (negative)',
        tangodevice = tango_base + 'syringe/pump0infuse',
        precision = 0.0001,
    ),

    pump1_diameter = device('nicos.devices.tango.AnalogOutput',
        description = 'Syringe diameter for second pump',
        tangodevice = tango_base + 'syringe/pump1diameter',
    ),
    pump1_rate = device('nicos.devices.tango.AnalogOutput',
        description = 'Infusion rate for second pump',
        tangodevice = tango_base + 'syringe/pump1rate',
    ),
    pump1_run = device('nicos_mlz.refsans.devices.syringepump.PumpAnalogOutput',
        description = 'Move to volume to infuse (positive) or withdraw (negative)',
        tangodevice = tango_base + 'syringe/pump1infuse',
        precision = 0.0001,
    ),
)
