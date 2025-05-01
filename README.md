# Movie-Recommender-System
🎬 Project Overview
This project is a Content-Based Movie Recommender System that suggests movies similar to a user’s input by analyzing the content of each movie (such as genres, keywords, cast, and director). The system uses text vectorization and cosine similarity to compute how closely related one movie is to another. When a user enters the name of a movie, the system returns a list of movies that share similar features.

🛠️ Tools and Technologies Used
Python – Core programming language for implementation.
Pandas – For data manipulation and preprocessing.
NumPy – For numerical computations.
Cosine Similarity- To find similarity between different movies in daatset.
Scikit-learn – For vectorization (CountVectorizer) and similarity calculation (cosine_similarity).
Streamlit - For deployment of moveie recommendeer system.

Jupyter Notebook – For interactive development and testing.

📂 Files Used
movies.csv – Contains movie-related metadata such as title, genre, cast, director, etc.
credits.csv – Contains additional information like cast and crew, used to enrich the dataset for better recommendations.
These files were merged and processed to create a unified dataset that captures key descriptive features of each movie.

movie recomendation.ipynb:  Main notebook
app.py : Streamlit deployment file

🌍 Real-World Applications
OTT platforms (like Netflix or Amazon Prime) – Can use this model to recommend similar movies based on what the user has already watched or liked.
Movie discovery apps – Helps users find new content that matches their preferences.
E-commerce and entertainment websites – Enhances user engagement by offering personalized recommendations based on content features.

