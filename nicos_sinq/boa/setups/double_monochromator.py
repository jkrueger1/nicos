description = 'BOA Double Monochromator'

pvprefix = 'SQ:BOA:mcu2:'

excludes = [
    'imaging_double_mono',
]

devices = dict(
    mth1 = device('nicos_sinq.devices.epics.motor.EpicsMotor',
        description = 'Double Monochromator Blade 1 Rotation',
        motorpv = pvprefix + 'MTH1',
        errormsgpv = pvprefix + 'MTH1-MsgTxt',
        precision = 0.02,
        can_disable = True,
    ),
    mth2 = device('nicos_sinq.devices.epics.motor.EpicsMotor',
        description = 'Double Monochromator Blade 2 Rotation',
        motorpv = pvprefix + 'MTH2',
        errormsgpv = pvprefix + 'MTH2-MsgTxt',
        precision = 0.02,
        can_disable = True,
    ),
    mtx = device('nicos_sinq.devices.epics.motor.EpicsMotor',
        description = 'Double Monochromator Translation',
        motorpv = pvprefix + 'MTX',
        errormsgpv = pvprefix + 'MTX-MsgTxt',
        precision = 0.02,
        can_disable = True,
    ),
    wavelength = device('nicos_sinq.devices.doublemono.DoubleMonochromator',
        description = 'SINQ Double Monochromator',
        unit = 'A',
        safe_position = 20.,
        dvalue = 3.335,
        distance = 100.,
        abslimits = (2.4, 6.2),
        mth1 = 'mth1',
        mth2 = 'mth2',
        mtx = 'mtx',
        precision = .01,
    ),
)
