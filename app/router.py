from fastapi import FastAPI

from app.user.router import user_router


def init_routes(app: FastAPI) -> None:
    app.include_router(user_router)

