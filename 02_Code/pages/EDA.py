# pages/3_EDA.py
import streamlit as st


def show():
    st.title("Exploratory Data Analysis (EDA)")
    st.header("Explore Trends and Correlations")

    if st.session_state.uploaded_file:
        st.write("### Uploaded Dataset Stats")
        import pandas as pd
        df = pd.read_csv(st.session_state.uploaded_file)
        st.write(df.describe())

        st.write("### Visualizations")
        st.write("Add interactive charts and filters here.")
    else:
        st.warning("Please upload a dataset from the sidebar to proceed.")