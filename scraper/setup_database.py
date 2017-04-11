# -*- coding: utf-8 -*-

from scraper.OglasModel import *
from peewee import *

db = SqliteDatabase('nekretnine.db')
db.create_tables([Zupanija, Grad, Naselje, Oglas])