import streamlit as st

st.title("My First App")

name = st.text_input("What's your name?")
if name:
    st.write(f"Hello, {name}!")

name2 = st.text_input("What's your name2?")
if name2:
    st.write(f"Hello, {name2}!")