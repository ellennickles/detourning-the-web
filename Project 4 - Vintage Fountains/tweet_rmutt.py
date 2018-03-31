import json
import os
import tweepy
from tweepy.auth import OAuthHandler
from get_fountain import savedname

with open('creds.json', 'r') as infile:
    creds = json.load(infile)

auth = tweepy.OAuthHandler(creds['consumer_key'], creds['consumer_secret'])
auth.set_access_token(creds['access_key'], creds['access_secret'])

api = tweepy.API(auth)

# do a test, search for keywords
# results = api.search('duchamp')
# for r in results:
#     print r.text

# do another test, post a status update
# api.update_status("just can't get enough of these fountains")

# post an image file
# api.update_with_media(savedname)
api.update_with_media(savedname, "#fountain #arthistory")

os.remove(savedname)
