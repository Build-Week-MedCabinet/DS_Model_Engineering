"""
Unpickle and load complex objects into memory/application environment
"""

from django.core.cache import cache

# Debug and Logging
import logging


logger = logging.getLogger(__name__)


def cache_file(file_key, file=None):
    myobj = cache.get(file_key)
    if myobj is None:
        if file is None:
            return False
        else:
            try:
                add_to_cache(file_key, file)
                logger.info('Successfully cached '+file_key)
                return True
            except:
                logger.info('Unable to cache '+file_key)
                return False
    else:
        return False


def add_to_cache(key, item, duration=None):
    cache.set(key, item, duration)
