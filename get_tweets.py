import requests
from requests_oauthlib import OAuth1

import json
import csv
import pprint
import argparse
from markov_generator import generate_tweet

pp = pprint.PrettyPrinter()

'''
After you have finished make_tweets, we will now retrieve tweets from people on
Twitter. Firstly, try the authentication; it is similar to how we finished make_tweets
'''
with open(API_KEY_FILE_HERE) as :
    api_keys = json.load()
# Authentication for Twitter loaded into OAuth1 object
#Your key, secret, access_token, and access_secret should go here
auth = OAuth1('Use your api_keys.json')

'''
Now we will use the requests library to retrieve users' tweets.
'''
def get_tweets(tweet_handle, writeto):
    url = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
    params = {
        'screen_name': tweet_handle,
        'tweet_mode': 'extended',
        'count': '200',
        'include_rts': False,
        'exclude_replies': True,
        'trim_user': True,
    }

    with open(WRITE_FILE_HERE) as :
        fieldnames = ['id', 'text', 'source']
        
        # Now lets use csv.DictWriter to write this to a file!
        # https://docs.python.org/3/library/csv.html


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('tweet_handle', type=str, help='the tweet handle to get tweets from, case insensitive and without the @')
    parser.add_argument('write_to', type=str, help='what file to write the tweet data to')
    args = parser.parse_args()
    get_tweets(args.tweet_handle, args.write_to)
