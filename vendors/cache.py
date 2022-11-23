from flask_caching import Cache


config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_TYPE": "SimpleCache",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}

cache = Cache(config=config)

def init_cache(_app):
    cache.init_app(_app)

def get_cache(key):
    return cache.get(key)


def set_cache(key, data):

    cache.set(key, data)

    return cache.get(key)