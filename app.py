import pandas as pd
import streamlit as st
import pickle

st.title('Movie Recommender System')

# Load the data
similarity = pickle.load(open('similarty.pkl', 'rb'))
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)


# Define the recommend function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movie = []
    for i in movies_list:
        recommended_movie.append(movies.iloc[i[0]].title)
    return recommended_movie


# Add a selectbox
selected_movie_name = st.selectbox(
    'Select a movie',
    movies['title'].values
)

# Add a button
if st.button("Recommend"):
    recommendations = recommend(selected_movie_name)
    st.write(f"Top 5 movies similar to **{selected_movie_name}** are:")
    for i in recommendations:
        st.write(i)
