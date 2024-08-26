description = 'setup for the NICOS watchdog'
group = 'special'

# watch_conditions:
# The entries in this list are dictionaries. Possible keys:
#
# 'setup' -- setup that must be loaded (default '' to mean all setups)
# 'condition' -- condition for warning (a Python expression where cache keys
#    can be used: t_value stands for t/value etc.
# 'gracetime' -- time in sec allowed for the condition to be true without
#    emitting a warning (default 5 sec)
# 'precondition'
#   If present, this condition must be fulfilled for at least ``precondtime``,
#   before condition will trigger. Default is no precondition.
# 'precondtime'
#   The time a precondition must be fulfilled. Default is 5 seconds
# 'message' -- warning message to display
# 'type' -- for defining different types of warnings; this corresponds to the
#     configured notifiers (default 'default')
#     type '' does not emit warnings (useful together with scriptaction)
# 'scriptaction' -- 'pausecount' to pause the count loop on the condition
#     or 'stop' or 'immediatestop' to cancel script execution
#     (default '')
# 'action' -- code to execute if condition is true (default no code is executed)
watch_conditions = [
    dict(condition = 'LogSpace_status[0] == WARN',
         message = 'Disk space for log files becomes too low.',
         type = 'logspace',
         gracetime = 30,
    ),
    dict(
        condition = 'reactorpower_value < 10',
        precondition = 'reactorpower_value > 19.1',
        precondtime = 600,
        message = 'Reactor power too low',
        type = 'critical',
        # action = 'stop()',
        gracetime = 300,
        setup = 'reactor',
    ),
    dict(
        condition = 'hv1_value < 3000',
        precondition = 'hv1_value > 3150',
        precondtime = 600,
        message = 'High voltage problem (anode voltage felt down)',
        type = 'highvoltage',
        gracetime = 5,
        setup = 'detector',
    ),
    dict(
        condition = 'hv2_value > -2300',
        precondition = 'hv1_value < -2450',
        precondtime = 600,
        message = 'High voltage problem (drift voltage felt down)',
        type = 'highvoltage',
        gracetime = 5,
        setup = 'detector',
    ),
]

includes = ['notifiers']

notifiers = {
    'default': ['email'],
    'critical': ['email', 'smser'],
    'highvoltage': ['hvemail', 'smser'],
    'logspace': ['email', 'smser', 'logspace_notif'],
}

devices = dict(
    Watchdog = device('nicos.services.watchdog.Watchdog',
        # use only 'localhost' if the cache is really running on
        # the same machine, otherwise use the official computer
        # name
        cache = 'stressictrl.stressi.frm2.tum.de',
        notifiers = notifiers,
        mailreceiverkey = 'email/receivers',
        watch = watch_conditions,
    ),
)
