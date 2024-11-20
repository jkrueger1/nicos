description = 'Email and SMS notifiers'

group = 'lowlevel'

devices = dict(
    email = device('nicos.devices.notifiers.Mailer',
        description = 'E-Mail notifier',
        mailserver = 'mailhost.frm2.tum.de',
        sender = 'dns@frm2.tum.de',
        copies = [
            ('y.su@fz-juelich.de', 'all'),
            ('t.mueller@fz-juelich.de', 'all'),
            ('g.brandl@fz-juelich.de', 'all'),
            ('l.fleischhauer-fuss@fz-juelich.de', 'important'),
        ],
        subject = '[NICOS] DNS',
    ),
    smser = device('nicos.devices.notifiers.SMSer',
        description = 'SMS notifier',
        server = 'triton.admin.frm2.tum.de',
    ),
)
