#import unicodecsv as csv
import csv
import wikipedia
import pprint
import urllib
import urllib.request
import time
from tqdm import tqdm

binding_list = {}
with open("pol_bindings.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        democrat = int(row["democrat"])
        republican = int(row["republican"])
        binding_list[int(row["id"])] = 2 if democrat>republican else 1 if democrat<republican else 0

not_suited = [(binding_list[key], key) for key in binding_list if binding_list[key] == 0]
suited = list = [(binding_list[key], key) for key in binding_list if binding_list[key] > 0]

len(not_suited)
len(suited)

suited_list = {key: binding_list[key] for key in binding_list if binding_list[key] > 0}

tweets = []
with open("pol_tweets.csv", encoding="utf-8") as file:
    reader = csv.DictReader(file, delimiter=";")
    for row in tqdm(reader):
        tweets.append([row["user_id"], row["tweet_text"]])

label = {1: "Republican", 2:"Democrat"}


def return_tweet(tweet):
    return str(label[suited_list[int(test_tweet[0])]]) + ": " + str(test_tweet[1])

test_tweet = tweets[500000]
print(return_tweet(test_tweet))

democounter = 0
repcounter = 0
for tweet in tweets:
    suited_list[int(test_tweet[0])]
