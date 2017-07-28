import json
import tweepy

with open('api_keys.json', 'r') as f:
    credentials = json.load(f)

auth = tweepy.OAuthHandler(credentials['consumer_key'], 
                           credentials['consumer_secret'])
auth.set_access_token(credentials['access_token'], 
                      credentials['access_token_secret'])

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text
