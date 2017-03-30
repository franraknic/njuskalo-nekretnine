# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
# TODO: Add pipeline for data conversion, from string to numeric etc.


import re
import sqlite3
from scrapy import log


class ScraperPipeline(object):

    def process_item(self, item, spider):
        return item


class SQLPersist(object):

    def __init__(self):

        self.db_path = 'D:\\njuskalobaza.db'
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS `oglasi` ( `id` INTEGER PRIMARY KEY AUTOINCREMENT, `cijena` TEXT, `link` TEXT, `objavljen` TEXT, `scraped` TEXT, `tip` TEXT, `zupanija` TEXT, `grad` TEXT, `naselje` TEXT, `m2` TEXT ); ")

    def process_item(self, item, spider):

        self.cursor.execute('SELECT count(oglasi.link) FROM oglasi WHERE oglasi.link=?', (item['link'],))
        result = self.cursor.fetchone()

        if result[0] != 0:
            log.msg('Item %s in database!' % item['link'], level=log.WARNING)
        else:
            oglas = [(None, item['cijena'], item['link'], item['scraped'], item['objavljen'], item['tip'], item['zupanija'], item['grad'], item['naselje'], item['m2'])]
            self.cursor.executemany('INSERT INTO oglasi VALUES (?,?,?,?,?,?,?,?,?,?)', oglas)
            self.connection.commit()

        return item
