description = 'Detector Table Experimental Chamber 1'

group = 'optional'

tango_base = 'tango://antareshw.antares.frm2:10000/antares/'

devices = dict(
    dtx = device('nicos.devices.tango.Motor',
        description = 'Detector Translation X',
        tangodevice = tango_base + 'fzjs7/X_det',
        abslimits = (0, 730),
        userlimits = (0, 730),
    ),
    dty = device('nicos.devices.tango.Motor',
        description = 'Detector Translation Y',
        tangodevice = tango_base + 'fzjs7/Y_det',
        abslimits = (0, 300),
        userlimits = (0, 300),
    ),
)
