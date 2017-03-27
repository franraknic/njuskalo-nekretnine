#!/usr/bin/env python
# -*- coding: utf-8 -*-
from base_spider import BaseNekretnineSpider
from scraper.items import IznmStanItem


class IznajmljivanjeStan(BaseNekretnineSpider):

    name = 'rent_stan'
    tip = '/iznajmljivanje-stanova'
    url_base = 'http://www.njuskalo.hr'
    start_urls = [url_base + tip]


class ProdajaStan(BaseNekretnineSpider):

    name = 'prodaja_stan'
    tip = '/prodaja-stanova'
    url_base = 'http://www.njuskalo.hr'
    start_urls = [url_base + tip]