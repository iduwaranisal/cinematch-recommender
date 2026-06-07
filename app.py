import streamlit as st
import pickle
import pandas as pd
import requests
import os
import gdown

st.set_page_config(page_title="CineMatch", page_icon="🍿", layout="wide")

st.markdown("""
<style>
    .reportview-container {
        background: #141414;
        color: white;
    }
    h1 {
        color: #E50914;
        text-align: center;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        font-weight: 700;
        margin-bottom: 2rem;
    }
    .stButton>button {
        background-color: #E50914;
        color: white;
        border: none;
        border-radius: 4px;
        padding: 0.5rem 2rem;
        font-size: 1.1rem;
        font-weight: 600;
        transition: background-color 0.3s;
    }
    .stButton>button:hover {
        background-color: #B20710;
        color: white;
    }
    .movie-title {
        font-size: 1.1rem;
        font-weight: bold;
        text-align: center;
        margin-top: 0.5rem;
        height: 3rem; 
        overflow: hidden;
        text-overflow: ellipsis;
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;
    }
    img {
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.3);
        transition: transform 0.3s ease;
    }
    img:hover {
        transform: scale(1.05);
    }
</style>
""", unsafe_allow_html=True)

def fetch_poster(movie_id):
    try:
        # Note: Production වලදී API keys `.env` file එකක් හරහා පාවිච්චි කරන එක වඩා ආරක්ෂිතයි
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
        response = requests.get(url)
        response.raise_for_status() 
        data = response.json()
        poster_path = data.get('poster_path')
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
        else:
             return "https://via.placeholder.com/500x750.png?text=No+Poster+Available"
    except requests.exceptions.RequestException:
        return "https://via.placeholder.com/500x750.png?text=Error+Loading+Poster"

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    recommended_movie_posters = []
    
    for i in movies_list:
        movie_id = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id))
        
    return recommended_movies, recommended_movie_posters

@st.cache_data
def load_data():

    movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
    
    similarity_path = 'similarity.pkl'

    file_id = '1TOTyykOWTnDA9byQdWh8vU52yyfgNvcy' 

    if not os.path.exists(similarity_path):
        with st.spinner("Downloading similarity data... This may take a moment on the first run."):
            gdown.download(id=file_id, output=similarity_path, quiet=False)
            
    similarity_data = pickle.load(open(similarity_path, 'rb'))
    
    return pd.DataFrame(movie_dict), similarity_data

movies, similarity = load_data()

st.title("🍿 CineMatch Recommender")

st.markdown("<h4 style='text-align: center; color: #808080;'>Find your next favorite movie!</h4>", unsafe_allow_html=True)
st.write("") 

col_left, col_mid, col_right = st.columns([1, 2, 1])

with col_mid:
    select_movie_name = st.selectbox(
        '',
        movies['title'].values,
        index=0,
        placeholder="Type or select a movie..."
    )

    st.write("")
    if st.button('Show Recommendations', use_container_width=True):
        with st.spinner('Curating recommendations...'):
            recommendations, posters = recommend(select_movie_name)
            st.success('Done!')

st.write("---")

if 'recommendations' in locals() and recommendations:
    st.markdown("<h3 style='margin-bottom: 1rem;'>Top Picks for You</h3>", unsafe_allow_html=True)
    cols = st.columns(5)
    
    for idx, col in enumerate(cols):
        with col:
            st.image(posters[idx], use_container_width=True)
            st.markdown(f"<div class='movie-title'>{recommendations[idx]}</div>", unsafe_allow_html=True)