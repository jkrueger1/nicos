description = 'neutron guide changer or collimator'

group = 'lowlevel'

nethost = 'toftofsrv.toftof.frm2'

devices = dict(
    ngc_motor = device('nicos.devices.taco.Motor',
        description = 'The TACO motor for the neutron guide changing '
        'mechanism',
        tacodevice = '//%s/toftof/huber/ccmot' % nethost,
        fmtstr = "%7.3f",
        userlimits = (-131.4, 0.),
        abslimits = (-131.4, 0.),
        requires = {'level': 'admin'},
        unit = 'mm',
        lowlevel = True,
    ),
    ngc = device('nicos_mlz.toftof.devices.neutronguide.Switcher',
        description = 'The neutron guide changer/collimator',
        moveable = 'ngc_motor',
        mapping = {
            'linear': -5.1,
            'focus': -131.25,
        },
        requires = {'level': 'admin'},
    ),
)
