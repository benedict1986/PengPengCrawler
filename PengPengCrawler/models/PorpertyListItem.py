# -*- coding: utf-8 -*-

class PorpertyListItem():
    
    detailUrl = ""
    
    def __init__(self, section):
        self.detailUrl = section.xpath(".//a[@class='detailsButton']/@href").extract()
        self.detailUrl = "" if len(self.detailUrl) == 0 else self.detailUrl[0]
        
    def printPorpertyListItem(self):
        print "detailUrl: " + self.detailUrl