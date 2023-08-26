from peewee import CharField, DateField, Model


class User(Model):
    _id = CharField()
    name = CharField()
    email = CharField()
    password = CharField()
    created_at = DateField()
