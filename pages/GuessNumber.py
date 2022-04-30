import streamlit as st
from PIL import Image
import numpy as np
import random
num=random.randint(1,20)
guesses=[]
guesses_result=[]

def app():
    result=""
    display = Image.open('encoded.jpg')
    display = np.array(display)
    st.image(display)
    header=st.container()
    result_all = st.container()
    with header:
        guess= st.text_input("Enter your Guess (1-20)",value="0")
        guess= int(guess)
        print (guess)
        st.write("Number Guessed:", guess)
        guesses.append(guess)
        if guess > num:
            result="Too High"
        if guess < num:
            result="Too Low"
        if guess == num:
            result="Correct"
        guesses_result.append(result)
        st.write(result)
        print("Answer:", num)
        st.write("Guesses so far:")
        guesses_string=", ".join(str(x) for x in guesses)
        guesses_result_string=", ".join(str(x) for x in guesses_result)
        st.write(guesses_string)
        st.write(guesses_result_string)
        
