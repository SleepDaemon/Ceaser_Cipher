import streamlit as st
from PIL import Image
import numpy as np

lst = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def decoder(sentence, key):
    decoded_string = ""
    for j in range(len(sentence)):
        if sentence[j] == " ":
            decoded_string += " "
            continue
        for i in range(len (lst)):
            if sentence[j] == lst[i]:
                code_location = i - key
                if code_location < 0:
                    code_location = code_location + 52
                decoded_string += lst[code_location]
    return decoded_string

def app():
    display = Image.open('decoded.webp')
    display = np.array(display)
    st.image(display)
    header=st.container()
    result_all = st.container()
    with header:
        sentence= st.text_input("Text to be decrypted")
        key= st.text_input("Enter the key",value="0")
        key= int(key)
        decoded=decoder(sentence, key)
        # st.write(encoded)
        print (decoded)
        st.write("Decrypted Text:",decoded)
       