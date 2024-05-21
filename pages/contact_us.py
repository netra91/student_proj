import streamlit as st
from send_email import send_mail
import pandas
df = pandas.read_csv("topic.csv")
st.header("Contact US")

with st.form(key="email_forms"):
    user_email = st.text_input("your email adress")
    user_topic = st.selectbox("what topic do you want to discuss", df["topic"])
    user_message = st.text_area("enter your message")
    message= f"""\
    
    Subject : new mail from {user_email}
    
    From : {user_email}
    Topic:{user_topic}
    {user_message}"""
    button = st.form_submit_button("submit")
    if button:
        send_mail(message)
        st.info("your email was sent successfully")
