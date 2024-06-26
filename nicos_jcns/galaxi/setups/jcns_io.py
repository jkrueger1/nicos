description = 'GALAXI in- and outputs setup'
group = 'optional'

tango_base = 'tango://phys.galaxi.jcns.fz-juelich.de:10000/galaxi/'
s7_digital = tango_base + 'fzjdp_digital/'
s7_analog = tango_base + 'plc_io/'

devices = dict(
    vacuumtube1 = device('nicos.devices.entangle.AnalogInput',
        description = 'Vacuum tube 1 pressure.',
        tangodevice = s7_analog + 'vacuum_tube1',
    ),
    vacuumtube2 = device('nicos.devices.entangle.AnalogInput',
        description = 'Vacuum tube 2 pressure.',
        tangodevice = s7_analog + 'vacuum_tube2',
    ),
    vacuumtube3 = device('nicos.devices.entangle.AnalogInput',
        description = 'Vacuum tube 3 pressure.',
        tangodevice = s7_analog + 'vacuum_tube3',
    ),
    pump02 = device('nicos.devices.entangle.NamedDigitalInput',
        description = 'Pump 2 status.',
        tangodevice = s7_digital + 'Pumpe2',
        mapping = dict(on = 0, off = 1, error_on = 2, error_off = 3),
        fmtstr = '%s',
    ),
    pump03 = device('nicos.devices.entangle.NamedDigitalInput',
        description = 'Pump 3 status.',
        tangodevice = s7_digital + 'Pumpe3',
        mapping = dict(on = 0, off = 1, error_on = 2, error_off = 3),
        fmtstr = '%s',
    ),
    detectorpos = device('nicos.devices.entangle.NamedDigitalInput',
        description = 'PILATUS detector position.',
        tangodevice = s7_digital + 'DetectorPos',
        mapping = dict(pos1 = 1, pos2 = 2, pos3 = 4, pos4 = 8, pos5 = 16),
        fmtstr = '%s',
        visibility = (),
    ),
    detectube01 = device('nicos.devices.entangle.NamedDigitalInput',
        description = 'Detector tube 1 position.',
        tangodevice = s7_digital + 'DetectorTube1',
        mapping = dict(up = 1, down = 2),
        fmtstr = '%s',
    ),
    detectube02 = device('nicos.devices.entangle.NamedDigitalInput',
        description = 'Detector tube 2 position.',
        tangodevice = s7_digital + 'DetectorTube2',
        mapping = dict(up = 1, down = 2),
        fmtstr = '%d',
    ),
    detectube03 = device('nicos.devices.entangle.NamedDigitalInput',
        description = 'Detector tube 3 position.',
        tangodevice = s7_digital + 'DetectorTube3',
        mapping = dict(up = 1, down = 2),
        fmtstr = '%d',
    ),
    detectube04 = device('nicos.devices.entangle.NamedDigitalInput',
        description = 'Detector tube 4 position.',
        tangodevice = s7_digital + 'DetectorTube4',
        mapping = dict(up = 1, down = 2),
        fmtstr = '%d',
    ),
    detdistance = device('nicos_jcns.galaxi.devices.automation.DetectorDistance',
        description = 'PILATUS detector to sample distance.',
        detectubes = ['detectube01', 'detectube02',
                      'detectube03', 'detectube04'],
        offset = 831,
        unit = 'mm',
        fmtstr = '%d',
    ),
    vavalve02 = device('nicos.devices.entangle.NamedDigitalInput',
        description = 'Vacuum valve 2 status.',
        tangodevice = s7_digital + 'VacuumValve2',
        mapping = dict(open = 0, close = 1),
        fmtstr = '%s',
    ),
    vavalve03 = device('nicos.devices.entangle.NamedDigitalInput',
        description = 'Vacuum valve 3 status.',
        tangodevice = s7_digital + 'VacuumValve2',
        mapping = dict(open = 0, close = 1),
        fmtstr = '%s',
    ),
    vavalve04 = device('nicos.devices.entangle.NamedDigitalInput',
        description = 'Vacuum valve 4 status.',
        tangodevice = s7_digital + 'VacuumValve4',
        mapping = dict(open = 0, close = 1),
        fmtstr = '%s',
    ),
    vavalve05 = device('nicos.devices.entangle.NamedDigitalInput',
        description = 'Vacuum valve 5 status.',
        tangodevice = s7_digital + 'VacuumValve5',
        mapping = dict(open = 0, close = 1),
        fmtstr = '%s',
    ),
    vavalve06 = device('nicos.devices.entangle.NamedDigitalInput',
        description = 'Vacuum valve 6 status.',
        tangodevice = s7_digital + 'VacuumValve6',
        mapping = dict(open = 0, close = 1),
        fmtstr = '%s',
    ),
    vbvalve01 = device('nicos.devices.entangle.NamedDigitalInput',
        description = 'Ventilation valve 1 status.',
        tangodevice = s7_digital + 'VentilationValve1',
        mapping = dict(open = 0, close = 1),
        fmtstr = '%s',
    ),
    vbvalve02 = device('nicos.devices.entangle.NamedDigitalInput',
        description = 'Ventilation valve 2 status.',
        tangodevice = s7_digital + 'VentilationValve2',
        mapping = dict(open = 0, close = 1),
        fmtstr = '%s',
    ),
    vbvalve03 = device('nicos.devices.entangle.NamedDigitalInput',
        description = 'Ventilation valve 3 status.',
        tangodevice = s7_digital + 'VentilationValve3',
        mapping = dict(open = 0, close = 1),
        fmtstr = '%s',
    ),
    coolerxraysource = device('nicos_jcns.galaxi.devices.bruker_axs.WaterCooler',
        description = 'X-ray source water cooler status.',
        tangodevice = s7_digital + 'Waterworks',
        mapping = dict(ok = 1, error = 0),
        startbit = 3,
        bitwidth = 1,
        warnlimits = ('ok', 'ok'),
        fmtstr = '%s',
    ),
    statussps = device('nicos.devices.entangle.NamedDigitalInput',
        description = 'PLC status.',
        tangodevice = s7_digital + 'statusSPS',
        mapping = dict(ok = 0, emergency_stop = 1),
        warnlimits = ('ok', 'ok'),
        fmtstr = '%s',
    ),
    voice_output = device('nicos.devices.entangle.DigitalOutput',
        description = 'Voice output device to welcome new users at GALAXI.',
        tangodevice = s7_digital + 'voice_output',
        visibility = (),
        fmtstr = '%d',
        unit = '',
    ),
    vacuumoperation = device('nicos_jcns.galaxi.devices.automation.VacuumOperation',
        description = 'Automatic vacuum/ventilation operations.',
        tangodevice = s7_digital + 'VacuumMode',
        mapping = dict(
            idle = 0,
            chamber1_vent = 1,
            chamber1_evacuate = 2,
            samplechamber_vent = 3,
            samplechamber_evacuate = 4,
            detector_open = 5,
            detector0 = 6,
            detector1 = 7,
            detector2 = 8,
            detector3 = 9,
            detector4 = 10,
        ),
        fmtstr = '%s',
    ),
)
