description = 'setup for the cache server'
group = 'special'

devices = dict(
    DB = device('nicos.services.cache.server.FlatfileCacheDatabase',
        storepath = '/data/cache',
        loglevel = 'info'
    ),
    Server = device('nicos.services.cache.server.CacheServer',
        db = 'DB',
        server = 'refsansctrl.refsans.frm2.tum.de',
        loglevel = 'info'
    ),
)
