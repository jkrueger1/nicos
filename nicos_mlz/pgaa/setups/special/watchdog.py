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
    # dict(condition = 't_value > 100',
    #      message = 'Temperature too high',
    #      type = 'critical',
    #      action = 'maw(T, 0)',
    # ),
    # dict(condition = 'phi_value > 100 and mono_value > 1.5',
    #      message = 'phi angle too high for current mono setting',
    #      gracetime = 5,
    # ),
]

includes = ['notifiers']

notifiers = {
    'default': ['email'],
    'critical': ['email', 'smser'],
    'logspace': ['email', 'smser', 'logspace_notif'],
}

devices = dict(
    Watchdog = device('nicos.services.watchdog.Watchdog',
        cache = 'tequila.pgaa.frm2.tum.de:14869',
        notifiers = notifiers,
        mailreceiverkey = 'email/receivers',
        watch = watch_conditions,
    ),
)
