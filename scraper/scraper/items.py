# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import datetime


class BaseOglasItem(scrapy.Item):

    cijena = scrapy.Field()
    sifra = scrapy.Field()
    objavljen = scrapy.Field()
    scraped = scrapy.Field()
    zupanija = scrapy.Field()
    grad = scrapy.Field()
    naselje = scrapy.Field()
    m2 = scrapy.Field()
    link = scrapy.Field()
    tip = scrapy.Field()

class IznmStanItem(BaseOglasItem):

    tip_stana = scrapy.Field()
    br_etaza = scrapy.Field()
    br_soba = scrapy.Field()
    lift = scrapy.Field()
    teretni_lift = scrapy.Field()
    god_adaptacije = scrapy.Field()
    blizina_bus = scrapy.Field()
    blizina_tram = scrapy.Field()
    br_parkmj = scrapy.Field()
    kat = scrapy.Field()
