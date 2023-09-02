import streamlit as st
import pickle
import pandas as pd
import requests

def movie_poster(movie_id):
     response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=39777f21004865828f8edf2622f2567c&language=en-US'.format(movie_id))
     api_data = response.json()
     return "https://image.tmdb.org/t/p/w500" + api_data['poster_path']

def recommend(movie):
     movie_index = movies[movies['title'] == movie].index[0]
     distance = similarity[movie_index]
     movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

     recommended_movies = []
     recommended_movie_poster = []
     for i in movie_list:
          recommended_movies.append(movies.iloc[i[0]].title)
          recommended_movie_poster.append(movie_poster(movies.iloc[i[0]].movie_id))
     return recommended_movies, recommended_movie_poster

movies_dict = pickle.load(open('movies.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similar.pkl','rb'))

st.title('Movie-Recommender-System')

selected_movie_name = st.selectbox(
     'Select movie',
     movies['title'].values)

if st.button('Recommend'):
     names, poster = recommend(selected_movie_name)
     col1, col2, col3, col4, col5 = st.columns(5)
     with col1:
          st.text(names[0])
          st.image(poster[0])
     with col2:
          st.text(names[1])
          st.image(poster[1])
     with col3:
          st.text(names[2])
          st.image(poster[2])
     with col4:
          st.text(names[3])
          st.image(poster[3])
     with col5:
          st.text(names[4])
          st.image(poster[4])
