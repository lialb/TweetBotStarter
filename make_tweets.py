'''
This class will be used to make the tweets themselves. We will be using the
tweepy and json libraryself.
This will make the actual tweets from the AI generated tweets. It parses
through the json containing the keys and access tokens.
'''
import tweepy
import json
from markov_generator import generate_tweet

#TODO: Get your authentication for your twitter account using the JSON with your API keys

with open('YOUR_FILE_HERE') as :
    api_keys =

auth = tweepy.OAuthHandler('YOUR KEYS AND SECRETS SHOULD GO HERE')
auth.set_access_token('What should go here?')

api = tweepy.API('your authentication thingy should go here.')


'''
Now we have finished the authentication for your twitter account. We will
see if we have the correct account using the following print statement.
'''
user = api.me()
print(user.name)


'''
After we confirm that it is indeed our account, we will now begin making simple
tweets from the command line. Using the function api.update_status('your_tweet'),
try making a tweet!
'''



'''
Now let's have our tweetbot print at a set interval of time. Using the "time" library
try tweeting every 10 seconds for one minute! HINT: you may find
https://docs.python.org/3/library/time.html very useful!
'''
import time
tweet_count = 0
while (tweet_count < 6):
    #Make your tweet
    #Make the time stall for 10 seconds
    count += 1
