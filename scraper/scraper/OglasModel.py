# TODO: Add Bool visible field to the Oglas model, to be used by pipeline - checking if Oglas is active or expired
# TODO: Don't forget to add fields that will be parsed in the future

from peewee import *


class BaseModel(Model):
    class Meta:
        database = SqliteDatabase('nekretnine.db')


class Zupanija(BaseModel):
    ime = TextField()

    class Meta:
        pass


class Grad(BaseModel):
    ime = TextField()
    zup = ForeignKeyField(Zupanija)

    class Meta:
        pass


class Naselje(BaseModel):
    ime = TextField()
    grad = ForeignKeyField(Grad)

    class Meta:
        pass


class Oglas(BaseModel):
    cijena = IntegerField()
    m2 = FloatField()
    link = TextField()
    tip = TextField()
    scraped = TextField()
    zup = ForeignKeyField(Zupanija)
    grad = ForeignKeyField(Grad)
    naselje = ForeignKeyField(Naselje)

    class Meta:
        pass
