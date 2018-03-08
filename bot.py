import os
import telebot

bot = telebot.TeleBot("456213688:AAFoo1ONApk_f0xmd0QDME0itr60lI90fSs")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, u"Hello, welcome to this bot!")

bot.polling()
