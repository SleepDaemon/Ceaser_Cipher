import streamlit as st
from PIL import Image
import numpy as np

List_hints=[]

def alpha_beta_gamma_checker(user_guess):
    hints=[]

    #Alpha Check
    for i in range(len(st.session_state['AlphaBetaGamma_list'])):
        if st.session_state['AlphaBetaGamma_list'][i] == user_guess[i]:
            hints.append("Alpha")

    #Beta Check
    for i in range(len(user_guess)):
        for j in range(len(st.session_state['AlphaBetaGamma_list'])):
            if i !=j:
                if user_guess[i] == st.session_state['AlphaBetaGamma_list'][j]:
                    hints.append("Beta")

    #Gamma Check
    for i in range(len(user_guess)):
        digit_absent=True
        for j in range(len(st.session_state['AlphaBetaGamma_list'])):
                if user_guess[i] != st.session_state['AlphaBetaGamma_list'][j]:
                    digit_absent=digit_absent&True
                else:
                    digit_absent=digit_absent&False
        if digit_absent:
            hints.append("Gamma")
    return hints

def app():
    st.title("Alpha Beta Gamma")
    st.text("Guess 3 digit number")
    display = Image.open('alphabetagamma.png')
    display = np.array(display)
    st.image(display)
    instruction_container=st.container()


    header=st.container()
    solutions=st.container()

    with instruction_container:
        st.header("AlphaBetaGamma Instructions")
        st.text("I am thinking of a 3-digit number. Try to guess what it is. ,")
        st.text('''The clues I give are...
When I say:    That means:
  Gamma       None of the digits is correct.
  Beta         One digit is correct but in the wrong position.
  Alpha        One digit is correct and in the right position.''')
        st.text("I have thought up a number.")
    
    with header:
        user_guess= st.text_input("Enter your Guess (3-digit)",value="")
        global List_hints

        if user_guess!="" and len(user_guess)==3:
            print(user_guess)
            st.session_state['AlphaBetaGamma_guesses'].append(user_guess)
            print("Guesses Till now", st.session_state['AlphaBetaGamma_guesses'])
            List_hints=[]
            for user_guess in st.session_state['AlphaBetaGamma_guesses']:
                hints=alpha_beta_gamma_checker(user_guess)
                List_hints.append(hints)
            print("Hints Till now", List_hints)
    
    with solutions:
        st.header("Solutions")

        for i in range( len(List_hints)):
            List_hints_string=", ".join(str(x) for x in List_hints[i])

            st.write(st.session_state['AlphaBetaGamma_guesses'][i], List_hints_string)