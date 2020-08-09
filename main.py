from urlgetter import *
import schedule
import time

TELEGRAM_TOKEN = 'PUT HERE YOUR TOKENID'
TELEGRAM_CHAT_ID = 'PUT HERE YOUR CHATID'

firstAccess = True
actual_number = 0

def urlUtil(url):
    pivot = url.rfind("=")
    num = url[pivot+1:len(url)]
    return int(num)


def main():
    urlGetter = UrlGetter('https://www.gazzettaufficiale.it')
    last_url = urlGetter.getUrl()
    last_number = urlUtil(last_url)

    global firstAccess
    global actual_number

    if firstAccess:
        '''send notification to user'''
        actual_number = last_number
        firstAccess = False
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        print(current_time)
        print(last_url)
        return
    else:
        if last_number is actual_number:
            print(last_url)
            return
        else:
            ''' send notification to user'''
            actual_number = last_number
            t = time.localtime()
            current_time = time.strftime("%H:%M:%S", t)
            print(current_time)
            print(last_url)
            return



def delayed_task():
    schedule.every(10).seconds.do(main)
    while True:
        schedule.run_pending()
        time.sleep(1)



if __name__ == "__main__":
    main() #I want to run it asap at launch
    delayed_task()
