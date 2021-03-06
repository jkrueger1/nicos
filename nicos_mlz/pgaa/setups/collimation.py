description = 'collimation devices'

group = 'lowlevel'

nethost = 'pgaasrv.pgaa.frm2'

devices = dict(
    ell = device('nicos.devices.taco.io.DigitalOutput',
        description = '',
        tacodevice = '//pgaasrv/pgaa/sample/elcol_press1',
        lowlevel = True,
        fmtstr = '%d',
    ),
    col = device('nicos.devices.taco.io.DigitalOutput',
        description = '',
        tacodevice = '//pgaasrv/pgaa/sample/elcol_press2',
        lowlevel = True,
        fmtstr = '%d',
    ),
    ellcol = device('nicos_mlz.pgaa.devices.BeamFocus',
        description = 'Switches between focused and collimated Beam',
        ellipse = 'ell',
        collimator = 'col',
        unit = ''
    ),
)
