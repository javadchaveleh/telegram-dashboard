import streamlit as st
import numpy as np
import seaborn as sns


with st.sidebar.form('Login'):
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')

    submitted = st.form_submit_button('Login')
    if submitted:
        pass

st.title(":zap: Telegram Dashboard")
# banner = Image.open("./data/banner.jpg")
# st.image(banner)
with st.expander("User Profile"):
    col1, col2 = st.columns(2)
    col1.text_input('First Name:')
    col2.text_input('Last Name:')
    st.camera_input("Take a picture")


