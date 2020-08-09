import logging
import requests
logging.basicConfig(level=logging.DEBUG)
from bs4 import BeautifulSoup



class UrlGetter:

    def __init__(self, pageUrl):
        self.url = pageUrl

    def requester(self):  #scarica la pagina
        try:
            r = requests.get(self.url, timeout=10)
            logging.debug("Status = " + str(r.status_code))
            return r.content
        except:
            #notcomplete
            logging.debug("Request Denied")
            return ""

    def getPage(self):
        page = self.requester()
        if page == "":
            logging.debug("Something went wrong")
            return
        return page

    def getUrl(self):  #parsa la pagina in html e ne estrae l'url richiesto con un css-selector
        page = self.getPage()
        soup = BeautifulSoup(page, "lxml", from_encoding="unicode")
        concorsi = soup.select('a[href*=concorsi]')
        extractedUrl = concorsi[0].get('href')
        finalUrl = self.url + extractedUrl
        return finalUrl
