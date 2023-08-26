from typing import Union

import uvicorn
from fastapi import FastAPI

from app.config import config
from app.router import init_routes


def create_app() -> FastAPI:
    app = FastAPI(title=config().PROJECT_NAME, version=config().PROJECT_VERSION)
    init_routes(app)
    return app


app = create_app()


@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
