
# directory where the system will search in, and where 
# newly fetched articles will be stored 
CORPUS_DIR = 'corpus_checkpoint_2'

CONTENT_PREVIEW_LENGTH = 300 #amount of characters of the content stored in the json file
MIN_ARTICLE_LENGTH = 300 # min length of the articles to fetch AFTER stopwords removed
NUM_ARTICLES_TO_FETCH = 500

URL = "https://en.wikipedia.org/w/api.php" #url for the WikiMedia API

mood_words = {
    "Curious": [
        "scientific", "scientifically", "learn", "learning", "explore", "exploring", 
        "investigation", "investigative", "investigate", "discovery", "discovering", 
        "groundbreaking", "breakthrough", "research", "researching", "curiosity", 
        "curious", "hypothesis", "hypotheses", "theory", "theories", "uncover", 
        "uncovering", "analyze", "analysis", "question", "questioning", "knowledge", 
        "knowledge-seeking", "phenomenon", "phenomena", "experiment", "experimental", 
        "observation", "observed"
    ],
    "Uplifting": [
        "inspiring", "inspiration", "hopeful", "hope", "positive", "positivity", 
        "motivating", "motivation", "persevere", "perseverance", "encourage", 
        "encouragement", "uplifting", "resilience", "resilient", "overcome", 
        "overcoming", "strength", "strong", "achieve", "achievement", "fulfilling", 
        "fulfilled", "joyful", "joy", "gratitude", "grateful", "success", "successful", 
        "optimistic", "optimism", "passion", "passionate", "thriving", "flourish", 
        "flourishing", "progress", "progressing"
    ],
    "Entertaining": [
        "movie", "movies", "fascinating", "fascination", "fascinate", "story", 
        "stories", "entertaining", "entertainment", "amusing", "amusement", 
        "funny", "humor", "dramatic", "drama", "comedy", "comedies", "captivating", 
        "captivate", "captivatingly", "engaging", "thrill", "thrilling", "adventure", 
        "adventurous", "epic", "characters", "character", "plot", "action", "scenes", 
        "spectacle", "charismatic", "charm", "charming", "delightful", "excitement", 
        "excite", "exciting", "mystery", "mysteries"
    ],
    "Sad": [
        "death", "deaths", "famine", "genocides", "genocide", "murder", "murders", 
        "lost", "loss", "losses", "grief", "grieving", "sorrow", "sorrowful", "mourn", 
        "mourning", "tragedy", "tragic", "heartbreak", "heartbroken", "disaster", 
        "disasters", "disease", "diseases", "illness", "illnesses", "plague", "plagues", 
        "starve", "starving", "starvation", "despair", "despairing", "suffering", 
        "suffer", "suffered", "affliction", "afflicted", "anguish", "bereavement", 
        "ruin", "ruined", "trauma", "traumatic", "devastation", "devastated", 
        "wounded", "wounds"
    ],
    "General": []  # no multiplier for general
}

stop_words = set([
    'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 
    'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 
    'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 
    'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 
    'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 
    'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 
    'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 
    'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 
    'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 
    'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 
    'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', 
    "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 
    'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 
    'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"
])