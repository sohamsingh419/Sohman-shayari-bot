import os
import random
from telegram.ext import Updater, CommandHandler

# Environment variables से Token और Chat ID लेंगे
TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

shayari_list = [
    "तेरा नाम लूं ज़ुबान से, यही बात रास नहीं आती...",
    "कभी कभी खामोश रहना ही बेहतर होता है..."
]

joke_list = [
    "डॉक्टर: नींद क्यों नहीं आती? मरीज: फेसबुक वाला मोबाइल नहीं देता!",
    "पप्पू: मैं तुझसे बहुत प्यार करता हूँ। गप्पू: पर मैं लड़का हूँ!"
]

def send_random_shayari(context):
    context.bot.send_message(chat_id=CHAT_ID, text=random.choice(shayari_list))

def send_random_joke(context):
    context.bot.send_message(chat_id=CHAT_ID, text=random.choice(joke_list))

def start(update, context):
    update.message.reply_text("Bot चालू हो गया! अब यह शायरी और जोक्स भेजेगा।")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    job_queue = updater.job_queue
    job_queue.run_repeating(send_random_shayari, interval=3600, first=10)
    job_queue.run_repeating(send_random_joke, interval=5400, first=20)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
