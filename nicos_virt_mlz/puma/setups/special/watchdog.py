description = 'setup for the NICOS watchdog'
group = 'special'

# The entries in this list are dictionaries. Possible keys:
#
# 'setup' -- setup that must be loaded (default '' to mean all setups)
# 'condition' -- condition for warning (a Python expression where cache keys
#    can be used: t_value stands for t/value etc.
# 'gracetime' -- time in sec allowed for the condition to be true without
#    emitting a warning (default 5 sec)
# 'message' -- warning message to display
# 'priority' -- 1 or 2, where 2 is more severe (default 1)
# 'action' -- code to execute if condition is true (default no code is executed)

watch_conditions = [
    dict(condition = 'LogSpace_status[0] == WARN',
         message = 'Disk space for log files becomes too low.',
         type = 'critical',
         gracetime = 30,
    ),
    dict(
        condition = 'mono_status[0] == BUSY',
        message = 'mtt is not moving. Maybe hardware blocked? Mobile block?',
        gracetime = 600,
        type = 'critical',
    ),
]

# The Watchdog device has two lists of notifiers, one for priority 1 and
# one for priority 2.

devices = dict(
    Watchdog = device('nicos.services.watchdog.Watchdog',
        cache = 'localhost',
        notifiers = {'default': [],
                     'critical': []},
        watch = watch_conditions,
    ),
)
