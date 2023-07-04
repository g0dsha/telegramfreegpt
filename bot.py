from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests

def start(update: Update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Я бот для работы с OpenAI.")

def message_handler(update: Update, context):
    message_text = update.message.text

    response = requests.post(YOUR_ENDPOINT_URL, json={"message": message_text})
    answer = response.json()["answer"]
    
    context.bot.send_message(chat_id=update.effective_chat.id, text=answer)

def main():
    updater = Updater(token='YOUR_BOT_TOKEN', use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    message_handler = MessageHandler(Filters.text & ~Filters.command, message_handler)
    dispatcher.add_handler(message_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
