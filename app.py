import os

import streamlit as st

from src.pipeline.prediction import custom_final_df
from src.utils import load_object

st.header("Pishing Domain Detection")

pkl_file_path = os.path.join("artifacts", "model.pkl")

#loading pickle file
model = load_object(pkl_file_path)


#Input Column for the URL
url = st.text_input(label="Enter the URL")

if st.button(label="Check Pish or not"):
    custom_data = custom_final_df(url)
    df = custom_data.final_df()
    model.predict([[df]])