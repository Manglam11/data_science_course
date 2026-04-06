import streamlit as st
import datetime
from dateutil.relativedelta import relativedelta

st.title("Welcome to Streamlit age calculator")

user_dob = st.date_input("Enter you date of birth:",
                         min_value=datetime.date(1900, 1,1),
                         max_value=datetime.date.today())
if user_dob:
    st.write(f"Your selected dob is {user_dob}")

today = datetime.date.today()
if today:
    st.write(f"Today's date {today}")

age = relativedelta(today, user_dob)

if age:
    st.write(f"Your age is: {age.years} years, {age.months} months, {age.days}days")
    st.success("The process is executed with code 0.")