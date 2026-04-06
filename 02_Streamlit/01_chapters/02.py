import streamlit as st
st.title("Chai Maker App")

if st.button("Make Cahi"):
    st.success("Your chai is being brewed")

add_masala = st.checkbox("Add Masala")

if add_masala:
    st.write("Masala added to your chai.")

tea_type = st.radio("Pick you chai base: ",
                    ["Milk", "Water", "Sugar", "Our Special Masala"])
st.write(f"Selected base {tea_type}")

flavours = st.selectbox("Choose your flavour: ",
                        ["Ginger", "Black Paper", "Keasar", "Tulsi"])
st.write(f"Selected flavour {flavours}")

sugar_level = st.slider("Sugar level (in gm): ",
                        0, 50, 10)
st.write(f"Selected sugar level {sugar_level}")

cups = st.number_input("How many cups",
                       min_value=1, max_value=10, step=1)
st.write(f"Selected Cups {cups}")

name = st.text_input("Enter you name")
if name:
    st.write(f"Welcome {name}! Your chai is on the way.")

dob = st.date_input("Select you date of birth:")
st.write(f"Your date of birth is {dob}")















