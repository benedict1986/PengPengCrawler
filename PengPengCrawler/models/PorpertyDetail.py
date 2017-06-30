# -*- coding: utf-8 -*-

import hashlib

class PorpertyDetail():
    hashcode = ""
    url = ""
    images = ""
    propertyPrice = ""
    propertyStreetAddress = ""
    propertyAddressLocality = ""
    propertyAddressRegion = ""
    propertyPostalCode = ""
    propertyNumber = ""
    agencyName = ""
    agencyStreetAddress = ""
    agencyLocality = ""
    agencyRegion = ""
    agencyPostalCode = ""
    descriptionTitle = ""
    descriptionDetail = ""
    propertyType = ""
    bedroomNumber = ""
    bathroomNumber = ""
    garageSpaces = ""
    landSize = ""
    toiletNumber = ""
    openDayDate = ""
    openDayTime = ""
    
    def __init__(self, section, url):
        
        self.url = url
        
        imageThumbs = section.xpath(".//div[@class='thumbs']//div[contains(@class, 'thumb photo')]/img/@src")
        for thumb in imageThumbs:
            #thumbUrls = thumb.extract();
            thumbUrl = thumb.extract()
            self.images += thumbUrl.replace("150x112", "800x600")+";"
            
        self.propertyPrice = section.xpath(".//p[@class='priceText' or @class='contactAgent']/text()").extract()
        self.propertyPrice = "0" if len(self.propertyPrice) == 0 else self.propertyPrice[0]
        
        self.propertyStreetAddress = section.xpath(".//span[@itemprop='streetAddress']/text()").extract()
        self.propertyStreetAddress = "" if len(self.propertyStreetAddress) == 0 else self.propertyStreetAddress[0]
        
        self.propertyAddressLocality = section.xpath(".//span[@itemprop='addressLocality']/text()").extract()
        self.propertyAddressLocality = "" if len(self.propertyAddressLocality) == 0 else self.propertyAddressLocality[0]
        
        self.propertyAddressRegion = section.xpath(".//span[@itemprop='addressRegion']/text()").extract()
        self.propertyAddressRegion = "" if len(self.propertyAddressRegion) == 0 else self.propertyAddressRegion[0]
        
        self.propertyPostalCode = section.xpath(".//span[@itemprop='postalCode']/text()").extract()
        self.propertyPostalCode = "" if len(self.propertyPostalCode) == 0 else self.propertyPostalCode[0]
        
        self.propertyNumber = section.xpath(".//span[@class='property_id']/text()").extract()
        self.propertyNumber = "" if len(self.propertyNumber) == 0 else self.propertyNumber[0]
        
        self.agencyName = section.xpath(".//div[@class='agencyDetails']//p[@class='agencyName']/text()").extract()
        self.agencyName = "" if len(self.agencyName) == 0 else self.agencyName[0]
        
        self.agencyStreetAddress = section.xpath(".//div[@class='agencyDetails']//span[@class='street-address']/text()").extract()
        self.agencyStreetAddress = "" if len(self.agencyStreetAddress) == 0 else self.agencyStreetAddress[0]
        
        self.agencyLocality = section.xpath(".//div[@class='agencyDetails']//span[@class='locality']/text()").extract()
        self.agencyLocality = "" if len(self.agencyLocality) == 0 else self.agencyLocality[0]
        
        self.agencyRegion = section.xpath(".//div[@class='agencyDetails']//span[@class='region']/text()").extract()
        self.agencyRegion = "" if len(self.agencyRegion) == 0 else self.agencyRegion[0]
        
        self.agencyPostalCode = section.xpath(".//div[@class='agencyDetails']//span[@class='postal-code']/text()").extract()
        self.agencyPostalCode = "" if len(self.agencyPostalCode) == 0 else self.agencyPostalCode[0]
        
        self.descriptionTitle = section.xpath(".//div[@id='description']//p[@class='title']/text()").extract()
        self.descriptionTitle = "" if len(self.descriptionTitle) == 0 else self.descriptionTitle[0]
        
        self.descriptionDetail = section.xpath(".//div[@id='description']//p[@class='body']/text()").extract()
        self.descriptionDetail = "" if len(self.descriptionDetail) == 0 else self.descriptionDetail[0]
        
        self.propertyType = section.xpath(".//div[@class='featureList']//li[contains(text(), 'Property Type:')]/span/text()").extract()
        self.propertyType = "" if len(self.propertyType) == 0 else self.propertyType[0]
        
        self.bedroomNumber = section.xpath(".//div[@class='featureList']//li[contains(text(), 'Bedrooms:')]/span/text()").extract()
        self.bedroomNumber = "" if len(self.bedroomNumber) == 0 else self.bedroomNumber[0]
        
        self.bathroomNumber = section.xpath(".//div[@class='featureList']//li[contains(text(), 'Bathrooms:')]/span/text()").extract()
        self.bathroomNumber = "" if len(self.bathroomNumber) == 0 else self.bathroomNumber[0]
        
        self.garageSpaces = section.xpath(".//div[@class='featureList']//li[contains(text(), 'Garage Spaces:')]/span/text()").extract()
        self.garageSpaces = "" if len(self.garageSpaces) == 0 else self.garageSpaces[0]
        
        self.landSize = section.xpath(".//div[@class='featureList']//li[contains(text(), 'Land Size:')]/span/text()").extract()
        self.landSize = "" if len(self.landSize) == 0 else self.landSize[0]
        
        self.toiletNumber = section.xpath(".//div[@class='featureList']//li[contains(text(), 'Toilets:')]/span/text()").extract()
        self.toiletNumber = "" if len(self.toiletNumber) == 0 else self.toiletNumber[0]
        
        self.openDayDate = section.xpath(".//div[@id='description']//div[@class='inspectionTimesWrapper']//strong[@itemprop='name']/text()").extract()
        self.openDayDate = "" if len(self.openDayDate) == 0 else self.openDayDate[0]
        
        self.openDayTime = section.xpath(".//div[@id='description']//div[@class='inspectionTimesWrapper']//span[@class='time']/text()").extract()
        self.openDayTime = "" if len(self.openDayTime) == 0 else self.openDayTime[0]
        
        self.hashcode = str(hashlib.sha1(self.propertyStreetAddress + " " + self.propertyAddressLocality + " " + self.propertyAddressRegion + " " + self.propertyPostalCode).hexdigest())
        
    def printPorpertyDetail(self):
        print "url: " + self.url
        print "images: " + self.images
        print "propertyPrice: " + self.propertyPrice
        print "propertyStreetAddress: " + self.propertyStreetAddress
        print "propertyAddressLocality: " + self.propertyAddressLocality
        print "propertyAddressRegion: " + self.propertyAddressRegion
        print "propertyPostalCode: " + self.propertyPostalCode
        print "propertyNumber: " + self.propertyNumber
        print "agencyName: " + self.agencyName
        print "agencyStreetAddress: " + self.agencyStreetAddress
        print "agencyLocality: " + self.agencyLocality
        print "agencyRegion: " + self.agencyRegion
        print "agencyPostalCode: " + self.agencyPostalCode
        print "descriptionTitle: " + self.descriptionTitle
        print "descriptionDetail: " + self.descriptionDetail
        print "propertyType: " + self.propertyType
        print "bedroomNumber: " + self.bedroomNumber
        print "bathroomNumber: " + self.bathroomNumber
        print "garageSpaces: " + self.garageSpaces
        print "landSize: " + self.landSize.encode("GB18030")
        print "toiletNumber: " + self.toiletNumber
        print "openDayDate: " + self.openDayDate
        print "openDayTime: " + self.openDayTime
        print "hashcode: " + self.hashcode