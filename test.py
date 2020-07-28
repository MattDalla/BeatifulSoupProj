import logging
import requests
logging.basicConfig(level=logging.DEBUG)
from bs4 import BeautifulSoup
import re

class UrlGetter:

    def __init__(self, strUrl):
        self.url = strUrl

    def requester(self):
        try:
            r = requests.get(self.url, timeout=10)
            print(r.status_code)
            return r.content
        except:
            logging.debug("Request Denied")
            return "None"

    def makeHtml(self, page):
        soup = BeautifulSoup(page,"lxml", from_encoding="unicode")
        concorsi = soup.select('a[href*=concorsi]')
        extractedUrl = concorsi[0].get('href')
        finalUrl = self.url + extractedUrl
        print(finalUrl)

