import os, json, string
from collections import Counter

from constants import *
# from bm25 import *

# tokenize raw text; remove punctuation and convert to lowercase
def tokenize(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    tokens = text.split()  # Tokenize
    tokens = [word for word in tokens if word not in stop_words]
    return tokens

# create a dictionary term frequency vector for each document
def create_vector(tokens):
    return dict(Counter(tokens)) 

