# pages/2_Data_Prep.py
import streamlit as st

def show():
    st.title("Data Preparation")
    st.header("Upload and Clean Your Data")
    if st.session_state.uploaded_file:
        st.write("### Uploaded Dataset Stats")
        import pandas as pd
        df = pd.read_csv(st.session_state.uploaded_file)
        st.write(df.head())
    else:
        st.warning("No dataset uploaded yet.")

