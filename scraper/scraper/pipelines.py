# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
# TODO: Add pipeline for data conversion, from string to numeric etc.


import sqlite3
from scrapy import log
from OglasModel import Oglas


class ScraperPipeline(object):

    def process_item(self, item):
        return item


class SQLPersist(object):

    def __init__(self):

        self.db_path = 'D:\\FINAL_QUESTION.db'
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS `oglasi` ( `id` INTEGER PRIMARY KEY AUTOINCREMENT, `cijena` TEXT, `link` TEXT, `objavljen` TEXT, `scraped` TEXT, `tip` TEXT, `zupanija` TEXT, `grad` TEXT, `naselje` TEXT, `m2` TEXT ); ")

    def process_item(self, item):

        self.cursor.execute('SELECT count(oglasi.link) FROM oglasi WHERE oglasi.link=?', (item['link'],))
        result = self.cursor.fetchone()

        if result[0] != 0:
            log.msg('Item %s in database!' % item['link'], level=log.WARNING)
        else:
            oglas = [(None, item['cijena'], item['link'], item['scraped'], item['objavljen'], item['tip'], item['zupanija'], item['grad'], item['naselje'], item['m2'])]
            self.cursor.executemany('INSERT INTO oglasi VALUES (?,?,?,?,?,?,?,?,?,?)', oglas)
            self.connection.commit()

        return item


class ORMPersist(object):

    def process_item(self, item):

        oglas = Oglas.create(link=item['link'], cijena=item['cijena'], zup_id=1, grad_id=1, naselje_id=1)
        oglas.save()
        log.msg("Item saved to database!", level=log.WARNING)

        return item
