import streamlit as st

st.title("Chai Taste Poll")

col1, col2 = st.columns(2)

with col1:
    st.header("Masala Chai")
    st.image("masala_chai.jpeg", width=300)
    vote1 = st.button("Vote Masala Chai")

with col2:
    st.header("Adarak Chai")
    st.image("adarak_chai.jpg", width=200)
    vote2 = st.button("Vote Adrak Cahi")

if vote1:
    st.success("Thanks for voting Masala Chai")
elif vote2:
    st.success("Thanks for voting Adrak Cahi")


name = st.sidebar.text_input("Enter you name")
tea = st.sidebar.selectbox("Choose your chai",
                           ["Masala", "Adarak"])
if name:
        st.write(f"Welcome {name} chai is getting ready")

with st.expander("Show Chai Making Instructions"):
    st.write("""
    1. Boil water tea leaves
    2. Add milk and spice
    3. Thoda tadapne do...
    """)










