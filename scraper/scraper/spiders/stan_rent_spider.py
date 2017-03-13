#!/usr/bin/env python
# -*- coding: utf-8 -*-
import scrapy
from scrapy import log


class RentStanSpider(scrapy.Spider):

    name = 'spider_rent_stan'
    allowed_domains = ['njuskalo.hr']
    start_urls = ['http://www.njuskalo.hr/iznajmljivanje-stanova']
    url_base = 'http://www.njuskalo.hr'

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

    def parse_oglas(self, response):
        pass
