import databases


class Database:
    def __init__(self) -> None:
        self.database: databases.Database = databases.Database(self.connection())

    def session(self) -> databases.Database:
        return self.database

    def connection(self) -> str:
        pass

    async def startup(self) -> None:
        await self.database.connect()

    async def shutdown(self) -> None:
        await self.database.disconnect()
