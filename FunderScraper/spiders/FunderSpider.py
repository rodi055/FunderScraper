import scrapy
from bs4 import BeautifulSoup
from scrapy.loader import ItemLoader
from selenium import webdriver

from FunderScraper.items import FundeItem

__author__ = 'Rawad Daher'


class FunderSpider(scrapy.Spider):
    name = "funder"

    @staticmethod
    def get_funds_links(page):
        links = set()
        for link in page.find_all('a'):
            url = link.get('href')
            if url:
                if 'fund.aspx?id=' in url:
                    links.add('http://www.funder.co.il/' + url)
        return links

    @staticmethod
    def get_string(label):
        return "//span[@id=\"ctl00_ContentPlaceHolder1_{}\"]//text()".format(label)

    def start_requests(self):
        browser = webdriver.PhantomJS()
        browser.get('http://www.funder.co.il/allInOne.aspx')
        page = BeautifulSoup(browser.page_source, 'html.parser')
        urls = FunderSpider.get_funds_links(page)
        browser.close()

        for url in urls:
            yield scrapy.Request(url=url, dont_filter=True, callback=self.parse)

    def parse(self, response):
        get_string = FunderSpider.get_string
        l = ItemLoader(item=FundeItem(), response=response)
        l.add_xpath('name', get_string('fundName'))
        l.add_xpath('num', get_string('fundNum'))
        l.add_xpath('daily', get_string('day1'))
        l.add_xpath('monthly', get_string('monthB'))
        l.add_xpath('yearly', get_string('yearB'))
        l.add_xpath('since_2016', get_string('LabelYear2016'))
        l.add_xpath('since_2015', get_string('LabelYear2015'))
        l.add_xpath('since_2014', get_string('LabelYear2014'))
        l.add_xpath('since_2013', get_string('LabelYear2013'))
        l.add_xpath('since_2012', get_string('LabelYear2012'))
        l.add_xpath('since_2011', get_string('LabelYear2011'))
        l.add_xpath('since_2010', get_string('LabelYear2010'))
        l.add_xpath('since_2009', get_string('LabelYear2009'))
        l.add_xpath('since_2008', get_string('LabelYear2008'))
        l.add_xpath('last_7_days', get_string('day7'))
        l.add_xpath('last_14_days', get_string('day14'))
        l.add_xpath('last_30_days', get_string('day30'))
        l.add_xpath('last_90_days', get_string('day90'))
        l.add_xpath('last_180_days', get_string('day180'))
        l.add_xpath('last_365_days', get_string('day365'))
        l.add_xpath('last_730_days', get_string('day730'))
        l.add_xpath('last_1095_days', get_string('day1095'))
        l.add_xpath('cost', get_string('Label4'))
        l.add_xpath('sharp', get_string('Label14'))
        l.add_xpath('exposure', get_string('Label6'))

        return l.load_item()
