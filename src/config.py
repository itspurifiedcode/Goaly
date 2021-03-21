from pydantic import BaseSettings

class Settings(BaseSettings):
    SQLALCHEMY_DB_URL: str

    class Config:
        env_file = ".env"
