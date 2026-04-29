import streamlit as st
import pickle
import pandas as pd


def recommend(song):
    music_index = musics[musics['SongName'] == song].index[0]
    distances = similarity[music_index]
    music_list = sorted(list(enumerate(distances)), reverse = True, key = lambda x:x[1])[1:6]
    
    recommended_music = []
    for i in music_list:
        recommended_music.append(musics.iloc[i[0]].SongName)
    return recommended_music
    
music_dict = pickle.load(open('music_dict.pkl', 'rb'))
musics = pd.DataFrame(music_dict)

similarity = pickle.load(open('similar.pkl', 'rb'))

print(music_dict)
st.title('Music Recommender System')
selected_music_name = st.selectbox(
"Choose your music",
musics['SongName'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_music_name)
    for i in recommendations:
        st.write(i)