#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys
import GenerateTweet
import DatabaseInterface as db

#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'qWm5MtNsSM7UOGIlCmK0sKmM2'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'VyEsPIN1xeoHistBQx2y8QMPb3VDCJW2OomfFbWmaIHE3RvDb3'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '1231349857912336384-FrCB4rBV57EpPANORUDay9NMUrsHTx'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'uPTs4Az0M9SouXgf53UZml8tuFHiMGrUCifZ6iay34h0x'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

connection = db.get_connection()
cursor = connection.cursor()

headline = db.get_a_headline(cursor)
# make sure we got a headline
if len(headline) > 0:
    tweet = GenerateTweet.get_tweet(headline)
    api.update_status(status=tweet) 
    db.mark_headline_as_posted(cursor, headline)
    connection.commit()
cursor.close()
connection.close()