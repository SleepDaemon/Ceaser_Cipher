import os
import streamlit as st
from PIL import Image
import numpy as np
import random
# Custom imports 
from multipage import MultiPage

from pages import Encoder, Decoder, Content, GuessNumber, AlphaBetaGamma
# Create an instance of the app 
app = MultiPage()

# Title of the main page
# display = Image.open('cover.jpg')
# display = np.array(display)
# st.image(display)
# st.title("Games in Python")
# st.text("Play games that were written in Python!")

# col1 = st.columns(1)
# col1, col2 = st.columns(2)
# col1.image(display, width = 400)
# col2.title("Data Storyteller Application")

# Add all your application here
app.add_page("Content", Content.app)
app.add_page("Encoder", Encoder.app)
app.add_page("Decoder", Decoder.app)
app.add_page("Guess Number", GuessNumber.app)
app.add_page("Alpha Beta Gamma", AlphaBetaGamma.app)

#Session State for GuessNumber
if 'num' not in st.session_state:
    st.session_state['num'] = random.randint(1,20)
if 'guesses' not in st.session_state:
    st.session_state['guesses'] = []
if 'gueses_result' not in st.session_state:
    st.session_state['guesses_result'] = []

# Seession State for AlphaBetaGamma
lst = random.sample(range(0, 9), 3)
lst2=[]
for val in lst:
    lst2.append(str(val))
lst=lst2
if 'AlphaBetaGamma_list' not in st.session_state:
    st.session_state['AlphaBetaGamma_list'] = lst
print("3 digits", st.session_state['AlphaBetaGamma_list'])
if 'AlphaBetaGamma_guesses' not in st.session_state:
    st.session_state['AlphaBetaGamma_guesses'] = []

# The main app
app.run()
