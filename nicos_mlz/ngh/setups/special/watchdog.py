description = 'setup for the NICOS watchdog'
group = 'special'

# watchlist:
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
watchlist = [
    dict(
        condition = 't_in_memograph_kws123_value > 3',
        message = 'Temperatur zu hoch (T_in KWS-123)',
        priority = 1,
        gracetime = 5
    ),
]

includes = ['notifiers']

devices = dict(
    Watchdog = device('nicos.services.watchdog.Watchdog',
        cache = 'localhost:14869',
        notifiers = {1: ['email']},
        mailreceiverkey = 'email/receivers',
        watch = watchlist,
    ),
)
