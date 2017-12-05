# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

__author__ = 'Rawad Daher'


class FundeItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    num = scrapy.Field()
    daily = scrapy.Field()
    monthly = scrapy.Field()
    yearly = scrapy.Field()
    since_2016 = scrapy.Field()
    since_2015 = scrapy.Field()
    since_2014 = scrapy.Field()
    since_2013 = scrapy.Field()
    since_2012 = scrapy.Field()
    since_2011 = scrapy.Field()
    since_2010 = scrapy.Field()
    since_2009 = scrapy.Field()
    since_2008 = scrapy.Field()
    last_7_days = scrapy.Field()
    last_14_days = scrapy.Field()
    last_30_days = scrapy.Field()
    last_90_days = scrapy.Field()
    last_180_days = scrapy.Field()
    last_365_days = scrapy.Field()
    last_730_days = scrapy.Field()
    last_1095_days = scrapy.Field()
    cost = scrapy.Field()
    sharp = scrapy.Field()
    exposure = scrapy.Field()
