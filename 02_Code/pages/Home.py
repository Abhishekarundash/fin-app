# pages/home.py
import streamlit as st

def show():
    st.title("Credit Risk Modeling App")
    st.header("Home")
    
    st.write("Welcome! Upload a CSV file to analyze auto loan credit risk.")
    
    if st.session_state.uploaded_file:
        st.write("### Uploaded Dataset Stats")
        import pandas as pd
        df = pd.read_csv(st.session_state.uploaded_file)
        st.write(f"Rows: {len(df)}, Columns: {len(df.columns)}")
    else:
        st.warning("No dataset uploaded yet.")