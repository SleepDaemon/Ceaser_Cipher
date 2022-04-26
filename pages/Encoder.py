import streamlit as st
lst = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encoder(sentence, key):
    encoded_string = ""
    for j in range(len(sentence)):
        if sentence[j] == " ":
            encoded_string += " "
            continue
        for i in range(len (lst)):
            if sentence[j] == lst[i]:
                code_location = i + key
                if code_location > 51:
                    code_location = code_location - 52
                encoded_string += lst[code_location]
    return encoded_string

def app():
    header=st.container()
    result_all = st.container()
    with header:
        sentence= st.text_input("Text to be encrypted")
        key= st.text_input("Enter the key",value="0")
        key= int(key)
        encoded=encoder(sentence, key)
        # st.write(encoded)
        print (encoded)
        st.write("Encrypted Text:",encoded)
       