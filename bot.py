import os
import telebot
#from textblob import TextBlob
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from nltk.corpus import stopwords
import numpy as np
import numpy.linalg as LA
from nltk.classify import NaiveBayesClassifier
from nltk.tokenize import word_tokenize

train_set = #input here

categories = ['left', 'right', 'neutral']
stopWords = stopwords.words('english')
vectorizer = CountVectorizer(stop_words = stopWords)
transformer = TfidfTransformer()

all_words = set(word.lower() for passage in train for word in word_tokenize(passage[0]))
t = [({word: (word in word_tokenize(x[0])) for word in all_words}, x[1]) for x in train]

classifier = NaiveBayesClassifier.train(t)




with open("token") as file:
    bot = telebot.TeleBot(file.readline()[:-1])


#commands=['start', 'help']
@bot.message_handler(func=lambda m: True)
def send_welcome(message):
    test_sent_features = {word.lower(): (word in word_tokenize(test_sentence.lower())) for word in all_words}
    bot.reply_to(message, u"Sentiment score: " + str(classifier.classify(test_sent_features)))

bot.polling()
