#!/usr/bin/python3

import random
import string
import time
from collections import Counter
from functools import reduce
from itertools import chain

import requests

url2 = "

#A Maybe monada
class MyMonad:
    def __init__(self, value=None):
        self.value = value

    def is_empty(self): #return a bool. In python "is" function is a comparator
        return self.value is None

    def get(self):
        if self.is_empty():
            print("No value to return. get() return nothing")
        return self.value

    '''
    Name:   bind
    Type:   High-order function
    Def:    bind applies a function (func) that returns a Monad to the
            value inside the Monad, effectively chaining operations
    Usage:  To chain multiple operations to function that returns a monad
    '''
    def bind(self, func):
        if self.is_empty():
            return self
        else:
            return func(self.value)


    def checkType(self):
        if not isinstance(self.value, (str, list, dict)):
            raise TypeError("The input must be a string or a list of strings.")
        if isinstance(self.value, list) and not all(isinstance(item, (str,dict)) for item in self.value):
            raise TypeError("The list must contain only strings.")
        return self

    '''
    Name:   flat_map
    Type:   functor, high-order function
    Def:    map applies a function (func) to the value
            inside the Monad (self.value) map works with
            functions that return regular values and
            returns a new Monad with the result
    '''
    def flat_map(self, func):
        if self.is_empty():
            return self
        else:
            self.checkType()
            return MyMonad(list(map(func,self.value)))

    '''
    Name:   flat_filter
    Type:   functor, high-order function
    Def:    filter applies a function (func) to the value
            inside the Monad (self.value), an iterator.
            Functions passed shal return True if the
            search/value is found, else False.
    '''
    def flat_filter(self,func):
        newlist = []
        if self.is_empty():
            return self
        else:
            self.checkType()
        return MyMonad(list(filter(func,self.value)))

    def __repr__(self):
        return f'MyMonad({self.value})'


'''
Name: tokenize
Type:First-Class Functions
Def:
'''
def tokenize(text):
    #remove  any punctuation and remove lowercase
    text = text.translate(str.maketrans("","",string.punctuation)).lower()
    #partir el texto en palabras
    tokens = text.split()
    return tokens

'''
Name: avg_word_lenght
Type: First-Class Functions
Def:
'''
def avg_word_lenght(tokens):
    total_lenght = reduce(lambda total, word: total + len(word), tokens,0)
    return total_lenght/len(tokens) if tokens else 0 #ternary operation in python


'''
Name: get_PushEvent_msgs
Type: First-Class Functions
Def:
'''
def get_PushEvent_msgs(resp):
    msg_txt = resp['payload']['commits'][0]['message']+" "
    return msg_txt

'''
Name: fetch_user_data
Type: First-Class Functions
Def:    Functions that can be treated as any other
        variable meaning they can be passed ar arguments,
        returned from other functions and assigned to variables
'''
def fetch_user_data():
    response = requests.get(url2)
    return response

'''
Name: filter_PushEvents
Type: First-Class Functions
Def:
'''
def filter_PushEvents(n):
    if n.get("type") == "PushEvent":
        return True
    else:
        return False

'''
Name: word_frequency
Type: First-Class Functions
Def:
'''
def word_frequency(tokens):
    #return list(map(Counter,tokens))
    #flatened_list =  [word for sublist in tokens for word in sublist]
    flatened_list = list(chain(*map(lambda x: x, tokens)))
    return Counter(flatened_list)

'''
Name:   most_common_words
Type:   First class function
Def:
'''
def most_common_words(frequency, num=3):
    #return list(map((frequency.most_common(num))))
    return frequency.most_common(num)

if __name__ == "__main__":
    while True:
        resp = fetch_user_data()

        git_events = MyMonad(resp.json())

        gith_filtered_data = git_events.flat_filter(filter_PushEvents)

        git_push_msgs = gith_filtered_data.flat_map(get_PushEvent_msgs)

        tokens = git_push_msgs.flat_map(tokenize)

        #print(f"tokens:{tokens.get()}\n")

        print(f"Total PushEvents:{len(gith_filtered_data.get())}")

        print(f"Total words:{reduce(lambda total, sublist: total + len(sublist),tokens.value,0)}")

        test = tokens.get()

        frequency = word_frequency(test)
        comm_words = most_common_words(frequency)
        print(f"Most common words:{comm_words}")
        print(f"PushEvent avg word length:{avg_word_lenght(tokens.get())}")

        interval = random.uniform(5,14)
        print(f"next request in: {interval}")
        print(f"press Ctrl+Z to stop the programm\n")
        time.sleep(interval)
