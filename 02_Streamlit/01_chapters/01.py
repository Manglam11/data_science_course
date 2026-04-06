import streamlit as st

st.title("Hello Chai App")
st.subheader("Brewed with streamlit")
st.text("Welcome to your first interactive app")
st.write("Choose your fav. variety of chai")

chai = st.selectbox("Your fav chai: ", ["Masala Chai", "Lemon Tea", "Adrak Chai", "Kesar Chai"])
st.write(f"You choose {chai}, excellent choice!")
st.success("You chai has been brewed")