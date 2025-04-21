import streamlit as st

st.title("My First App")

name = st.text_input("What's your name?")
if name:
    st.write(f"Hello, {name}!")

add = 2 + 2 

st.write("2 + 2 = ")
st.write(add)