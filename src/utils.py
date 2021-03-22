from functools import lru_cache
from . import config
from passlib.context import CryptContext

#for caching .env file
@lru_cache()
def get_settings():
    return config.Settings()

#for password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    def get_password_hash(password):
        return pwd_context.hash(password)
