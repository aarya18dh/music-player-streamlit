import streamlit as st
import streamlit.components.v1 as components
import requests

st.set_page_config(page_title="Music Player", layout="centered")

# Fetch HTML file from GitHub repo (raw link)
url = "https://raw.githubusercontent.com/<aarya18dh>/music-player-streamlit/main/music_player.html"
html_code = requests.get(url).text

components.html(html_code, height=720, scrolling=True)
