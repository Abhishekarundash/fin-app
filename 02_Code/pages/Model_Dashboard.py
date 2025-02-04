# pages/4_Model_Dashboard.py
import streamlit as st

def show():
    st.title("Model Dashboard")
    st.header("Train and Run the Risk Prediction Model")

    if st.session_state.uploaded_file:
        st.write("### Model Inputs")
        st.write("Select features and train the model here.")

        st.write("### Model Performance")
        st.write("Display evaluation metrics like ROC-AUC, precision, recall, etc.")
    else:
        st.warning("Please upload a dataset from the sidebar to proceed.")


