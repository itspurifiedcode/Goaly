from functools import lru_cache
from . import config

@lru_cache()
def get_settings():
    return config.Settings()