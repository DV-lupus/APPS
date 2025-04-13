import streamlit as st

st.title("👋 Hello App")

name = st.text_input("What is your name?")

if name:
    st.write(f"Hello, {name}!")
