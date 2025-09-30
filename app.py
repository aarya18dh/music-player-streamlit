import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Music Player", layout="centered")

# Load the local HTML file
with open("music_player.html", "r", encoding="utf-8") as f:
    html_code = f.read()

components.html(html_code, height=720, scrolling=True)
