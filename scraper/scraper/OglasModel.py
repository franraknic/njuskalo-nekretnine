from peewee import *


class BaseModel(Model):
    class Meta:
        database = SqliteDatabase('test.db', **{})


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
    cijena = TextField()
    link = TextField()
    zup = ForeignKeyField(Zupanija)
    grad = ForeignKeyField(Grad)
    naselje = ForeignKeyField(Naselje)

    class Meta:
        pass
