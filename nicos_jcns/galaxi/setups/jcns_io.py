# -*- coding: utf-8 -*-

description = 'GALAXI in- and outputs'

group = 'optional'

tango_base = 'tango://phys.galaxi.kfa-juelich.de:10000/galaxi/'
tango_digital = tango_base + 'fzjdp_digital/'
tango_analog = tango_base + 'plc_io/'

devices = dict(
    vacuumtube1 = device('nicos.devices.tango.AnalogInput',
        description = 'Vacuum tube 1',
        tangodevice = tango_analog + 'vacuum_tube1',
    ),
    vacuumtube2 = device('nicos.devices.tango.AnalogInput',
        description = 'Vacuum tube 2',
        tangodevice = tango_analog + 'vacuum_tube2',
    ),
    vacuumtube3 = device('nicos.devices.tango.AnalogInput',
        description = 'Vacuum tube 3',
        tangodevice = tango_analog + 'vacuum_tube3',
    ),
    pump02 = device('nicos.devices.tango.NamedDigitalInput',
        description = 'Pump 2',
        tangodevice = tango_digital + 'Pumpe2',
        mapping = dict(on = 0, off = 1, error_on = 2, error_off = 3),
        fmtstr = '%s',
    ),
    pump03 = device('nicos.devices.tango.NamedDigitalInput',
        description = 'Pump 3',
        tangodevice = tango_digital + 'Pumpe3',
        mapping = dict(on = 0, off = 1, error_on = 2, error_off = 3),
        fmtstr = '%s',
    ),
    detectorpos = device('nicos.devices.tango.NamedDigitalInput',
        description = 'Detectorposition',
        tangodevice = tango_digital + 'DetectorPos',
        mapping = dict(pos1 = 1, pos2 = 2, pos3 = 4, pos4 = 8, pos5 = 16),
        fmtstr = '%s',
        lowlevel = True,
    ),
    detectube01 = device('nicos.devices.tango.NamedDigitalInput',
        description = 'Detectortube 1',
        tangodevice = tango_digital + 'DetectorTube1',
        mapping = dict(up = 1, down = 2),
        fmtstr = '%s',
    ),
    detectube02 = device('nicos.devices.tango.NamedDigitalInput',
        description = 'Detectortube 2',
        tangodevice = tango_digital + 'DetectorTube2',
        mapping = dict(up = 1, down = 2),
        fmtstr = '%d',
    ),
    detectube03 = device('nicos.devices.tango.NamedDigitalInput',
        description = 'Detectortube 3',
        tangodevice = tango_digital + 'DetectorTube3',
        mapping = dict(up = 1, down = 2),
        fmtstr = '%d',
    ),
    detectube04 = device('nicos.devices.tango.NamedDigitalInput',
        description = 'Detectortube 4',
        tangodevice = tango_digital + 'DetectorTube4',
        mapping = dict(up = 1, down = 2),
        fmtstr = '%d',
    ),
    detdistance = device('nicos_jcns.galaxi.devices.automation.DetectorDistance',
        description = 'Pilatus detector distance',
        detectubes = [
            'detectube01', 'detectube02', 'detectube03', 'detectube04'
        ],
        offset = 831,
        unit = 'mm',
        fmtstr = '%d',
    ),
    vavalve02 = device('nicos.devices.tango.NamedDigitalInput',
        description = 'Vacuumvalve 2',
        tangodevice = tango_digital + 'VacuumValve2',
        mapping = dict(open = 0, close = 1),
        fmtstr = '%s',
    ),
    vavalve03 = device('nicos.devices.tango.NamedDigitalInput',
        description = 'Vacuumvalve 2',
        tangodevice = tango_digital + 'VacuumValve2',
        mapping = dict(open = 0, close = 1),
        fmtstr = '%s',
    ),
    vavalve04 = device('nicos.devices.tango.NamedDigitalInput',
        description = 'Vacuumvalve 4',
        tangodevice = tango_digital + 'VacuumValve4',
        mapping = dict(open = 0, close = 1),
        fmtstr = '%s',
    ),
    vavalve05 = device('nicos.devices.tango.NamedDigitalInput',
        description = 'Vacuumvalve 5',
        tangodevice = tango_digital + 'VacuumValve5',
        mapping = dict(open = 0, close = 1),
        fmtstr = '%s',
    ),
    vavalve06 = device('nicos.devices.tango.NamedDigitalInput',
        description = 'Vacuumvalve 6',
        tangodevice = tango_digital + 'VacuumValve6',
        mapping = dict(open = 0, close = 1),
        fmtstr = '%s',
    ),
    vbvalve01 = device('nicos.devices.tango.NamedDigitalInput',
        description = 'Ventilationvalve 1',
        tangodevice = tango_digital + 'VentilationValve1',
        mapping = dict(open = 0, close = 1),
        fmtstr = '%s',
    ),
    vbvalve02 = device('nicos.devices.tango.NamedDigitalInput',
        description = 'Ventilationvalve 2',
        tangodevice = tango_digital + 'VentilationValve2',
        mapping = dict(open = 0, close = 1),
        fmtstr = '%s',
    ),
    vbvalve03 = device('nicos.devices.tango.NamedDigitalInput',
        description = 'Ventilationvalve 3',
        tangodevice = tango_digital + 'VentilationValve3',
        mapping = dict(open = 0, close = 1),
        fmtstr = '%s',
    ),
    coolerxraysource = device('nicos_jcns.galaxi.devices.bruker_axs.WaterCooler',
        description = 'Water cooler info',
        tangodevice = tango_digital + 'Waterworks',
        mapping = dict(ok = 1, error = 0),
        startbit = 3,
        bitwidth = 1,
        warnlimits = ('ok', 'ok'),
        fmtstr = '%s',
    ),
    statussps = device('nicos.devices.tango.NamedDigitalInput',
        description = 'Status SPS Info',
        tangodevice = tango_digital + 'statusSPS',
        mapping = {'ok': 0, 'emergency stop': 1},
        warnlimits = ('ok', 'ok'),
        fmtstr = '%s',
    ),
    voice_output = device('nicos.devices.tango.DigitalOutput',
        description = 'Voice output device that welcomes new users to GALAXI',
        tangodevice = tango_digital + 'voice_output',
        lowlevel = True,
        fmtstr = '%d',
        unit = '',
    ),
    vacuumoperation = device('nicos_jcns.galaxi.devices.automation.VacuumOperation',
        description = 'Different Vacuum operations',
        tangodevice = tango_digital + 'VacuumMode',
        mapping = {
            'idle': 0,
            'chamber1 vent': 1,
            'chamber1 evacuate': 2,
            'samplechamber vent': 3,
            'samplechamber evacuate': 4,
            'detector open': 5,
            'detector 0': 6,
            'detector 1': 7,
            'detector 2': 8,
            'detector 3': 9,
            'detector 4': 10,
        },
        fmtstr = '%s',
    ),
)
