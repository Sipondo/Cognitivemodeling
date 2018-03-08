import os
import telebot

bot = telebot.TeleBot("456213688:AAFoo1ONApk_f0xmd0QDME0itr60lI90fSs")

#commands=['start', 'help']
@bot.message_handler()
def send_welcome(message):
    bot.reply_to(message, u"Hello, welcome to this bot!")
    print(message)

bot.polling()
