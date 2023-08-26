from core.config import config
from core.database.base import Database


class PostgresDatabase(Database):
    def connection(self) -> str:
        user = config().postgres.user
        password = config().postgres.password
        host = config().postgres.host
        db = config().postgres.db
        return f"postgresql+asyncpg://{user}:{password}@{host}:5432/{db}"

