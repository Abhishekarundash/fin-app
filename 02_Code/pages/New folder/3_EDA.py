# pages/3_EDA.py
import streamlit as st

st.title("Exploratory Data Analysis (EDA)")
st.header("Explore Trends and Correlations")

if 'uploaded_file' in st.session_state:
    st.write("### Dataset Overview")
    import pandas as pd
    data = pd.read_csv(st.session_state['uploaded_file'])
    st.write(data.describe())

    st.write("### Visualizations")
    st.write("Add interactive charts and filters here.")
else:
    st.warning("Please upload a dataset from the sidebar to proceed.")