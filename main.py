from urlgetter import *
import logging
from messages import start_message
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
import schedule
import time
from telegram.ext import Updater, InlineQueryHandler, CommandHandler

firstAccess = True
actual_number = 0


def main():
    updater = Updater('TOKEN ID HERE', use_context=True)
    disp = updater.dispatcher

    disp.add_handler(CommandHandler("start", start))
    disp.add_handler(CommandHandler("On", initialize))

    updater.start_polling()
    updater.idle()


def initialize(update, context):
    delayed_task(update, context)


def start(update, context):
    update.message.reply_text(start_message)


def search(update, context):
    urlGetter = UrlGetter('https://www.gazzettaufficiale.it')
    last_url = urlGetter.getUrl()
    last_number = urlUtil(last_url)

    global firstAccess
    global actual_number

    if firstAccess:
        actual_number = last_number
        firstAccess = False
        update.message.reply_text("Ecco il link per i concorsi disponibili al momento:")
        update.message.reply_text(last_url)
        update.message.reply_text("Ora rimango a lavoro e ti manderò un messaggio non appena la pagina verrà aggiornata!")
        return
    else:
        if last_number is actual_number:
            return
        else:
            actual_number = last_number
            update.message.reply_text("Ciao! Ho appena trovato degli aggiornamenti! Ecco il link:")
            update.message.reply_text(last_url)
            return


def urlUtil(url):
    pivot = url.rfind("=")
    num = url[pivot + 1:len(url)]
    return int(num)


def delayed_task(update, context):
    schedule.every(60).seconds.do(lambda: search(update, context))
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
