import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
     response= requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=b5dd0618ecc340e7ab0beea8d6da1021')
     data=response.json()
     return "https://image.tmdb.org/t/p/w500/" + data['poster_path']




def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movies_sorted = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    recommend_movies=[]
    recommended_movies_posters = []
    for i in movies_sorted:
        movie_id=movies.iloc[i[0]].id
        recommend_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommend_movies , recommended_movies_posters

st.title('MOVIE RECOMMENDAR SYSTEM')
movies_list=pickle.load(open('movies.pkl', 'rb'))
movies=pd.DataFrame(movies_list)

similarity=pickle.load(open('similarity.pkl', 'rb'))

selected_movie_name= st.selectbox(
    "Choose the Movie",

movies['title'].values)


if st.button("Recommend"):
   names ,posters = recommend(selected_movie_name)

   col1, col2, col3 , col4 , col5 = st.columns(5)

   with col1:
       st.text(names[0])
       st.image(posters[0])

   with col2:
       st.text(names[1])
       st.image(posters[1])

   with col3:
       st.text(names[2])
       st.image(posters[2])

   with col4:
        st.text(names[3])
        st.image(posters[3])

   with col5:
       st.text(names[4])
       st.image(posters[4])







