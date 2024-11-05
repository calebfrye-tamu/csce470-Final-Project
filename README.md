
# WikiMood Search Tool
### Final Project for CSCE 470

This web app allows you to search for wikipedia articles using a query and a mood. Articles are ranked against the query using BM25,  and the mood is weighted based on how many times so-called 'mood words' appear in the article. The corpus contains information about each article in a json file, including: 
- title
- url
- content preview
- title and body term frequencies
- mood scores. 

By precalculating all of the term frequencies, it allows the app to store a huge corpus of documents while hardly taking up any storage space. It also improves response time drastically. 

## How to run the app locally
#### Prerequisites:
The app uses an Angular server for the frontend UI and a  Flask server for the backend API. To run the app, you need to start both servers on your computer. To do this, make sure you install the following before you start:
- python
- pip
- npm installed on your computer 

Once you have npm installed, you'll need to install the Angular CLI if you don't have it already. To do that, run 
``npm install -g @angular/cli. ``

#### Starting the Backend API server
Open a terminal in the `wikipedia-mood-backend-flask` folder. Create a virtual environment for python by typing:
`` python3 -m venv .venv ``
You should see your command line now says 'venv' somewhere. 
Then, run  ``. .venv/bin/activate`` to activate the environment. 
Install all required dependencies by typing 
``pip install -r requirements.txt``
If everything went well, start the server by typing: ``python3 app.py`` 
The flask server should start on port 12000. It is important that the server is on port 12000 and not any other port, because the Angular frontend expects port 12000. The backend API is now ready.

#### Starting the Frontend UI server
Open a different terminal into the ``wikipedia-mood-frontend`` directory. You should have already installed the Angular CLI, so type: `ng serve -o` to start the Angular server. Your web browser should open to the WikiMood UI page. The frontend is now ready to use.  
