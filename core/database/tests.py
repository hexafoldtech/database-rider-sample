from core.database.base import Database


class TestsDatabase(Database):
    def __init__(self, conn_url: str) -> None:
        self.connection_url = conn_url
        super().__init__()

    def connection(self) -> str:
        return self.connection_url
