description = 'qmesydaq devices for SANS1'

# included by sans1
group = 'lowlevel'

nethost = 'sans1srv.sans1.frm2'

sysconfig = dict(
    datasinks = ['BerSANSFileSaver', 'LivePNGSink', 'LivePNGSinkLog',
                 'DetectorSetup', 'DetectorCalibration'],
)

devices = dict(
    BerSANSFileSaver = device('nicos_mlz.sans1.devices.bersans.BerSANSImageSink',
        description = 'Saves image data in BerSANS format',
        filenametemplate = [
            'D%(pointcounter)07d.001', '/data_user/D%(pointcounter)07d.001'
        ],
        subdir = 'hist',
    ),
    # LiveViewSink = device('nicos.devices.datasinks.LiveViewSink',
    #     description = 'Sends image data to LiveViewWidget',
    #     filenametemplate=[],
    # ),
    LivePNGSinkLog = device('nicos.devices.datasinks.PNGLiveFileSink',
        description = 'Saves live image as .png every now and then',
        filename = '/sans1control/webroot/live_log.png',
        log10 = True,
        interval = 15,
    ),
    LivePNGSink = device('nicos.devices.datasinks.PNGLiveFileSink',
        description = 'Saves live image as .png every now and then',
        filename = '/sans1control/webroot/live_lin.png',
        log10 = False,
        interval = 15,
    ),
    Histogram = device('nicos_mlz.devices.qmesydaqsinks.HistogramSink',
        description = 'Histogram data written via QMesyDAQ',
        image = 'det1_image',
        subdir = 'mtxt',
        filenametemplate = ['%(pointcounter)07d.mtxt'],
    ),
    Listmode = device('nicos_mlz.devices.qmesydaqsinks.ListmodeSink',
        description = 'Listmode data written via QMesyDAQ',
        image = 'det1_image',
        subdir = 'list',
        filenametemplate = ['%(pointcounter)07d.mdat'],
    ),
    DetectorSetup = device('nicos_mlz.sans1.devices.copysink.CopySink',
        description = 'Save the current detector setup file',
        source = 'configfile',
        subdir = 'configs',
        path = '/data/qmesydaq/configs/configuration_2016_07_13',
        filenametemplate = ['config_%(pointcounter)07d.mcfg'],
    ),
    DetectorCalibration = device('nicos_mlz.sans1.devices.copysink.CopySink',
        description = 'Save the current detector calibration file',
        source = 'calibrationfile',
        subdir = 'configs',
        path = '/data/qmesydaq/configs/pos_calibration_2016_07_13',
        filenametemplate = ['calib_%(pointcounter)07d.txt'],
    ),
    det1_mon1 = device('nicos.devices.vendor.qmesydaq.taco.Counter',
        description = 'QMesyDAQ Counter0',
        tacodevice = '//%s/sans1/qmesydaq/counter0' % nethost,
        type = 'monitor',
    ),
    det1_mon2 = device('nicos.devices.vendor.qmesydaq.taco.Counter',
        description = 'QMesyDAQ Counter1',
        tacodevice = '//%s/sans1/qmesydaq/counter1' % nethost,
        type = 'monitor',
    ),
    det1_mon3 = device('nicos.devices.vendor.qmesydaq.taco.Counter',
        description = 'QMesyDAQ Counter2 (reference for tisane)',
        tacodevice = '//%s/sans1/qmesydaq/counter2' % nethost,
        type = 'monitor',
    ),
    det1_ev = device('nicos.devices.vendor.qmesydaq.taco.Counter',
        description = 'QMesyDAQ Events channel',
        tacodevice = '//%s/sans1/qmesydaq/events' % nethost,
        type = 'counter',
    ),
    det1_timer = device('nicos.devices.vendor.qmesydaq.taco.Timer',
        description = 'QMesyDAQ Timer',
        tacodevice = '//%s/sans1/qmesydaq/timer' % nethost,
    ),
    det1_image = device('nicos.devices.vendor.qmesydaq.taco.Image',
        description = 'QMesyDAQ Image',
        tacodevice = '//%s/sans1/qmesydaq/det' % nethost,
        flipaxes = [0],  # flip image up-down
    ),
    # the combined detector device is in sans1.py or tisane.py
)

startupcode = '''
SetDetectors(det1)
'''
