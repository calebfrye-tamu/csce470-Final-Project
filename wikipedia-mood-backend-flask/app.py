from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from bm25 import *
app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

#call this function upon program start to precalculate all necessary information
articles, idfs, avg_title_len, avg_body_len = load_articles_and_compute_idfs()

@app.route('/search', methods=['POST'])
@cross_origin
def search_articles():
    data = request.get_json()
    query = data.get('query', '')
    mood = data.get('mood', 'general') # default to "general" 
    print(f"Finding articles with mood={mood.lower()}")

    #score each article in CORPUS_DIR
    ranked_articles = [
        (article, bm25_score(query, article, idfs, avg_title_len, avg_body_len, mood))
        for article in articles
    ]

    #sort by mood weighted bm25 score
    ranked_articles.sort(key=lambda x: x[1][1], reverse=True)

    #get the top 100 articles from the ranked articles list and 
    #send their information as an http response
    top_articles = [
        {
            'title': article['title'],
            'snippet': article['content-preview'][:300],
            'url': article['url'],
            'mood_weighted_score': mood_weighted_bm25_score,
            'raw_score': raw_bm25_score,
            'mood_score': mood_multiplier
        }
        for article, (raw_bm25_score, mood_weighted_bm25_score, mood_multiplier) in ranked_articles[:100]
    ]

    return jsonify({'results': top_articles})

if __name__ == '__main__':
    app.run(port=12000, debug=True)
