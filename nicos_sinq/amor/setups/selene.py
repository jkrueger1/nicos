description = 'Selene support devices in AMOR'

display_order = 25

devices = dict(
    selene = device('nicos_sinq.amor.devices.selene.Selene',
        description = 'Selene support devices in AMOR',
        position = [-1.1 for _ in range(36)],
        low_limit_narrow = [-2.0 for _ in range(36)],
        high_limit_narrow = [2.0 for _ in range(36)],
        low_limit_wide = [-10.0 for _ in range(36)],
        high_limit_wide = [10.0 for _ in range(36)],
        working_position = [0.0 for _ in range(36)],
        backup_path = '/home/amor/nicos/backup',
        motor = ['smp1', 'smp2'],
        range_selector = ['mcu1', 'mcu2'],
        digital_input = [f'p{(p + 1):02d}' for p in range(36)],
        asyn = 'selene_asyn_channel',
    ),
    selene_asyn_channel = device('nicos_sinq.devices.epics.extensions.EpicsCommandReply',
        description = 'Direct communication to the mcu',
        commandpv = 'SQ:AMOR:SEL2.AOUT',
        replypv = 'SQ:AMOR:SEL2.AINP'
    ),
    smp1 = device('nicos_sinq.amor.devices.selene.SeleneEpicsMotor',
        description = 'Pitch motor for selene1',
        readpv = 'SQ:AMOR:SEL2:MIRROR1.RBV',
        writepv = 'SQ:AMOR:SEL2:MIRROR1.VAL',
        motorpv = 'SQ:AMOR:SEL2:MIRROR1',
        errormsgpv = 'SQ:AMOR:SEL2:MIRROR1-MsgTxt',
        abslimits = (-10.0, 10.0),
    ),
    mcu1 = device('nicos_sinq.amor.devices.selene.RangeSelector',
        description = 'Motor control unit for selene2',
        id = 1,
        readpv = 'SQ:AMOR:SEL2:MCU1:FineAdjustment:Selected',
        writepv = 'SQ:AMOR:SEL2:MCU1:FineAdjustment:Select',
        pvprefix = 'SQ:AMOR:SEL2',
    ),
    smp2 = device('nicos_sinq.amor.devices.selene.SeleneEpicsMotor',
        description = 'Pitch motor for selene2',
        readpv = 'SQ:AMOR:SEL2:MIRROR2.RBV',
        writepv = 'SQ:AMOR:SEL2:MIRROR2.VAL',
        motorpv = 'SQ:AMOR:SEL2:MIRROR2',
        errormsgpv = 'SQ:AMOR:SEL2:MIRROR2-MsgTxt',
        abslimits = (-10.0, 10.0),
    ),
    mcu2 = device('nicos_sinq.amor.devices.selene.RangeSelector',
        description = 'Motor control unit for selene2',
        id = 2,
        readpv = 'SQ:AMOR:SEL2:MCU2:FineAdjustment:Selected',
        writepv = 'SQ:AMOR:SEL2:MCU2:FineAdjustment:Select',
        pvprefix = 'SQ:AMOR:SEL2',
    ),
    sel2 = device('nicos_sinq.devices.epics.extensions.EpicsCommandReply',
        description = 'Controller of the devices connected to the selene MCU',
        commandpv = 'SQ:AMOR:SEL2' + '.AOUT',
        replypv = 'SQ:AMOR:SEL2' + '.AINP',
    ),
)

for p in range(1, 37):
    devices[f'p{p:02d}'] = device('nicos_sinq.amor.devices.selene.DigitalInput',
        description = 'Digital input for the pitch %d' % p,
        pitch = p,
        pvprefix = 'SQ:AMOR:SEL2',
        readpv = f'SQ:AMOR:SEL2:P{p}:Selected',
        fmtstr = '%d',
        pollinterval = 5,
    )