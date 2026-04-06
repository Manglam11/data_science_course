import streamlit as st
st.title("Welcome to the world of programming")
st.subheader("Let's learn 0/1 language")

languages = st.selectbox("Choose you preferred lang: ",
             ["Python", "Java", "JavaScript", "C++"])
st.write(f"You choose {languages}, excellent choice!!")
st.success("Let's dive together")