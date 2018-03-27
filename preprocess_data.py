#import unicodecsv as csv
import csv

author_dict = {}

with open("pol_accounts.csv", encoding="utf-8") as file:
    reader = csv.DictReader(file, delimiter=";")
    for row in reader:
        author_dict[int(row["id"])] = ([row["screen_name"], row["description"]])

bobby = author_dict[785624983145852928]

def get_search_string(representative):
    return representative[0] + " " + representative[1]

get_search_string(bobby)

from wikidata.client import Client
import wikipedia

client = Client()

wikipedia.search("repbobbyscott")

entity = client.get('repbobbyscott')

entity.description


    # Sleutel 1: 93a63c2d291f4148a548bd4741b4d833
    #
    # Sleutel 2: 3894e4f9af4b483aa730dc34c42f6610
####For Web Results:


from py_ms_cognitive import PyMsCognitiveWebSearch
search_term = "Python Software Foundation"
search_service = PyMsCognitiveWebSearch('93a63c2d291f4148a548bd4741b4d833', search_term)

first_fifty_result = search_service.search(limit=50, format='json') #1-50
# >>> second_fifty_resul t= search_service.search(limit=50, format='json') #51-100
#
# >>> print (second_fifty_result[0].snippet)
#     u'Python Software Foundation Home Page. The mission of the Python Software Foundation is to promote, protect, and advance the Python programming language, and to ...'
# >>> print (first_fifty_result[0].__dict__.keys()) #see what variables are available.
# ['name', 'display_url', 'url', 'title', 'snippet', 'json', 'id', 'description']
#
#     # To get individual result json:
# >>> print (second_fifty_result[0].json)
# ...
#
#     # To get the whole response json from the MOST RECENT response
#     # (which will hold 50 individual responses depending on limit set):
# >>> print (search_service.most_recent_json)

# id;"screen_name";"description";
# "created_at";"location";"is_verified";
# "latest_following_count";"latest_followers_count";
# "latest_status_count";"array_agg"
# None
