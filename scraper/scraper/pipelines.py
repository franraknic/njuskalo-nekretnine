# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
# TODO: Add method for checking duplicates in database
# TODO: Add method for checking if Oglas is still active (not sold or expired), Oglas.link can be used for this



from scrapy import log
from OglasModel import Oglas, Grad, Naselje, Zupanija
import datetime


class ScraperPipeline(object):

    def process_item(self, item, spider):
        return item


class NormalizeData(object):
    """Convert scraped strings to integers or the required format before persisting to DB"""

    def process_item(self, item, spider):
        item['cijena'] = item['cijena'].strip().replace('.','')
        item['cijena'] = int(item['cijena'])

        item['m2'] = item['m2'].replace(',','.')
        item['m2'] = float(item['m2'])
        return item


class ORMPersist(object):
    """Persists scraped data to an SQLite databse, run setup_databse.py or DatabaseObject.create(Model) from console"""

    def persist_oglas(self, item):

        new_zup, c1 = Zupanija.get_or_create(ime=item['zupanija'])
        new_grad, c2 = Grad.get_or_create(ime=item['grad'], zup_id=new_zup.id)
        new_nas, c3 = Naselje.get_or_create(ime=item['naselje'], grad_id=new_grad.id)

        ogl, saved = Oglas.get_or_create(link=item['link'], defaults={ 'cijena':item['cijena'], 'm2':item['m2'], 'tip':item['tip'], 'scraped':item['scraped'],
                      'zup':new_zup.id, 'grad':new_grad.id, 'naselje':new_nas.id, 'last_active': item['scraped']})

        if not saved:
            q = Oglas.update(active=True, last_active=datetime.datetime.now()).where(Oglas.link == item['link'])
            q.execute()
            log.msg('Exists in database - set as active : %s' % ogl.link, level=log.INFO)

    def process_item(self, item, spider):

        self.persist_oglas(item)

        return item
