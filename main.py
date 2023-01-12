import os

print("Hello world from ...")
os.system("python --version")

import tweepy
import tweepy 

#get Tweepy Authentication 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#get the API 
api = tweepy.API(auth)

#make a tweet
api.update_status('Hello, world!')

#get recent tweets 
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

#search tweets
searched_tweets = api.search(q="Python")

for tweet in searched_tweets:
    print(tweet.text)