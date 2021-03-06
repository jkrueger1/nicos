description = 'Pixelman Detector UDP interface'

devices = dict(
    pixelman_udp=device('nicos_ess.v20.devices.pixelman.PixelmanUDPChannel',
                        description='Pixelman detector UDP interface',
                        host='192.168.1.102:5150',
                        acquire='ACQUIRE',
                        finished='FINISHED',
                        lowlevel=True
                        ),
    det=device('nicos.devices.generic.Detector',
               description='Pixelman Detector',
               others=['pixelman_udp'])
)
