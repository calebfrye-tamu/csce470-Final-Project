import math, os, json
from collections import defaultdict

from constants import *
from helper_functions import tokenize

titleWeight = 1.5
bodyWeight = 0.5
B_title = 0.75
B_body = 0.5
K1 = 2

def load_articles_and_compute_idfs():
    articles = []
    for filename in os.listdir(CORPUS_DIR):
        if filename.endswith(".json"):
            with open(os.path.join(CORPUS_DIR, filename), 'r') as f:
                articles.append(json.load(f))
    
    avg_title_len = sum(doc['title-length'] for doc in articles) / len(articles)
    avg_body_len = sum(doc['content-length'] for doc in articles) / len(articles)
    
    idfs = compute_idfs(articles)
    
    return articles, idfs, avg_title_len, avg_body_len

def compute_idfs(documents):
    doc_count = len(documents)
    term_doc_frequency = defaultdict(int)
    
    for doc in documents:
        unique_terms = set(doc['title-terms'].keys()).union(set(doc['content-terms'].keys()))
        for term in unique_terms:
            term_doc_frequency[term] += 1

    idf = {term: math.log((doc_count + 1) / (freq + 1)) + 1 for term, freq in term_doc_frequency.items()}
    return idf

#returns raw bm25 score, mood-weighted bm25 score, and mood multiplier
def bm25_score(query, document, idfs, avg_title_len, avg_body_len, mood=None):
    query_terms = tokenize(query)
    bm25_score = 0

    # the mood boost is (document's score for this mood) / (number of mood words for this mood)
    mood_multiplier = ((document[f"{mood.lower()}_frequency"] + 1) / (len(mood_words[mood]) + 1)) 
    # print(f"MOOD BOOST FOR DOCUMENT: {document['title']} is {mood_multiplier}")
    
    if query != '':
        for term in query_terms:
            tf_title = document['title-terms'].get(term, 0)
            tf_body = document['content-terms'].get(term, 0)
            title_len = document['title-length']
            content_len = document['content-length']

            norm_tf_title = (tf_title * (K1 + 1)) / (tf_title + K1 * (1 - B_title + B_title * (title_len / avg_title_len)))
            norm_tf_body = (tf_body * (K1 + 1)) / (tf_body + K1 * (1 - B_body + B_body * (content_len / avg_body_len)))
            term_score = idfs.get(term, 0) * (titleWeight * norm_tf_title + bodyWeight * norm_tf_body)
        
            bm25_score += term_score
    else: #if query is none, we only care about the mood multiplier
        bm25_score = 1
    return bm25_score, bm25_score * mood_multiplier, mood_multiplier #apply the mood boost as a multiplier
