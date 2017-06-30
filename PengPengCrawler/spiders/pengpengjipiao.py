# -*- coding: utf-8 -*-

from scrapy.spiders import Spider  
from scrapy.selector import Selector
from selenium import webdriver
from scrapy.http import Request
from datetime import date, timedelta
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PengPengJiPiaoSpider(Spider):  
    name = "PengPengJiPiao"  
    allowed_domains = ['b2c.csair.com']  
    pageIndex = 1
    url_format = "http://b2c.csair.com/B2C40/modules/bookingnew/inter/flightSelectDirect.html?lang=en&t=R&at=1&ct=0&it=0&egs=IBE&c1=KHN&c2=MEL&d1={start}&d2={end}"
    startDate = date(2017, 6, 1)
    endDate = date(2017, 8, 1)
    dayA = startDate
    dayB = dayA + timedelta(days=1)
    start_urls = [url_format.replace("{start}", dayA.strftime("%Y-%m-%d")).replace("{end}", dayB.strftime("%Y-%m-%d"))]
    driver = webdriver.Chrome()
    result = []
    
#    def __init__(self):
#        dayA = self.startDate
#        while dayA <= self.endDate - timedelta(days=1):
#            dayB = dayA + timedelta(days=1)
#            while dayB <= self.endDate:
#                self.start_urls.append(self.url_format.replace("{start}", dayA.strftime("%Y-%m-%d")).replace("{end}", dayB.strftime("%Y-%m-%d")))
#                dayB += timedelta(days=1)
#            dayA += timedelta(days=1)
#        print self.start_urls
        

    
    def parse(self, response): 
        #driver = webdriver.Chrome()
        self.driver.get(response.url)
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@class='fl-trip-expander' or @class='fl-error-box']")))
        try:
            selection_lines = self.driver.find_elements_by_class_name("fl-selection-line")
            print selection_lines
            for line in selection_lines:
                hoursA = int(line.find_elements_by_class_name("duration")[0].text.split("h")[0])
                hoursB = int(line.find_elements_by_class_name("duration")[0].text.split("h")[0])
                if hoursA > 25 or hoursB > 25:
                    continue
                else:
                    slices = line.find_elements_by_class_name("fl-slice")
                    goWay = slices[0].find_elements_by_tag_name("strong")[0].text+" - " + slices[0].find_elements_by_tag_name("strong")[1].text
                    returnWay = slices[1].find_elements_by_tag_name("strong")[0].text+" - " + slices[1].find_elements_by_tag_name("strong")[1].text
                    price = line.find_element_by_class_name("fl-final-price").find_element_by_tag_name("b").text
                    self.result.append([self.dayA.strftime("%Y-%m-%d")+"-"+self.dayB.strftime("%Y-%m-%d"), goWay, returnWay, price])
            print self.result
                
                
        except:
            self.driver.close()
        
        self.dayB += timedelta(days=1)
        if (self.dayB > self.endDate):
            self.dayA += timedelta(days=1)
            self.dayB = self.dayA + timedelta(days=1)
        yield Request(self.url_format.replace("{start}", self.dayA.strftime("%Y-%m-%d")).replace("{end}", self.dayB.strftime("%Y-%m-%d")), callback=self.parse, dont_filter = True)

        

        #self.driver.get('https://www.example.org/abc')