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
         type = 'critical',
         gracetime = 30,
        ),
    dict(condition = 'reactorpower_value < 19',
         message = 'Possible Reactor Shutdown! Reactor power < 19MW',
         type = 'critical',
         setup = 'reactor',
         gracetime = 300,
        ),
    # dict(condition = 'He_pressure_value < 30',
    #      message = 'Pressure in He bottle less than 30bar. Please change soon!',
    #      type = 'default',
    #      setup = 'reactor',
    #      gracetime = 300,
    #     ),
    # dict(condition = 'selector_vacuum_value > 0.005',
    #      message = 'Selector vacuum above 5E-3mbar!',
    #      type = 'default',
    #      setup = 'selector',
    #      gracetime = 30,
    #     ),
    dict(condition = 'DataSpace_value < 100',
         message = 'data is running out of space. Only 100GB left!',
         type = 'default',
         setup = 'system',
         gracetime = 300,
        ),
]

devices = dict(
    Watchdog = device('nicos.services.watchdog.Watchdog',
        # use only 'localhost' if the cache is really running on
        # the same machine, otherwise use the official computer
        # name
        cache = configdata('config_data.host'),
        # notifiers = notifiers,
        mailreceiverkey = 'email/receivers',
        watch = watch_conditions,
    ),
)
