import streamlit as st
from modules.AES import encryption, decryption

st.write("# Decryption")
encrypted_text = st.text_area("Write the base64 text to decrypt")
password = st.text_input("Write your password")
if st.button("Decrypt"):
    original = decryption(encrypted_text, password)
    st.write("Decrypted Text: ")
    st.write(f"{original}")
