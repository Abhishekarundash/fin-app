import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    st.title("📈 Exploratory Data Analysis")

    if "uploaded_file" in st.session_state:
        df = pd.read_csv(st.session_state["uploaded_file"])
        
        st.write("### Data Head")
        st.write(df.head())
        
        st.write("### Missing Values")
        st.write(df.isnull().sum())
        
        st.write("### Correlation Heatmap")
        plt.figure(figsize=(10, 5))
        sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
        st.pyplot(plt)
    else:
        st.warning("Please upload a CSV file from the sidebar.")

if __name__ == "__main__":
    main()
