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
    scraped = datetime.datetime.now()
    zupanija = scrapy.Field()
    grad = scrapy.Field()
    naselje = scrapy.Field()
    m2 = scrapy.Field()
