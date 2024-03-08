import pickle
import streamlit as st
import requests
import pandas as pd

#title
movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')



#fetching movie poster






# fetching data from the model

def recommend(movie_name):
    movie_index = movies[movies['title'] == movie_name].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


# Select box
selected_movie_name = st.selectbox(
    'Select movie from here .... ><', movies['title'].values)

# Button
if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for movie in recommendations:
        st.write(movie)
