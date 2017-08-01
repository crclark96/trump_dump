import json
import sys
import tweepy
import vocabulary

with open('api_keys.json', 'r') as f:
    credentials = json.load(f)

auth = tweepy.OAuthHandler(credentials['consumer_key'], 
                           credentials['consumer_secret'])
auth.set_access_token(credentials['access_token'], 
                      credentials['access_token_secret'])

api = tweepy.API(auth)

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        if status._json['user']['screen_name'] == 'realdonaldtrump':
            print status
            vocabulary.updateVocabulary(status.text.encode('UTF-8').split(' '))

if __name__ == '__main__':
    myStream = tweepy.Stream(auth=api.auth, listener=MyStreamListener())

    myStream.filter(follow=['25073877'])
