#!/bin/python
#usarmyjoe
#This is the tweety script
#It is meant to like tweets based upon hashtags/keywords.
#It is not meant to be a "bot"
#This script requires several libraries:
#1. tweepy
#2. setuptools
#3. urllib2
#4. json
#It will not run without these libraries
#It also needs the Auth.py file, which contains the creds.
#
#Hence:
import tweepy, time
from Auth import *
#Get the creds ready for use:
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)
#
#
#
#
#** Configs - Configs - Configs *************************************************
#Wait time between tweets in seconds
TWEET_WAIT_TIME = 60
#Wait time between runs in seconds
RUN_WAIT_TIME = 600
#List of Stuff to Find & Favorite
KEYWORDS = 'hacking'
#favorites per run
LIKES = 1
#Date to start from. use 'today' for tweets starting after today
DATE = 'today'
#
#
#
#
#**Code Stuffs**
#Get stuff 'From list'
def findtweets(api):
    #Array for holding tweets found
    found = []
    for tweet in tweepy.Cursor(api.search, q=KEYWORDS, lang='en', since="2018-01-01").items(LIKES):
        #print(tweet.id,tweet.created_at)
        #add 'ID' to array
        found.append(tweet.id)
    return found

#Like Stuff 'Favorite in Twitter Vern'
def favoriteit(api,tweets):
    try:
        #print(tweets)
        #Go through the array and get individual tweet IDs
        for tweet in tweets:
            status = api.create_favorite(id=tweet)
            if len(tweets) > 1:
                time.sleep(TWEET_WAIT_TIME)
            #print(status)
    #Error handling
    except tweepy.TweepError:
        return (False, tweets)
    return (True, tweets)

#Do Stuff
while True:
    #Array for the found tweets
    fav=[]
    #Add found tweets to the array
    fav=findtweets(api)
    #like the found tweets by ID
    response = favoriteit(api,fav)
    #print the result
    if response[0]:
        print('Liked: ', response[1])
    else:
        print('Failed (likely due to a "duplicate fav"): ',response)
    print('Waiting ',RUN_WAIT_TIME,' seconds for new run...')
    time.sleep(RUN_WAIT_TIME)
#fin