from functools import lru_cache

from pydantic.v1 import BaseSettings


class Postgres(BaseSettings):
    user: str = "user"
    password: str = "user"
    host: str = "password"
    db: str = "postgres"

    class Config:
        env_prefix = "postgres_"


class Settings(BaseSettings):

    PROJECT_NAME: str = "Database Rider 🔥"
    PROJECT_VERSION: str = "1.0.0"

    debug: bool = True

    env: str = "debug"

    class Config:
        env_file = ".env"


@lru_cache
def get_config() -> Settings:
    return Settings()


def config() -> Settings:
    return get_config()
