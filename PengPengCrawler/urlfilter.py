# -*- coding: utf-8 -*-

from scrapy.dupefilters import RFPDupeFilter

class urlfilter(RFPDupeFilter):
    """ 只根据url去重"""
    def __init__(self, path=None):
        self.urls_seen = set()
        RFPDupeFilter.__init__(self, path)
    def request_seen(self, request):
        if request.url in self.urls_seen:
            return True
        else:
            self.urls_seen.add(request.url)