import streamlit as st

st.header("Pishing Domain Detection")
url = st.text_input(label="Enter the URL")

st.button(label="Check Pish or not")