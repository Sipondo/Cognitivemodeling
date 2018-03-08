import os
import telebot

with open("token") as file:
    bot = telebot.TeleBot(file.readline()[:-1])


#commands=['start', 'help']
@bot.message_handler(func=lambda m: True)
def send_welcome(message):
    bot.reply_to(message, u"Hello, welcome to this bot!")
    print(message)

bot.polling()
