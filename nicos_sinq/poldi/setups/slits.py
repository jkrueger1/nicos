description = 'POLDI slits'

pvpref = 'SQ:POLDI:MCU1:'

devices = dict(
    d1hl = device('nicos_sinq.devices.epics.motor_deprecated.EpicsMotor',
        description = 'Slit 1 (horizontal) left',
        motorpv = pvpref + 'D1HL',
        errormsgpv = pvpref + 'D1HL-MsgTxt',
        precision = 0.01,
        can_disable = True,
    ),
    d1hr = device('nicos_sinq.devices.epics.motor_deprecated.EpicsMotor',
        description = 'Slit 1 (horizontal) right',
        motorpv = pvpref + 'D1HR',
        errormsgpv = pvpref + 'D1HR-MsgTxt',
        precision = 0.01,
        can_disable = True,
    ),
    d2hl = device('nicos_sinq.devices.epics.motor_deprecated.EpicsMotor',
        description = 'Slit 2 (horizontal) left',
        motorpv = pvpref + 'D2HL',
        errormsgpv = pvpref + 'D2HL-MsgTxt',
        precision = 0.01,
        can_disable = True,
    ),
    d2hr = device('nicos_sinq.devices.epics.motor_deprecated.EpicsMotor',
        description = 'Slit 2 (horizontal) right',
        motorpv = pvpref + 'D2HR',
        errormsgpv = pvpref + 'D2HR-MsgTxt',
        precision = 0.01,
        can_disable = True,
    ),
    d2vu = device('nicos_sinq.devices.epics.motor_deprecated.EpicsMotor',
        description = 'Slit 2 (vertical) upper',
        motorpv = pvpref + 'D2VU',
        errormsgpv = pvpref + 'D2HL-MsgTxt',
        precision = 0.01,
        can_disable = True,
    ),
    d2vl = device('nicos_sinq.devices.epics.motor_deprecated.EpicsMotor',
        description = 'Slit 2 (vertical) lower',
        motorpv = pvpref + 'D2VL',
        errormsgpv = pvpref + 'D2VL-MsgTxt',
        precision = 0.01,
        can_disable = True,
    ),
    d2x = device('nicos_sinq.devices.epics.motor_deprecated.AbsoluteEpicsMotor',
        description = 'Slit 2 X translation',
        motorpv = pvpref + 'D2X',
        errormsgpv = pvpref + 'D2X-MsgTxt',
        precision = 0.01,
        can_disable = True,
        absolute_encoder = True,
    ),
)
