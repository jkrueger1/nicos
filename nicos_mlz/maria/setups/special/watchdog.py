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
#     type '' does not emit warnings (useful together with 'pausecount'
#     for conditions that should block counting but are not otherwise errors)
# 'pausecount' -- if True, the count loop should be paused on the condition
#     (default False)
# 'action' -- code to execute if condition is true (default no code is executed)
watch_conditions = [
    dict(
        condition = '(sixfold_value == \'closed\' or nl5_value == \'closed\') '
                    'and reactorpower_value > 19.1',
        message = 'NL5 or sixfold shutter closed',
        type = 'critical',
    ),
    dict(
        condition = 'selector_speed_status[0] == ERROR',
        message =
        'Selector in error status. Please check selector2.maria.frm2.',
        type = 'critical',
    ),
    dict(
        condition = 'selector_speed_target > 0 '
                    'and selector_vacuum_status[0] == WARN',
        message = 'Selector vacuum in warning range.',
        type = 'default',
    ),
]

includes = ['notifiers']

notifiers = {
    'default':  ['mailer'],
    'critical': ['mailer', 'smser'],
}

devices = dict(
    Watchdog = device('nicos.services.watchdog.Watchdog',
        cache = 'localhost',
        notifiers = notifiers,
        mailreceiverkey = 'email/receivers',
        watch = watch_conditions,
    ),
)
