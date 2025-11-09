
devices = dict(
    symmetry = device('nicos.devices.generic.ManualSwitch',
        states = ['symmetric', 'short', 'unsymmetric'],
    ),
    enable = device('nicos.devices.generic.ManualSwitch',
        states = ['on', 'off']
    ),
    current = device('nicos.devices.generic.VirtualMotor',
        abslimits = (-100, 100),
        unit = 'A',
    ),
    magnet = device('nicos_mlz.devices.amagnet.GarfieldMagnet',
        currentsource = 'current',
        enable = 'enable',
        symmetry = 'symmetry',
        unit = 'T',
        calibrationtable = dict(
            symmetric = (
                0.00186517, 0.0431937, -0.185956, 0.0599757, 0.194042
            ),
            short = (0.0, 0.0, 0.0, 0.0, 0.0),
            unsymmetric = (
                0.00136154, 0.027454, -0.120951, 0.0495289, 0.110689
            ),
        ),
        userlimits = (-0.35, 0.35),
        fmtstr = '%.4f',
    ),
    rmagnet = device('nicos_mlz.devices.amagnet.GarfieldMagnet',
        currentsource = 'current',
        currentreadback = 'current',
        enable = 'enable',
        symmetry = 'symmetry',
        unit = 'T',
        calibrationtable = dict(
            symmetric = (
                0.00186517, 0.0431937, -0.185956, 0.0599757, 0.194042
            ),
            short = (0.0, 0.0, 0.0, 0.0, 0.0),
            unsymmetric = (
                0.00136154, 0.027454, -0.120951, 0.0495289, 0.110689
            ),
        ),
        userlimits = (-0.35, 0.35),
        fmtstr = '%.4f',
    ),
)
