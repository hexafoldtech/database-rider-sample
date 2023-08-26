from peewee import BooleanField, CharField, DateField, DecimalField, IntegerField, Model


class User(Model):
    _id = CharField()
    name = CharField()
    email = CharField()
    password = CharField()
    created_at = DateField()
