import json
import requests
import argparse
import time
from requests_oauthlib import OAuth1
from markov_generator import generate_tweet

'''
This class will be used to make the tweets themselves. We will be using the requests and json library.
This will make the actual tweets from the AI generated tweets. It parses through the json containing the keys and access tokens.
'''

def make_tweets(csv_file, num_tweets):
    with open('KEY FILE HERE') as :
        api_keys = 
    auth = OAuth1(ADD AUTHENTICATION HERE)

    post_url = 'https://api.twitter.com/1.1/statuses/update.json'
    post_params = {
        'status': TEXT_TO_TWEET_HERE
    }

    # TODO: After we get posting working, try tweeting num_tweets tweets every 10 seconds!
    # Hint: You may find https://docs.python.org/3/library/time.html very useful!
    r = requests.post(POST PARAMS HERE)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('csv_file', type=str, help='the csv file to make tweets using')
    parser.add_argument('num_tweets', type=int, nargs='?', default=10, help='the number of tweets to make')
    args = parser.parse_args()
    make_tweets(args.csv_file, args.num_tweets)

