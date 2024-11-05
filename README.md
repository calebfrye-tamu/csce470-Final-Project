

# WikiMood Search Tool
### Final Project for CSCE 470
#### (The UI is currently is unpolished but fully functional. The backend is done now so I will be focusing on the UI from here on out)

This web app allows you to search for wikipedia articles using a query and a mood. Articles are ranked against the query using BM25,  and the mood is weighted based on how many times so-called 'mood words' appear in the article. The corpus contains information about each article in a json file, including: 
- title
- url
- content preview
- title and body term frequencies
- mood scores. 

By precalculating all of the term frequencies, it allows the app to store a huge corpus of documents while hardly taking up any storage space (2000 articles take up ~22 MB on my computer). It also improves response time drastically. 

## How to run the app locally
#### Prerequisites:
The app uses an Angular server for the frontend UI and a  Flask server for the backend API. To run the app, you need to start both servers on your computer. To do this, make sure you install the following before you start:
- python
- pip
- npm 

The installation methods for the above packages depends on your OS. Once you have npm installed, you'll need to install the Angular CLI if you don't have it already. To do that, run 
``npm install -g @angular/cli. ``

#### Starting the Backend API server
Open a terminal in the `wikipedia-mood-backend-flask` folder. Create a virtual environment for python by typing:
`` python3 -m venv .venv ``
Then, run  ``. .venv/bin/activate`` to activate the environment. You should see your command line now says 'venv' somewhere. 
Install all the required dependencies by typing 
``pip install -r requirements.txt``. If everything went well, you can start the backend API server by typing: ``python3 app.py`` (you may need to do python instead of python3 depending on your OS). 
The flask server should start on port 12000. It is important that the server is on port 12000 and not any other port, because the Angular frontend expects port 12000. The backend API is now ready.

#### Starting the Frontend UI server
Open a new terminal into the ``wikipedia-mood-frontend`` directory. You should have already installed the Angular CLI, so type: `ng serve -o` to start the Angular server. Your web browser should open to the WikiMood UI page. The frontend is now ready to use.  

### Core Algorithm
The core algorithm that the app uses is BM25. I calculate the term frequencies of each articles when I fetch them using the MediaWiki API. The code to fetch the articles is in `fetch_articles.py`, and you can fetch more articles if you want by running `python3 fetch_articles.py`. If you do this, you'll see the new articles' json files appearing in the CORPUS_DIR. Their filenames are '*pageid*.json'. You can configure the following parameters by changing the constants in `constants.py` in the backend code:
- CORPUS_DIR - directory that the system uses as the corpus for searching and storing newly fetched articles
- CONTENT_PREVIEW_LENGTH - number of characters of the content that will be saved to the json file
- MIN_ARTICLE_LENGTH - the minimum number of words in an article required for the system to store it AFTER stopwords have been removed
- NUM_ARTICLES_TO_FETCH - number of articles to fetch when you run the command to fetch more articles. Will only fetch articles that have more words than MIN_ARTICLE_LENGTH after stopwords have been removed. I recommend not going higher than 500 unless you want to wait for a while.

You can also see the mood words and stopwords dictionaries in `constants.py`. 

### Verifying the Core Algorithm (BM25)
I have prepared a corpus directory for Checkpoint 2 called `corpus_checkpoint_2/`. In this corpus you will find processed information about 2000 articles which I have fetched using `fetch_articles.py`. If you go to the frontend UI and perform a search query, you can see the scores assigned to each returned document. The scores displayed are:
- Mood-Weighted BM25 Score - the combined score of the mood multiplier and bm25 scores
- Raw BM25 Score
- Mood Multiplier - this is calculated by dividing the number of times the article contains mood words for the given mood by the total number of mood words for the mood. For example, if the article "WW2 Skirmish" has the word "death" 5 times and "famine" 2 times (which are both words in the 'Sad' mood list), and there are 14 different words in the 'Sad' mood list, the article's mood multiplier for 'Sad' would be $$ \frac{7}{14}  = 0.5$$

#### Verification of BM25
If you perform some queries in the frontend using the 'General' mood (mood weight always = 1) and look at the Raw BM25 score, you will be able to see that the highest ranked articles are indeed relevant to your query. Additionally, examine the code in `bm25.py` to see my BM25 logic. I believe you will find that it is correct. 

After you do some queries with the 'General' mood, try changing the mood to see how it affects the results. You may see some changes in which articles are ranked  at the top, and you can see how the mood multiplier changes. 
