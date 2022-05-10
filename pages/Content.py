import streamlit as st
from PIL import Image
import numpy as np

def app():
    display = Image.open('game_over.webp')
    display = np.array(display)
    st.image(display)
    st.title("Play Games Built in Python")
    st.subheader('Ceaser Cipher')
    st.subheader('Guess the Number')
    st.subheader('Alpha Beta Gamma')
    st.caption('Select Game from Sidebar')