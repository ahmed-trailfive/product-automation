from pydantic import BaseSettings
from firebase_admin import credentials


class CommonSettings(BaseSettings):
    APP_NAME: str = "Product Automation"
    DEBUG_MODE: bool = True


class ServerSettings(BaseSettings):
    HOST: str = "0.0.0.0"
    PORT: int = 8000


class DatabaseSettings(BaseSettings):
    CRED = credentials.Certificate("serviceAccountKey.json")


class Settings(CommonSettings, ServerSettings, DatabaseSettings):
    pass
