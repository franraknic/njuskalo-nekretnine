#!/usr/bin/env python
# -*- coding: utf-8 -*-
import scrapy
from scrapy import log


class BaseNekretnineSpider(scrapy.Spider):

    name = ''
    tip = ''
    allowed_domains = ['']
    url_base = ''
    start_urls = []

    def parse(self, response):

        zup = response.xpath(u'//div[@class = "list-topcats"]//li/a/@href').extract()

        for z in zup:
            yield scrapy.Request(self.url_base + z, callback=self.oglasi_links)

    def oglasi_links(self, response):

        links_oglasi = response.xpath(u'//ul[@class = "EntityList-items"]/li/article/h3/a/@href').extract()

        for link in links_oglasi:
            if link[:12] == u'/nekretnine/':
                yield scrapy.Request(self.url_base + link, callback=self.parse_oglas)
            else:
                log.msg('Rejecting link: %s' % link, level=log.INFO)

        pagination = response.xpath(u'//a[text() = "Sljede\u0107a\xa0"]/@href').extract_first()
        if pagination:
            yield scrapy.Request(pagination, callback=self.oglasi_links)

    def parse_oglas(self, response):
        pass
