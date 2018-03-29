import os

import telebot
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *

import generator.markov_model as markov_model

with open("token") as file:
    bot = telebot.TeleBot(file.readline()[:-1])

The_Donald_model = markov_model.load('The_Donald')
TwoXChromosomes_model = markov_model.load('TwoXChromosomes')

def respond(message: str):
    return The_Donald_model.make_sentence()

#commands=['start', 'help']
@bot.message_handler(func=lambda m: True)
def send_welcome(message):
    print('>' + message.text)
    response = respond(message)
    print(response)
    bot.reply_to(message, response)

print('Running!')
bot.polling()
