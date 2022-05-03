from git import refresh
import streamlit as st
from PIL import Image
import numpy as np
import random

if 'num' not in st.session_state:
    st.session_state['num'] = random.randint(1,20)

#num=random.randint(1,20)
guesses=[]
guesses_result=[]

def app():
    if "num" not in st.session_state:
        st.session_state['num'] = random.randint(1,20)

    num=st.session_state['num']
    result=""
    display = Image.open('encoded.jpg')
    display = np.array(display)
    st.image(display)

    header=st.container()
    result_all = st.container()

    with header:
        guess= st.text_input("Enter your Guess (1-20)",value="0")
        guess= int(guess)
        #Computer doesn't check for zero
        if guess!=0:
            print (guess)
            st.write("Number Guessed:", guess)
            guesses.append(guess)
            if guess > num:
                result="Too High"
            elif guess < num:
                result="Too Low"
            elif guess == num:
                #Game Reset (clears result and guess list)
                result="Correct"
                guesses.clear()
                guesses_result.clear()
                st.session_state['num'] = random.randint(1,20)
                num=st.session_state['num']
                print("New random number is ",num)
        
            guesses_result.append(result)
            st.write(result)
            print("Answer:", num)
            st.write("Guesses so far:")
            guesses_string=", ".join(str(x) for x in guesses)
            st.write(guesses_string)
            #To get rid of correct from the final result string
            if "Correct" in guesses_result:
                guesses_result.remove("Correct")

            guesses_result_string=", ".join(str(x) for x in guesses_result)
            st.write(guesses_result_string)

    