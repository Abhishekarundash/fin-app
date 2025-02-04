# pages/2_Data_Prep.py
import streamlit as st

st.title("Data Preparation")
st.header("Upload and Clean Your Data")

if 'uploaded_file' in st.session_state:
    st.write("### Uploaded Dataset Preview")
    # Load and display the dataset
    import pandas as pd
    data = pd.read_csv(st.session_state['uploaded_file'])
    st.write(data.head())

    st.write("### Data Cleaning Options")
    st.write("Handle missing values, outliers, and feature engineering here.")
else:
    st.warning("Please upload a dataset from the sidebar to proceed.")