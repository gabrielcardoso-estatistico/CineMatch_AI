import streamlit as st
import pickle
import pandas as pd
import requests

# Configuração da página
st.set_page_config(page_title="CineMatch AI", layout="wide")

# Função para buscar poster via API do TMDB
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=553379ae2b4cb4cea3399fb36a34bbf9&language=pt-BR"
    try:
        data = requests.get(url).json()
        poster_path = data['poster_path']
        return "https://image.tmdb.org/t/p/w500/" + poster_path
    except:
        return "https://via.placeholder.com/500x750?text=Poster+Indisponivel"

# Carregamento dos dados salvos
@st.cache_resource
def load_data():
    movies = pickle.load(open('movies_list.pkl', 'rb'))
    similarity = pickle.load(open('similarity_matrix.pkl', 'rb'))
    return movies, similarity

movies, similarity = load_data()

st.title("🎬 CineMatch AI: Recomendador High-Tech")
st.markdown("Sistema de recomendação utilizando **Deep Learning (BERT)** e filtragem híbrida.")

# Barra lateral para filtros
st.sidebar.header("Configurações")
selected_movie = st.sidebar.selectbox("Escolha um filme base:", movies['title'].values)

all_genres = sorted(list(set([g for sublist in movies['genres'] for g in sublist])))
selected_genres = st.sidebar.multiselect("Filtre por gêneros desejados:", all_genres, default=["Action", "Adventure", "Science Fiction"])

num_rec = st.sidebar.slider("Quantidade de recomendações:", 5, 20, 10)

if st.sidebar.button("Gerar Recomendações"):
    idx = movies[movies['title'] == selected_movie].index[0]
    distances = sorted(list(enumerate(similarity[idx])), reverse=True, key=lambda x: x[1])
    
    recomms = []
    for i in distances[1:]:
        m_idx = i[0]
        m_genres = movies.iloc[m_idx].genres
        if any(g in m_genres for g in selected_genres):
            recomms.append(movies.iloc[m_idx])
        if len(recomms) == num_rec:
            break

    # Exibição em Grid
    if recomms:
        cols = st.columns(5)
        for i, movie in enumerate(recomms):
            with cols[i % 5]:
                st.image(fetch_poster(movie.id))
                st.subheader(movie.title)
                st.caption(f"⭐ Score: {round(distances[i+1][1]*100, 1)}%")
                st.write(f"🎭 {', '.join(movie.genres[:2])}")
    else:
        st.error("Nenhum filme encontrado com esses critérios.")