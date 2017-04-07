# -*- coding: utf-8 -*-

from OglasModel import *
from peewee import *


db = SqliteDatabase('test.db')
db.connect()

db.create_tables([Zupanija, Grad, Naselje, Oglas])

zupanije = ['Bjelovarsko-bilogorska', 'Brodsko-posavska', 'Dubrovačko-neretvanska', 'Istarska',
            'Karlovačka', 'Koprivničko-križevečka', 'Krapinsko-zagorska', 'Ličko-senjska',
            'Međimurska', 'Osječko-baranjska', 'Požeško-slavnoska', 'Primorsko-goranska', 'Sisačko-moslavačka',
            'Splitsko-dalmatinska', 'Šibensko-kninska', 'Varaždinska', 'Virovitičko-podravksa',
            'Vukovarsko-srijemska', 'Zadarska', 'Grad Zagreb', 'Zagrebačka']

for z in zupanije:

    zup = Zupanija(ime=z)
    zup.save()
