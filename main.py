import sys

from test import *
import schedule
import time

def main():
    url = 'https://www.gazzettaufficiale.it'
    req = UrlGetter(url)
    page = req.requester()
    if page is "None":
        logging.debug("Something went wrong")
        return
    concorsi_url = req.getUrl(page)
    actualUrl = ""
    if req.getAccessState():
        actualUrl = concorsi_url
        req.setAccessState(True)
        '''SEND NOTIFICATION TO USER'''
    else:
        verify(actualUrl, concorsi_url)

    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print(current_time)
    print(concorsi_url)


def delayed_task():
    schedule.every(60).seconds.do(main)
    while True:
        schedule.run_pending()
        time.sleep(1)



if __name__ == "__main__":
    main()   #I want it to run asap for the first time
    delayed_task()
