from functools import lru_cache
from . import config
from passlib.context import CryptContext
import shutil
import os
from jose import JWTError, jwt
from datetime import datetime, timedelta
from .schemas import auth_schema

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
        
    def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

# for JWT authentication
SECRET_KEY = get_settings().SECRET_KEY
ALGORITHM = get_settings().ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = get_settings().ACCESS_TOKEN_EXPIRE_MINUTES

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token:str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("email")
        if email is None:
            raise credentials_exception
        token_data = auth_schema.TokenData(email=email)
    except JWTError:
        raise credentials_exception