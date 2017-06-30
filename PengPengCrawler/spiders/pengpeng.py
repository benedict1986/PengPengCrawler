# -*- coding: utf-8 -*-

from scrapy.spiders import Spider  
from scrapy.selector import Selector 
from scrapy.http import Request
from ..models import PorpertyListItem
from ..models import PorpertyDetail
import MySQLdb as mdb

class PengPengSpider(Spider):  
    name = "PengPeng"  
    allowed_domains = ['www.realestate.com.au']  
    pageIndex = 1
    start_urls = ["http://www.realestate.com.au/buy/property-house-with-3-bedrooms-between-500000-550000-in-berwick/list-1?maxBeds=3&source=location-search"]
    conn = mdb.connect(host='127.0.0.1', port=3306, user='admin', passwd='admin', db='pengpeng', charset='utf8')

    def parse(self, response): 
        sel = Selector(response)
        sections = sel.xpath("//article[contains(@class, 'resultBody')]")
        #print len(sections)
        for section in sections:
            p = PorpertyListItem.PorpertyListItem(section)
            #print "============>"+p.detailUrl
            yield Request("http://"+self.allowed_domains[0]+p.detailUrl, callback=self.parseDetail, dont_filter = True)
        nextLink = sel.xpath("//li[@class='nextLink'][1]/a/@href").extract()
        #print nextLink
        if len(nextLink) != 0:
            yield Request("http://"+self.allowed_domains[0]+nextLink[0], callback=self.parse, dont_filter = True)

        
    def parseDetail(self, response):
        sel = Selector(response)
        p = PorpertyDetail.PorpertyDetail(sel, response.url)
        #p.printPorpertyDetail()
        self.pageIndex += 1
        self.insertTable(p)
        #print("====================================>"+str(self.pageIndex) + " " + str(p.hashcode))
        
    def insertTable(self, p):
        sqlString = r"INSERT INTO `Properties` (`id`, `hashcode`, `url`, `images`, `propertyPrice`, `propertyStreetAddress`, `propertyAddressLocality`, `propertyAddressRegion`, `propertyPostalCode`, `propertyNumber`, `agencyName`, `agencyStreetAddress`, `agencyLocality`, `agencyRegion`, `agencyPostalCode`, `descriptionTitle`, `descriptionDetail`, `propertyType`, `bedroomNumber`, `bathroomNumber`, `garageSpaces`, `landSize`, `toiletNumber`, `openDayDate`, `openDayTime`) VALUES (NULL, '{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}', '{10}', '{11}', '{12}', '{13}', '{14}', '{15}', '{16}', '{17}', '{18}', '{19}', '{20}', '{21}', '{22}', '{23}');"
        sqlString = sqlString.format(mdb.escape_string(p.hashcode.encode('ascii', 'ignore')), mdb.escape_string(p.url.encode('ascii', 'ignore')), mdb.escape_string(p.images.encode('ascii', 'ignore')), mdb.escape_string(p.propertyPrice.encode('ascii', 'ignore')), mdb.escape_string(p.propertyStreetAddress.encode('ascii', 'ignore')), mdb.escape_string(p.propertyAddressLocality.encode('ascii', 'ignore')), mdb.escape_string(p.propertyAddressRegion.encode('ascii', 'ignore')), mdb.escape_string(p.propertyPostalCode.encode('ascii', 'ignore')), mdb.escape_string(p.propertyNumber.encode('ascii', 'ignore')), mdb.escape_string(p.agencyName.encode('ascii', 'ignore')), mdb.escape_string(p.agencyStreetAddress.encode('ascii', 'ignore')), mdb.escape_string(p.agencyLocality.encode('ascii', 'ignore')), mdb.escape_string(p.agencyRegion.encode('ascii', 'ignore')), mdb.escape_string(p.agencyPostalCode.encode('ascii', 'ignore')), mdb.escape_string(p.descriptionTitle.encode('ascii', 'ignore')), mdb.escape_string(p.descriptionDetail.encode('ascii', 'ignore')), mdb.escape_string(p.propertyType.encode('ascii', 'ignore')), mdb.escape_string(p.bedroomNumber.encode('ascii', 'ignore')), mdb.escape_string(p.bathroomNumber.encode('ascii', 'ignore')), mdb.escape_string(p.garageSpaces.encode('ascii', 'ignore')), mdb.escape_string(p.landSize.encode('ascii', 'ignore')), mdb.escape_string(p.toiletNumber.encode('ascii', 'ignore')), mdb.escape_string(p.openDayDate.encode('ascii', 'ignore')), mdb.escape_string(p.openDayTime.encode('ascii', 'ignore')))
        print sqlString
        try:
            cursor = self.conn.cursor()
            cursor.execute(sqlString)
        except:
            import traceback
            traceback.print_exc()
        finally:
            cursor.close()