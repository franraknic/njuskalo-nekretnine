#!/usr/bin/env python
# -*- coding: utf-8 -*-
import scrapy
from scrapy import log
from scraper.items import BaseOglasItem


class BaseNekretnineSpider(scrapy.Spider):

    name = ''
    db_name = ''
    tip = ''
    allowed_domains = ['njuskalo.hr']
    url_base = ''
    start_urls = []

    def parse(self, response):

        zup = response.xpath(u'//div[@class = "list-topcats"]//li/a/@href').extract()

        for z in zup:
            yield scrapy.Request(self.url_base + z, callback=self.oglasi_links)

    def oglasi_links(self, response):

        links_oglasi = response.xpath(u'//ul[@class = "EntityList-items"]/li/article/h3/a/@href').extract()

        for link in links_oglasi:
            if link[:12] == u'/nekretnine/': #FIXME if u'/nekretnine/' in link:
                yield scrapy.Request(self.url_base + link, callback=self.parse_oglas)
            else:
                log.msg('Rejecting link: %s' % link, level=log.INFO)

        pagination = response.xpath(u'//a[text() = "Sljede\u0107a\xa0"]/@href').extract_first()
        if pagination:
            yield scrapy.Request(pagination, callback=self.oglasi_links)

    def parse_oglas(self, response):

        item = BaseOglasItem()
        do_isteka = response.xpath(u'//li[span[text() = "Do isteka je još:"]]/span').extract() # FIXME: broken xpath
        prikazan = response.xpath(u'//li[span[text() = "Oglas prikazan:"]]/span[@class = "value"]').extract() # FIXME: broken xpath

        item['link'] = response.url
        item['tip'] = self.db_name

        # table parsing
        item['cijena'] = response.xpath(u'//strong[@class = "price price--hrk"]/text()').extract_first()
        item['sifra'] = response.xpath(u'//li[span[text() = "Šifra oglasa:"]]/span/b/text()').extract()
        item['objavljen'] = response.xpath(u'//li[span[text() = "Objavljen:"]]/time/@datetime').extract_first()
        item['zupanija'] = response.xpath(u'//table/tbody/tr[th[text() = "Županija:"]]/td/text()').extract()
        item['grad'] = response.xpath(u'//table/tbody/tr[th[text() = "Grad/Općina:"]]/td/text()').extract()
        item['naselje'] = response.xpath(u'//table/tbody/tr[th[text() = "Naselje:"]]/td/text()').extract()
        item['m2'] = response.xpath(u'//table/tbody/tr[th[text() = "Stambena površina:"]]/td/text()').extract()
        # item['kat'] = response.xpath(u'//table/tbody/tr[th[text() = "Kat:"]]/td/text()').extract()

        return item

