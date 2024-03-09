description = 'Email and SMS notifiers'

group = 'lowlevel'

devices = dict(
    # Configure source and copy addresses to an existing address.
    email    = device('nicos.devices.notifiers.Mailer',
        sender = 'spodi@frm2.tum.de',
        copies = [('markus.hoelzel@frm2.tum.de', 'all'),   # gets all messages
                  ('anatoliy.senyshyn@frm2.tum.de', 'all'),   # gets all messages
                  ('josef.pfanzelt@frm2.tum.de', 'important')], # gets only important messages
        subject = 'SPODI',
        mailserver ='mailhost.frm2.tum.de',
    ),
    ngmail = device('nicos.devices.notifiers.Mailer',
        sender = 'spodi@frm2.tum.de',
        copies = [('markus.hoelzel@frm2.tum.de', 'all'),   # gets all messages
                  ('anatoliy.senyshyn@frm2.tum.de', 'all'),   # gets all messages
                  ('josef.pfanzelt@frm2.tum.de', 'important')], # gets only important messages
        subject = 'SPODI/Neutron guide',
        mailserver ='mailhost.frm2.tum.de',
    ),
    # Configure SMS receivers if wanted and registered with IT.
    smser = device('nicos.devices.notifiers.SMSer',
        server = 'triton.admin.frm2.tum.de',
        receivers = [],
    ),
)
