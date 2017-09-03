# TODO: Add Bool visible field to the Oglas model, to be used by pipeline - checking if Oglas is active or expired
# TODO: Don't forget to add fields that will be parsed in the future

from peewee import *

myDb = MySQLDatabase('njuskalo', host='127.0.0.1', user='root', passwd='')


class BaseModel(Model):
    class Meta:
        # database = SqliteDatabase('nekretnine.db')
        database = myDb



class Zupanija(BaseModel):
    ime = CharField()

    class Meta:
        pass


class Grad(BaseModel):
    ime = CharField()
    zup = ForeignKeyField(Zupanija)

    class Meta:
        pass


class Naselje(BaseModel):
    ime = CharField()
    grad = ForeignKeyField(Grad)

    class Meta:
        pass


class Oglas(BaseModel):
    cijena = IntegerField()
    m2 = FloatField()
    link = CharField(unique=True)
    tip = CharField()
    scraped = CharField()
    zup = ForeignKeyField(Zupanija)
    grad = ForeignKeyField(Grad)
    naselje = ForeignKeyField(Naselje)
    active = BooleanField(default=True)
    last_active = CharField()

    class Meta:
        pass