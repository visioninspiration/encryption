import streamlit as st
from modules.AES import encryption, decryption

st.write("# Encryption")
text = st.text_area("Write the text to encrypt")
password = st.text_input("Write your password")
if st.button("Encrypt"):
    encoded = encryption(text, password)
    st.text_area("Encrypted Text: ", value=encoded)
