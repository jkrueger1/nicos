description = 'system setup'

group = 'lowlevel'

sysconfig = dict(
    cache='localhost',
    instrument='DMC',
    experiment='Exp',
    datasinks=['conssink', 'dmnsink', 'NexusDataSink', 'HistogramDataSink'],
)

modules = ['nicos.commands.standard', 'nicos_ess.commands.file_writing',
           'nicos_sinq.commands.sics']

devices = dict(
    DMC=device('nicos.devices.instrument.Instrument',
               description='instrument object',
               instrument='SINQ DMC',
               responsible='Lukas Keller <lukas.keller@psi.ch>',
               operators=['Paul-Scherrer-Institut (PSI)'],
               facility='SINQ, PSI',
               website='https://www.psi.ch/sinq/dmc/',
               ),

    Sample=device('nicos.devices.sample.Sample',
                  description='The currently used sample',
                  ),

    Exp=device('nicos_sinq.devices.experiment.SinqExperiment',
               description='experiment object',
               dataroot=configdata('config.DATA_PATH'),
               sendmail=False,
               serviceexp='Service',
               sample='Sample',
               ),

    Space=device('nicos.devices.generic.FreeSpace',
                 description='The amount of free space for storing data',
                 path=None,
                 minfree=5,
                 ),

    KafkaForwarder=device(
        'nicos_ess.devices.forwarder.EpicsKafkaForwarder',
        description="Configures commands to forward-epics-to-kafka",
        cmdtopic="DMC_forwarderCommands",
        statustopic="DMC_forwarderStatus",
        instpvtopic="DMC_metadata",
        instpvschema='f142',
        brokers=configdata('config.KAFKA_BROKERS'),
    ),

    HistogramDataSink=device(
        'nicos_ess.devices.datasinks.imagesink.kafka.ImageKafkaDataSink',
        brokers=configdata('config.KAFKA_BROKERS'),
        channeltostream={
            'area_detector': ('DMC_bananaDetector', 'linear')
        },
    ),

    NexusDataSink=device(
        'nicos_sinq.devices.datasinks.SinqNexusFileSink',
        description="Sink for NeXus file writer (kafka-to-nexus)",
        brokers=configdata('config.KAFKA_BROKERS'),
        filenametemplate=['dmc%(year)sn%(pointcounter)06d.hdf'],
        cmdtopic="DMC_filewriterCommands",
        status_provider='NexusFileWriter',
        templatesmodule='nicos_sinq.dmc.nexus.nexus_templates',
        templatename='dmc_default'
    ),

    NexusFileWriter=device(
        'nicos_ess.devices.datasinks.nexussink.NexusFileWriterStatus',
        description="Status for nexus file writing",
        brokers=configdata('config.KAFKA_BROKERS'),
        statustopic="DMC_filewriterStatus",
    ),

    conssink=device('nicos.devices.datasinks.ConsoleScanSink'),

    dmnsink=device('nicos.devices.datasinks.DaemonSink')

)
