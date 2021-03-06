description = 'memograph readout'

group = 'optional'

devices = dict(
    t_in_fak40 = device('nicos_mlz.devices.memograph.MemographValue',
        hostname = 'memograph02.care.frm2',
        group = 1,
        valuename = 'T_in MIRA',
        description = 'inlet temperature memograph',
        fmtstr = '%.2F',
        warnlimits = (-1, 17.5), #-1 no lower value
        unit = 'degC',
    ),
    t_out_fak40 = device('nicos_mlz.devices.memograph.MemographValue',
        hostname = 'memograph02.care.frm2',
        group = 1,
        valuename = 'T_out MIRA',
        description = 'outlet temperature memograph',
        pollinterval = 30,
        maxage = 60,
        fmtstr = '%.2F',
        unit = 'degC',
    ),
    p_in_fak40 = device('nicos_mlz.devices.memograph.MemographValue',
        hostname = 'memograph02.care.frm2',
        group = 1,
        valuename = 'P_in MIRA',
        description = 'inlet pressure memograph',
        pollinterval = 30,
        maxage = 60,
        fmtstr = '%.2F',
        unit = 'bar',
    ),
    p_out_fak40 = device('nicos_mlz.devices.memograph.MemographValue',
        hostname = 'memograph02.care.frm2',
        group = 1,
        valuename = 'P_out MIRA',
        description = 'outlet pressure memograph',
        pollinterval = 30,
        maxage = 60,
        fmtstr = '%.2F',
        unit = 'bar',
    ),
    flow_in_fak40 = device('nicos_mlz.devices.memograph.MemographValue',
        hostname = 'memograph02.care.frm2',
        group = 1,
        valuename = 'FLOW_in MIRA',
        description = 'inlet flow memograph',
        pollinterval = 30,
        maxage = 60,
        fmtstr = '%.2F',
        warnlimits = (0.2, 100), #100 no upper value
        unit = 'l/min',
    ),
    flow_out_fak40 = device('nicos_mlz.devices.memograph.MemographValue',
        hostname = 'memograph02.care.frm2',
        group = 1,
        valuename = 'FLOW_out MIRA',
        description = 'outlet flow memograph',
        pollinterval = 30,
        maxage = 60,
        fmtstr = '%.2F',
        unit = 'l/min',
    ),
    leak_fak40 = device('nicos_mlz.devices.memograph.MemographValue',
        hostname = 'memograph02.care.frm2',
        group = 1,
        valuename = 'Leak MIRA',
        description = 'leakage memograph',
        pollinterval = 30,
        maxage = 60,
        fmtstr = '%.2F',
        warnlimits = (-1, 1), #-1 no lower value
        unit = 'l/min',
    ),
    cooling_fak40 = device('nicos_mlz.devices.memograph.MemographValue',
        hostname = 'memograph02.care.frm2',
        group = 1,
        valuename = 'Cooling MIRA',
        description = 'cooling memograph',
        pollinterval = 30,
        maxage = 60,
        fmtstr = '%.2F',
        unit = 'kW',
    ),
)
