from git import refresh
import streamlit as st
from PIL import Image
import numpy as np
import random

guesses_result_local=[]

def app():
    st.title("Guess the Number")
    st.text("This is a game that will allow you to guess a number between 1 and 20.")
    result=""
    display = Image.open('guessnumber.jpeg')
    display = np.array(display)
    st.image(display)

    header=st.container()

    
    with header:
        guess= st.text_input("Enter your Guess (1-20)",value="")

        #Computer doesn't check for zero
        if guess!="":
            print (guess)
            guess= int(guess)
            st.write("Number Guessed:", guess)
            
            if guess > st.session_state['num']:
                result="Too High"
            elif guess < st.session_state['num']:
                result="Too Low"

            if guess!=st.session_state['num']:
                print("Result:",result)
                st.session_state['guesses'].append(guess)
                print("Session Values:", st.session_state['guesses'])
            else:
                #Game Reset (clears result and guess list)
                result="Correct"
                st.session_state['guesses'].clear()
                guesses_result_local.clear()
                st.session_state['num'] = random.randint(1,20)
                
                print("New random number is ",st.session_state['num'])
            
            st.write(result)
            print("Answer:", st.session_state['num'])
            st.write("Guesses so far:")
            guesses_string=", ".join(str(x) for x in st.session_state['guesses'])
            st.write(guesses_string)

            guesses_result_local.clear()
            # lets use the st.session_state['guesses'] variable to calculate the guesses result
            for guess_value in st.session_state['guesses']:
                if guess_value > st.session_state['num']:
                    guesses_result_local.append("Too High")
                elif guess_value < st.session_state['num']:
                    guesses_result_local.append("Too Low")
                else:
                    guesses_result_local.append("Correct")
                
            #To get rid of correct from the final result string
            if "Correct" in guesses_result_local:
                guesses_result_local.remove("Correct")
            
            guesses_result_string=", ".join(str(x) for x in guesses_result_local)

            st.write(guesses_result_string)

    