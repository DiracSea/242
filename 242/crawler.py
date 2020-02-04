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
import tweepy
import simplejson
from threading import Lock

# if __name__ == '__main__':
def crawler(query, max_tweets):
    
    ckey = '37WJxuPqjpTNSnMLR7FlFX0MR'
    csecret = 'apBwS0mFSlkbs1o5UrCdXxMsAH7TeRv4yemVcYvHGOv8gNyE4a'
    atoken = '1188950150225416192-Qi9YmpOMh7deaH2BtsEHIlqRTjaCvJ'
    asecret = 'LHMDQiFb4n2mtn2E3RB41IOMdybbw9NnwSPrM2hpQM0rY'
    # ckey = 'x3REa2FkcAAhLDTP23tL0DQVU'
    # csecret = '6afyavLJNLn9Iif3aJtktU8j1JysMGKJlRHMcVnz1M13EcS5jQ'
    # atoken = '1219771892296380416-LTwo5hcbX44GNXiHH22SeRLyMfSej9'
    # asecret = 'FbukzpzOhLMwOG8JzM6ETTANL9NOSkFN4locxE4s3kt3L'
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
    
    searched_tweets = [status._json for status in tweepy.Cursor(api.search,  q=query).items(max_tweets)]
          
    """
    q: query text
    .items: # of tweets
    """


    json_strings = [json.dumps(json_obj) for json_obj in searched_tweets] 
    out_file = 'samples.json'
    
    
    with open(out_file, 'a') as f:
        for tweet in json_strings:
            '''
            1.entities,user
            '''

            # store a tweet into the dictionary
            tweet_dict = simplejson.loads(tweet)
 
            #get tweet id
            #print(tweet_dict["id"])
            
            #get time stamp
            #print(tweet_dict["created_at"])
            
            # get tweet
            #print(tweet_dict["text"])
            
            # get user
            #print(tweet_dict["user"])
            
            # get geo
            #print(tweet_dict["geo"])
            
            #get hashtag
            hashtags=[]
            for hashtag in tweet_dict["entities"]["hashtags"]:
                #print(hashtag["text"])
                hashtags.append(hashtag["text"])
                
            new_dict={'id':tweet_dict["id"],
                      'created_at':tweet_dict["created_at"],
                      'text':tweet_dict["text"],
                      'hashtags':hashtags,
                      'user':tweet_dict["user"],
                      'geo':tweet_dict["geo"]}
            
            # print(new_dict)
            # print("\n\n")

#             lock = Lock()
# #     return searched_tweets
#             lock.acquire()
            f.writelines(json.dumps(new_dict)+"\n");
            # lock.release()
                    
            
            


     
    
