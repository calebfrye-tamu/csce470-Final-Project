import os
import json
import requests
import argparse
from tqdm import tqdm  #tqdm for the progress bar

# import the constants defined in constants.py
# from constants import *

# import the helper functions I made
from constants import *
from helper_functions import tokenize, create_vector

S = requests.Session()

# ensure the output directory exists
if not os.path.exists(CORPUS_DIR):
    os.makedirs(CORPUS_DIR)

# Function to calculate the mood score for a document
def calculate_mood_word_freqency(title_terms, content_terms):
    mood_scores = {}
    for mood, words in mood_words.items():
        score = sum(title_terms.get(word, 0) + content_terms.get(word, 0) for word in words)
        mood_scores[f"{mood.lower()}_frequency"] = score
    return mood_scores

# NOT WORKING Re-fetch full content for each existing article and recompute vectors
# def recompute_vectors():
    existing_articles = []
    for filename in os.listdir(CORPUS_DIR):
        if filename.endswith(".json"):
            with open(os.path.join(CORPUS_DIR, filename), 'r') as f:
                existing_articles.append(json.load(f))

    print(f"Recomputing vectors for {len(existing_articles)} articles...")

    for article in tqdm(existing_articles, desc="Processing Articles", unit="article"):
        try:
            title, content, url = fetch_article_content(article['id'])
            if content:
                article_info = {
                    'title': title,
                    'content-preview': content[:CONTENT_PREVIEW_LENGTH],
                    'url': url,
                    'pageid': article['id']
                }
                
                #preprocess and tokenize title and content
                title_tokens = tokenize(title)
                content_tokens = tokenize(content)
                if len(content_tokens) < MIN_ARTICLE_LENGTH:
                    continue  # Skip articles that are too short
                
                #create term frequency vectors
                article_info['title-terms'] = create_vector(title_tokens)
                article_info['content-terms'] = create_vector(content_tokens)
                article_info['title-length'] = len(title_tokens)
                article_info['content-length'] = len(content_tokens)
                
                #calculate mood scores
                mood_scores = calculate_mood_word_freqency(article_info['title-terms'], article_info['content-terms'])
                article_info.update(mood_scores)
                
                #save article data with mood scores to a new json file in CORPUS_DIR
                pageid = article_info['pageid']
                filepath = os.path.join(CORPUS_DIR, f"{pageid}.json")
                with open(filepath, 'w') as f:
                    json.dump(article_info, f, indent=2)
                num_articles_fetched += 1

        except Exception as e:
            print(f"Error fetching article '{article['title']} (ID: {article['id']}': {e}")


# fetches random articles using the WikiMedia API and returns data about them.
# note: does not return the article's content, that is why fetch_article_content() is also defined
def fetch_random_articles(num_pages):
    RANDOM_PARAMS = {
        "action": "query",
        "format": "json",
        "list": "random",
        "rnlimit": num_pages,
        "rnnamespace": 0  # Namespace 0 is for articles
    }
    R = S.get(url=URL, params=RANDOM_PARAMS)
    DATA = R.json()
    return DATA["query"]["random"]

# fetches the title, content, url, and pageid of an article given its pageid
def fetch_article_content(pageid):
    CONTENT_PARAMS = {
        "action": "query",
        "format": "json",
        "prop": "extracts|info",  #requests content and url
        "explaintext": True, 
        "inprop": "url", 
        "pageids": pageid
    }
    R = S.get(url=URL, params=CONTENT_PARAMS)
    DATA = R.json()
    
    # extract the information from the article's json data
    pages = DATA.get('query', {}).get('pages', {})
    if pages:
        page_data = list(pages.values())[0]
        content = page_data.get('extract', '')
        title = page_data.get('title', '')
        url = page_data.get('fullurl', '')

        if "may refer to" in content.lower():
            return None, None, None  # skip disambiguation pages
        return title, content, url
    return None, None, None

# Fetch and store articles with mood scores and dictionary vectors
def fetch_and_store_articles(num_pages):
    print(f"Fetching {num_pages} Random Wikipedia articles...")

    random_articles = fetch_random_articles(num_pages)
    num_articles_fetched = 0

    for article in tqdm(random_articles, desc="Processing Articles", unit="article"):
        try:
            title, content, url = fetch_article_content(article['id'])
            if content:
                article_info = {
                    'title': title,
                    'content-preview': content[:CONTENT_PREVIEW_LENGTH],
                    'url': url,
                    'pageid': article['id']
                }
                
                #preprocess and tokenize title and content
                title_tokens = tokenize(title)
                content_tokens = tokenize(content)
                if len(content_tokens) < MIN_ARTICLE_LENGTH:
                    continue  # Skip articles that are too short
                
                #create term frequency vectors
                article_info['title-terms'] = create_vector(title_tokens)
                article_info['content-terms'] = create_vector(content_tokens)
                article_info['title-length'] = len(title_tokens)
                article_info['content-length'] = len(content_tokens)
                
                #calculate mood scores
                mood_scores = calculate_mood_word_freqency(article_info['title-terms'], article_info['content-terms'])
                article_info.update(mood_scores)
                
                #save article data with mood scores to a new json file in CORPUS_DIR
                pageid = article_info['pageid']
                filepath = os.path.join(CORPUS_DIR, f"{pageid}.json")
                with open(filepath, 'w') as f:
                    json.dump(article_info, f, indent=2)
                num_articles_fetched += 1

        except Exception as e:
            print(f"Error fetching article '{article['title']} (ID: {article['id']}': {e}")

    print(f"Articles and vectors with mood scores successfully stored in '{CORPUS_DIR}' directory. Total articles: {num_articles_fetched}")
    return num_articles_fetched


if __name__ == '__main__':
    #parse arguments
    parser = argparse.ArgumentParser(description="Wikipedia Article Fetcher and Vector Recalculator")
    parser.add_argument('--recompute', action='store_true', help="Recompute vectors for existing articles")
    args = parser.parse_args()

    # recompute vectors if the '--recompute' argument is passed
    # if args.recompute:
    #     recompute_vectors()

    i = 0
    while (i < NUM_ARTICLES_TO_FETCH):
        if (i < 0):
            break
        i += fetch_and_store_articles(min((NUM_ARTICLES_TO_FETCH - i), 500))
        print(f"Fetched {i} articles of length > {MIN_ARTICLE_LENGTH}, fetching more...")
    print(f"Fetched {i} articles of length > {MIN_ARTICLE_LENGTH}")
