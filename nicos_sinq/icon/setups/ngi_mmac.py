description = 'Yet another neutron grating interferometry setup'

pvprefix = 'SQ:NGI:mmac:'

devices = dict(
    g0_lin = device('nicos_sinq.devices.epics.motor.EpicsMotor',
        description = 'G0 translation',
        motorpv = pvprefix + 'g0-lin',
        errormsgpv = pvprefix + 'g0-lin-MsgTxt',
        precision = 0.05,
        can_disable = True,
    ),
    g0_rot = device('nicos_sinq.devices.epics.motor.EpicsMotor',
        description = 'G0 rotation',
        motorpv = pvprefix + 'g0-rot',
        errormsgpv = pvprefix + 'g0-rot-MsgTxt',
        precision = 0.05,
        can_disable = True,
    ),
    g1_lin = device('nicos_sinq.devices.epics.motor.EpicsMotor',
        description = 'G1 translation',
        motorpv = pvprefix + 'g1-lin',
        errormsgpv = pvprefix + 'g1-lin-MsgTxt',
        precision = 0.05,
        can_disable = True,
    ),
    g1_rot = device('nicos_sinq.devices.epics.motor.EpicsMotor',
        description = 'G1 rotation',
        motorpv = pvprefix + 'g1-rot',
        errormsgpv = pvprefix + 'g1-rot-MsgTxt',
        precision = 0.05,
        can_disable = True,
    ),
    g2_rot = device('nicos_sinq.devices.epics.motor.EpicsMotor',
        description = 'G2 rotation',
        motorpv = pvprefix + 'g2-rot',
        errormsgpv = pvprefix + 'g2-rot-MsgTxt',
        precision = 0.05,
        can_disable = True,
    ),
    samtry = device('nicos_sinq.devices.epics.motor.EpicsMotor',
        description = 'Sample TR y translation',
        motorpv = pvprefix + 'samtry',
        errormsgpv = pvprefix + 'samtry-MsgTxt',
        precision = 0.05,
        can_disable = True,
    ),
    samtrx = device('nicos_sinq.devices.epics.motor.EpicsMotor',
        description = 'Sample TR x translation',
        motorpv = pvprefix + 'samtrx',
        errormsgpv = pvprefix + 'samtrx-MsgTxt',
        precision = 0.05,
        can_disable = True,
    ),
    samtrz = device('nicos_sinq.devices.epics.motor.EpicsMotor',
        description = 'Sample TR z translation',
        motorpv = pvprefix + 'samtrz',
        errormsgpv = pvprefix + 'samtrz-MsgTxt',
        precision = 0.05,
        can_disable = True,
    ),
)