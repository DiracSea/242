#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 21:47:54 2020

@author: Yue Lu
"""
# authorized info: https://developer.twitter.com/en/apps/17329293
import json
import twitter
import re
import time
import tweepy
import simplejson
from threading import Lock

# if __name__ == '__main__':
def crawler(query, max_tweets):
    
    # ckey = '37WJxuPqjpTNSnMLR7FlFX0MR'
    # csecret = 'apBwS0mFSlkbs1o5UrCdXxMsAH7TeRv4yemVcYvHGOv8gNyE4a'
    # atoken = '1188950150225416192-Qi9YmpOMh7deaH2BtsEHIlqRTjaCvJ'
    # asecret = 'LHMDQiFb4n2mtn2E3RB41IOMdybbw9NnwSPrM2hpQM0rY'
    ckey = 'x3REa2FkcAAhLDTP23tL0DQVU'
    csecret = '6afyavLJNLn9Iif3aJtktU8j1JysMGKJlRHMcVnz1M13EcS5jQ'
    atoken = '1219771892296380416-LTwo5hcbX44GNXiHH22SeRLyMfSej9'
    asecret = 'FbukzpzOhLMwOG8JzM6ETTANL9NOSkFN4locxE4s3kt3L'
    auth = tweepy.OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)  
    api = tweepy.API(auth, wait_on_rate_limit=True)
    
    #1
    #search_result = api.search(q="#LA", count=0, tweet_mode="extended", lang='en')
    #print(search_result)
    
    #2
    #trends=api.trends_place(1)
    #print(trends)
    #print(json.dumps(trends,indent=1))
    
    #3
    #search=tweepy.Cursor(api.search,q='#LA').items(20)  
    #query = '#beach'; 
    
    query = query+" -filter:retweets"
    # searched_tweets = [] 
    last_id = -1 
    itr = 0 
    num_tweets = 0
    while num_tweets < max_tweets: 
        count = max_tweets - num_tweets 
        
        try: 
            new_tweets = api.search(q = query, count=count, tweet_mode="extended", max_id=str(last_id-1))
            if not new_tweets: 
                break 

            num_tweets = num_tweets + len(new_tweets)
            last_id = new_tweets[-1].id 

            out_file = 'samples.json'
            f = open(out_file, 'a')
            itr += 1
            json_strings = [json.dumps(status._json) for status in new_tweets]

            json_parser(json_strings, f)

            print("end: " + str(itr))
        except tweepy.TweepError as e: 
            print("tweepy error")
            break
    


def json_parser(json_strings, f): 
    for tweet in json_strings:
        '''
        1.entities,user
        '''

        # store a tweet into the dictionary
        tweet_dict = simplejson.loads(tweet)
        hashtags=[]
        for hashtag in tweet_dict["entities"]["hashtags"]:
            #print(hashtag["text"])
            hashtags.append(hashtag["text"])
            
        new_dict={'id':tweet_dict["id"],
                'created_at':tweet_dict["created_at"],
                'text':tweet_dict["full_text"],
                'hashtags':hashtags,
                'user':tweet_dict["user"],
                'geo':tweet_dict["geo"]}
            
        print(json.dumps(new_dict), file = f)
        
        
            
            


     
    
