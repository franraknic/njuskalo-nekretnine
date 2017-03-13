#!/usr/bin/env python
# -*- coding: utf-8 -*-
import scrapy
from scrapy import log


class RentStanSpider(scrapy.Spider):

    name = 'spider_rent_stan'
    allowed_domains = ['njuskalo.hr']
    start_urls = ['http://www.njuskalo.hr/iznajmljivanje-stanova']
    url_base = 'http://www.njuskalo.hr'