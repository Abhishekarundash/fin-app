import streamlit as st
import pandas as pd

def main():
    st.title("📊 Data Summary")
    
    if "uploaded_file" in st.session_state:
        df = pd.read_csv(st.session_state["uploaded_file"])
        st.write("### Dataset Overview")
        st.write(df.head())
        st.write("### Summary Statistics")
        st.write(df.describe())
    else:
        st.warning("Please upload a CSV file from the sidebar.")

if __name__ == "__main__":
    main()
