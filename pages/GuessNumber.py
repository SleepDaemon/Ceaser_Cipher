import streamlit as st
from PIL import Image
import numpy as np

def app():
    display = Image.open('encoded.jpg')
    display = np.array(display)
    st.image(display)
    header=st.container()
    result_all = st.container()
    with header:
        guess= st.text_input("Enter your Guess",value="0")
        guess= int(guess)
        # st.write(encoded)
        print (guess)
        st.write("Number Guessed:", guess)