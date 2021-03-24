from functools import lru_cache
from . import config
from passlib.context import CryptContext
import shutil
import os

#for caching .env file
@lru_cache()
def get_settings():
    return config.Settings()

#todo attachments
def save_file_to_disk(uploaded_file, path=".", save_as="default"):
    extension = os.path.splitext(uploaded_file.filename)[-1]
    temp_file = os.path.join(path, save_as + extension)
    with open(temp_file, "wb") as buffer:
        shutil.copyfileobj(uploaded_file.file, buffer)
    return temp_file

#for password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    def get_password_hash(password):
        return pwd_context.hash(password)
