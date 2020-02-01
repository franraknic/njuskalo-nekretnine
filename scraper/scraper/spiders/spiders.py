#!/usr/bin/env python
# -*- coding: utf-8 -*-
from base_spider import BaseNekretnineSpider


class IznajmljivanjeStan(BaseNekretnineSpider):

    name = 'rent_stan'
    tip = '/iznajmljivanje-stanova'
    db_name = 'stan_rent'
    url_base = 'http://www.njuskalo.hr'
    start_urls = [url_base + tip]


class ProdajaStan(BaseNekretnineSpider):

    name = 'prodaja_stan'
    tip = '/prodaja-stanova'
    db_name = 'stan_prodaja'
    url_base = 'http://www.njuskalo.hr'
    start_urls = [url_base + tip]


class ProdajaKuca(BaseNekretnineSpider):

    name = 'prodaja_kuca'
    tip = '/prodaja-kuca'
    db_name = 'kuca_prodaja'
    url_base = 'http://www.njuskalo.hr'
    start_urls = [url_base + tip]


class IznajmljivanjeKuca(BaseNekretnineSpider):

    name = 'rent_kuca'
    tip = '/iznajmljivanje-kuca'
    db_name = 'kuca_rent'
    url_base = 'http://www.njuskalo.hr'
    start_urls = [url_base + tip]
