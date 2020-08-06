import logging
import requests

logging.basicConfig(level=logging.DEBUG)
from bs4 import BeautifulSoup



class UrlGetter:

    def __init__(self, strUrl):
        self.url = strUrl
        self.accessState = True

    def setAccessState(self, bool):  #must be boolean
        self.accessState = bool

    def getAccessState(self):   #return boolean
        return self.accessState

    def requester(self):
        try:
            r = requests.get(self.url, timeout=10)
            print(r.status_code)
            return r.content
        except:
            #notcomplete
            logging.debug("Request Denied")
            return "None"

    def getUrl(self, page):
        soup = BeautifulSoup(page, "lxml", from_encoding="unicode")
        concorsi = soup.select('a[href*=concorsi]')
        extractedUrl = concorsi[0].get('href')
        finalUrl = self.url + extractedUrl
        return finalUrl
