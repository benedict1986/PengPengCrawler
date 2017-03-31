# -*- coding: utf-8 -*-

from scrapy.spider import Spider  
from scrapy.selector import Selector 
from scrapy.http import Request
import re 

class PengPengSpider(Spider):  
    name = "PengPeng"  
    allowed_domains = ['www.dentist-chatswood.com.au']  
    start_urls = [  
        "http://www.dentist-chatswood.com.au/index.php" 
    ]  

    def parse(self, response): 
        sel = Selector(response)
        urls = sel.xpath('//ul[@id="sm-menu"]//a/@href').extract()
        for url in urls:  
            url = "http://www.dentist-chatswood.com.au" + re.sub("^[.|..]", "", url)
            yield Request(url, callback=self.parse, dont_filter = True) 
            