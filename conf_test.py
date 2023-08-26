from peewee import PostgresqlDatabase
import logging
from typing import Generator

import pytest
from core.database import db, postgres_container
from database_rider import setup_db_rider
from fastapi.testclient import TestClient

from main import create_app
from tests.models import User


#Peewee logger
logger = logging.getLogger("peewee")
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)

# Faker logger
logger = logging.getLogger("faker")
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)


@pytest.fixture
def header() -> dict:
    return {"Authorization": "Bearer my.jwt.token"}


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(create_app()) as c:
        yield c

@pytest.fixture(scope="session", autouse=True)
def create_schema() -> Generator:
    database = PostgresqlDatabase(db.connection().replace("+psycopg2", ""))
    setup_db_rider(database)
    models = [
        User
    ]
    database.bind(models)
    database.create_tables(models)
    yield


@pytest.fixture(scope="session", autouse=True)
def shutdown_pg_container() -> Generator:
    yield
    postgres_container.stop()
