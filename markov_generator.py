import random
import pandas as pd
import string
import argparse

TWEET_LENGTH = 280

'''
Main function, takes in a csv file and generates tweet text based on that data
@param csv: the csv file name to pull tweets from
@return the generated markov chain string
'''
def generate_tweet(csv):
    begin_words, word_chain = get_markov_dict(get_tweets_csv(csv))
    word = random.choice(begin_words)
    ret_str = ''
    for i in range(100):
        if (len(ret_str) + len(word + ' ')) > TWEET_LENGTH:
            break
        ret_str += word + ' '
        clean_word = clean_string(word)
        if (word_chain[clean_word] == []):
            break
        word = random.choice(word_chain[clean_word])
    return ret_str

'''
 Returns a dictionary with word frequencies associated with each word
 The dictionary word_chain is going to have a word as a key, and a list of all the words that follow it as the value
 The list begin_words just has every starting word from library
 @param library: an array of strings to parse from
 @return a tuple containing beginning words, word-frequency dictionary
'''
def get_markov_dict(library):
    # TODO: COMPLETE MARKOV CHAINS
    word_chain = {}
    begin_words = []
    # Iterate through every sentence in the library
    # Remember to clean the string using clean_string()!
        # Then iterate through every word in the sentence and add it to the dictionary and list
    return begin_words, word_chain

'''
Used to strip string of mentions, hashtags so we don't get banned.
Also replaces html encoding of &amp with &
@param input: the string to clean words from
@return the cleaned string
'''
def clean_string(input):
    input = input.replace('&amp', '&')
    input = input.replace('&;', ';')
    input = input.replace('@', '')
    input = input.replace('#', '')
    return input;

'''
Uses pandas to read the csv file for tweet text.
@param csv: the csv filename as a string
@return a data frame object
'''
def get_tweets_csv(csv):
    df = pd.read_csv(csv)
    return df['text'].tolist()




#Don't modify anything below!
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('csv_file', type=str, help='the csv file to make tweets using')
    args = parser.parse_args()
    print(generate_tweet(args.csv_file))
