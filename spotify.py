import streamlit as st
import pandas as pd

st.set_page_config(layout="wide", page_title="Spotify Data")

df = pd.read_csv('spotify_data.csv')

st.title('Spotify Data')

df.set_index('Track', inplace=True)

artists = df['Artist'].unique()
selected_artist = st.selectbox('Select a Artist', artists)
df_filtred = df[df['Artist'] == selected_artist]

albums = df_filtred['Album'].unique()
selected_album = st.selectbox('Select a Album', albums)

df_filtred2 = df[df['Album'] == selected_album]

st.bar_chart(df_filtred2['Stream'])
