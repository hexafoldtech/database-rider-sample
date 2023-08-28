import ormar
import sqlalchemy
from fastapi_sqlalchemy import db

Base = ormar.Model

metadata = sqlalchemy.MetaData()


class MainMeta(ormar.ModelMeta):
    metadata = metadata
    database = db.database
