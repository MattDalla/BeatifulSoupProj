from test import *


def main():
    url = 'https://www.gazzettaufficiale.it'
    req = UrlGetter(url)
    page = req.requester()
    if page is "None":
        logging.debug("Something went wrong")
        return
    concorsi_url = req.getUrl(page)
    while True:
        '''/ToDo'''
        return


if __name__ == "__main__":
    main()
