# pages/5_Output_Actions.py
import streamlit as st

def show():
    st.title("Output & Actions")
    st.header("Generate Predictions and Recommendations")

    if 'uploaded_file' in st.session_state:
        st.write("### Risk Predictions")
        st.write("Display default probabilities and risk tiers for each customer.")

        st.write("### Actionable Insights")
        st.write("Provide recommendations like 'Approve', 'Reject', or 'Further Review'.")

        st.write("### Download Reports")
        st.write("Allow users to download predictions and insights as CSV/PDF.")
    else:
        st.warning("Please upload a dataset from the sidebar to proceed.")