description = 'system setup for the HERMES time-of-flight reflectometer'
group = 'lowlevel'

sysconfig = dict(
    cache = 'localhost',
    instrument = 'HERMES',
    experiment = 'Exp',
    datasinks = ['conssink', 'daemonsink', 'liveviewsink'],
    notifiers = ['email'],
)

modules = ['nicos.commands.standard']

includes = ['notifiers']

devices = dict(
    HERMES = device('nicos.devices.instrument.Instrument',
        description = 'HERMES time-of-flight reflectometer in COSY\'s Big '
                      'Karl experimental area.',
        instrument = 'HERMES',
        responsible = 'Ulrich Rücker <u.ruecker@fz-juelich.de>',
        facility = 'Forschungszentrum Jülich',
        operators = ['Jülich Centre for Neutron Science (JCNS)',
                     'Nuclear Physics Institute (IKP)'],
    ),
    Sample = device('nicos.devices.sample.Sample',
        description = 'Currently used sample.',
    ),
    Exp = device('nicos.devices.experiment.Experiment',
        description = 'HERMES experiment object.',
        dataroot = '/data',
        managerights = dict(
            enableDirMode = 0o775,
            enableFileMode = 0o664,
            disableDirMode = 0o775,
            disableFileMode = 0o664,
            owner = 'jcns',
            group = 'jcns'
        ),
        mailserver = 'mail.fz-juelich.de',
        mailsender = 'hermes@fz-juelich.de',
        sendmail = False,
        zipdata = True,
        serviceexp = 'service',
        sample = 'Sample',
    ),
    conssink = device('nicos.devices.datasinks.ConsoleScanSink',
    ),
    daemonsink = device('nicos.devices.datasinks.DaemonSink',
    ),
    filesink = device('nicos.devices.datasinks.AsciiScanfileSink',
        description = 'Device storing scanfiles in Ascii output format.',
        filenametemplate = ['%(session.experiment.users)s_'
                            '%(session.experiment.sample.filename)s_'
                            '%(session.experiment.lastscan)s.dat'],
    ),
    liveviewsink = device('nicos.devices.datasinks.LiveViewSink',
        description = 'Device showing live data during measurements.',
    ),
    Space = device('nicos.devices.generic.FreeSpace',
        description = 'The amount of free space for storing data.',
        path = None,
        minfree = 5,
    ),
)