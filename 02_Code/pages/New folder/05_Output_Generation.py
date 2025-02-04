import streamlit as st
import pandas as pd

def main():
    st.title("📤 Output Generation")

    if "uploaded_file" in st.session_state:
        df = pd.read_csv(st.session_state["uploaded_file"])
        st.write("### Final Predictions")
        st.write(df.sample(10))  # Placeholder for actual predictions
    else:
        st.warning("Please upload a CSV file from the sidebar.")

if __name__ == "__main__":
    main()
