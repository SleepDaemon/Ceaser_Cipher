import os
import streamlit as st
from PIL import Image
import numpy as np
import random
# Custom imports 
from multipage import MultiPage

from pages import Encoder, Decoder, Content, GuessNumber
# Create an instance of the app 
app = MultiPage()

# Title of the main page
# display = Image.open('cover.jpg')
# display = np.array(display)
# st.image(display)
st.title("Ceaser Cipher")
st.text("Encrypt or Decrypt using Ceaser Cipher")

# col1 = st.columns(1)
# col1, col2 = st.columns(2)
# col1.image(display, width = 400)
# col2.title("Data Storyteller Application")

# Add all your application here
app.add_page("Content", Content.app)
app.add_page("Encoder", Encoder.app)
app.add_page("Decoder", Decoder.app)
app.add_page("Guess Number", GuessNumber.app)


if 'num' not in st.session_state:
    st.session_state['num'] = random.randint(1,20)
if 'guesses' not in st.session_state:
    st.session_state['guesses'] = []
if 'gueses_result' not in st.session_state:
    st.session_state['guesses_result'] = []
# The main app
app.run()
