#!/usr/bin/env python
# -*- coding: utf-8 -*-
from base_spider import BaseNekretnineSpider

class IznajmljivanjeSpider(BaseNekretnineSpider):

    name = 'rent_stan'
    tip = '/iznajmljivanje-stanova'
    allowed_domains = ['njuskalo.hr']
    url_base = 'http://www.njuskalo.hr'
    start_urls = [url_base + tip]

    def parse_oglas(self, response):
        # TODO: Add pipeline for data conversion, from string to numeric etc.

        sifra = response.xpath(u'//li[span[text() = "Šifra oglasa:"]]/span/b/text()').extract()
        objavljen = response.xpath(u'//li[span[text() = "Objavljen:"]]/time/@datetime').extract_first()
        do_isteka = response.xpath(u'//li[span[text() = "Do isteka je još:"]]/span').extract() # FIXME: broken xpath
        prikazan = response.xpath(u'//li[span[text() = "Oglas prikazan:"]]/span[@class = "value"]').extract() # FIXME: broken xpath
        cijena = response.xpath(u'//strong[@class = "price price--hrk"]/text()').extract_first()

        # table parsing
        zupanija = response.xpath(u'//table/tbody/tr[th[text() = "Županija:"]]/td/text()').extract()
        grad = response.xpath(u'//table/tbody/tr[th[text() = "Grad/Općina:"]]/td/text()').extract()
        naselje = response.xpath(u'//table/tbody/tr[th[text() = "Naselje:"]]/td/text()').extract()
        stan_m2 = response.xpath(u'//table/tbody/tr[th[text() = "Stambena površina:"]]/td/text()').extract()
        kat = response.xpath(u'//table/tbody/tr[th[text() = "Kat:"]]/td/text()').extract()




