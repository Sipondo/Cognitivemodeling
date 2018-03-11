#!/usr/bin/env python

from gensim.models import Word2Vec
from gensim.models.keyedvectors import KeyedVectors

#l.ansteeg@donders.ru.nl

# Load Google's pre-trained Word2Vec model
model = KeyedVectors.load_word2vec_format('./GoogleNews-vectors-negative300.bin', binary=True)
# has plural and upper/lower case, and even bigrams (e.g., taxpayer_dollars; vast_sums)

# flex word2vec's muscles
model.doesnt_match("man woman child kitchen".split())
model.doesnt_match("france england germany berlin".split())
model.doesnt_match("paris berlin london austria".split())
model.most_similar("dolphin")

# Consider a two-person task with a signaler and a receiver (similar to the TV gameshow 'Password'):
# The signalers were told that they would be playing a word-guessing game in which
# they would have to think of one-word signals that would help someone guess their items.
# They were talked through an example: if the item was 'dog', then a good signal would be
# 'puppy' since most people given 'puppy' would probably guess 'dog'.

# sender thinks bank, says money
# receiver think cash
model.most_similar("bank") # .69 robber, .67 robbery, robbers, security, agency ..
model.most_similar("money") # .55 dollars, .55 profit, .54 cash
model.most_similar("cash") # .69 capitalize, .54 money, sell, debt, tax


model['money']

model.similarity("hot","cold") # .20
model.similarity("hot","warm") # .14

def receive_word(hint): #receive word, also used by send word!
    return_list = []
    for (option, odds) in model.most_similar_cosmul(positive=[hint], topn=100): #check 100 words
        if (not hint.lower() in option.lower())\
         and (not option.lower() in hint.lower())\
         and (not "_" in option.lower()): #these filter some words that found unsatisfactory
            return_list.append(option)
    if(len(return_list)>0):
        return_list.sort(key = lambda x:len(x)) #this returns the shortest word i/o first hit
        return return_list[0]
    return "NaN"
    #return model.most_similar(positive=[hint],negative=["object"])[0]

def send_word(secret): #receive word, also used by send word!
    for (option, odds) in model.most_similar_cosmul(positive=[secret], topn=100): #check 100 words
        if (not option.lower() in secret.lower()): #these filter some words that found unsatisfactory
            if (not "_" in option):
                if (receive_word(option) == secret):# and not (secret in option[0]):
                    return option
    return_list = []
    for (option, odds)in model.most_similar_cosmul(positive=[secret], topn=50):
        if (not secret in option) and (not option in secret):
            return_list.append(option)
    if(len(return_list)>0):
        return_list.sort(key = lambda x:len(x)) #this returns the shortest word i/o first hit
        return return_list[0]
    return "NaN"

test_set = ["cut", "ice", "stamp", "self", "snail", "now", "bed", "night",\
            "needle", "scratch", "bank", "joke", "king", "salt", "good",\
            "washer", "east", "nail", "bulb", "lost"]

hint_set = []
for word in test_set:
    hint = send_word(word)
    print word + ": " + hint
    hint_set.append(hint)

for i in range(len(hint_set)):
    word = test_set[i]
    hint = hint_set[i]
    print word + ": " + hint + " -> " + receive_word(hint)
