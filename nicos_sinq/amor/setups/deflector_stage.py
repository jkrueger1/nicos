description = 'Lift and pitch of deflector and flight tube'

display_order = 40

includes = [
    'base', 'diaphragm2', 'sample_stage', 'detector_stage'
    ]

pvprefix = 'SQ:AMOR:masterMacs1:'

devices = dict(
    ltz_r = device('nicos_sinq.devices.epics.sinqmotor_deprecated.SinqMotor',
        description = 'Lift (z translation) of deflector & flight tube',
        motorpv = pvprefix + 'ltz',
        unit = 'mm',
        visibility = ('devlist', 'metadata', 'namespace'),
    ),
    lom_r = device('nicos_sinq.devices.epics.sinqmotor_deprecated.SinqMotor',
        description = 'Tilt (pitch) of deflector & flight tube',
        motorpv = pvprefix + 'lom',
        unit = 'deg',
        visibility = ('devlist', 'metadata', 'namespace'),
    ),
)
