#main.py
import streamlit as st
from PIL import Image  # For image handling

logo = Image.open("credit_risk.jpg")
# Initialize session state for page and data
if "page" not in st.session_state:
    st.session_state.page = "Home"
if "uploaded_file" not in st.session_state:
    st.session_state.uploaded_file = None

# Sidebar Navigation and File Uploader (Persistent across all pages)
with st.sidebar:
    st.image(
        logo,
        use_container_width=True,  # Adjusts image to sidebar width
        caption="Credit Risk Analysis"
    )
    st.divider()
    st.title("Navigation")
    page = st.radio("Go to",["Home","Data Summary","Exploratory Analysis","Modelling","Output and Actions"],key = "Nav_Radio")
    st.title("Data Upload")
    uploaded_file = st.file_uploader("Please upload your data here",type = ["csv"],key = "file_uploader")

# Update session with state with the selected page and uploaded file
st.session_state.page = page
if uploaded_file is not None :
    st.session_state.uploaded_file = uploaded_file
    st.sidebar.success("File Uploaded Successfully!!!")
else:
    st.sidebar.info("Please upload a CSV file to proceed")

# Dynamically Render the selected page
if st.session_state.page == "Home":
    from pages import Home as home_page
elif st.session_state.page == "Data Summary":
    from pages import Data_Summ as home_page
elif st.session_state.page == "Exploratory Analysis":
    from pages import EDA as home_page
elif st.session_state.page == "Modelling" :
    from pages import Model_Dashboard as home_page
elif st.session_state.page == "Output and Actions":
    from pages import Output_Actions as home_page

# Call the show() function of the selected page
home_page.show()
