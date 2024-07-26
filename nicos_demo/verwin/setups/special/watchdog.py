
description = 'setup for the NICOS watchdog'
group = 'special'

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
#   The time a precondition must be fulfilled. Default is 5 seconds.
# 'message' -- warning message to display
# 'type' -- for defining different types of warnings; this corresponds to the
#   configured notifiers (default 'default')
#   type '' does not emit warnings (useful together with scriptaction)
# 'scriptaction' -- 'pausecount' to pause the count loop on the condition
#   or 'stop' or 'immediatestop' to cancel script execution
#   (default '')
# 'action' -- code to execute if condition is true (default no code is executed)

watch_conditions = [
    dict(condition = 'LogSpace_status[0] == WARN',
         message = 'Disk space for the log files becomes too low.',
         type = 'critical',
         gracetime = 30,
    ),
    dict(condition = 'Space_status[0] == WARN',
         message = 'Disk space for the data files becomes too low.',
         type = 'critical',
         gracetime = 10,
    ),
    dict(condition = 's_tripped_value == "Trip"',
         # precondition = 's_hv_value != "Off"',
         # precondtime = 60,
         # setup = 'source',
         message = 'Small detector high voltage current too high',
         type = 'critical',
         action = 'maw(s_hv, "off")',
         actiontimeout = 600,
         # gracetime = 5,
    ),
    dict(condition = 'b_tripped_value == "Trip"',
         # precondition = 's_hv_value != "Off"',
         # precondtime = 60,
         # setup = 'source',
         message = 'Big detector high voltage current too high',
         type = 'critical',
         action = 'maw(b_hv, "off")',
         actiontimeout = 600,
         # gracetime = 5,
    ),
]

# The Watchdog device has two lists of notifiers, one for priority 1 ('default')
# and one for priority 2 ('critical').

devices = dict(
    Watchdog = device('nicos.services.watchdog.Watchdog',
        cache = 'localhost:14869',
        notifiers = {'default': [],
                     'critical': []},
        watch = watch_conditions,
        loglevel = 'debug',
    ),
)
