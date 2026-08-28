from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    JWT_ALGORITHM: str = "ES256"
    JWT_PRIVATE_KEY: str
    JWT_PUBLIC_KEY: str
    JWT_ISSUER: str
    JWT_AUDIENCE: str
    ACCESS_TOKEN_MTL: int = 15
    REFRESH_TOKEN_DTL: int = 7
    CLOCK_SKEW_LEEWAY: int = 5

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()