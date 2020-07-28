from test import *


def main():
    url =  'https://www.gazzettaufficiale.it'
    req = UrlGetter(url)
    page = req.requester()
    req.makeHtml(page)



if __name__ == "__main__":
    main()