from flask_caching import Cache
import redis

cache = redis.Redis(host='redis', port=6379)


def get_cache(key):
    return cache.get(key)


def set_cache(key, data):

    cache.set(key, data)

    return cache.get(key)