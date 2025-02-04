import streamlit as st
from PIL import Image

# Set page config
st.set_page_config(
    page_title="Credit Risk Modeling App",
    page_icon="🔍",
    layout="wide"
)

# Sidebar
with st.sidebar:
    # Add Image Icon
    logo = Image.open("credit_risk.jpg")  # Ensure you have a logo file
    st.image(logo, use_column_width=True)

    # Navigation Links
    st.markdown("## Navigation")
    page = st.radio("Go to", ["Home", "Data Summary", "Exploratory Data Analysis", "Model Creation", "Output Generation"])

    # Data Upload Section
    st.markdown("---")
    st.markdown("## Upload Data")
    uploaded_file = st.file_uploader("Upload your dataset (CSV)", type=["csv"])

    # Store uploaded file in session state
    if uploaded_file is not None:
        st.session_state["uploaded_file"] = uploaded_file
        st.sidebar.success("File uploaded successfully!")

# Page routing
if page == "Home":
    st.title("🏠 Home Page")
    st.write("Welcome to the Credit Risk Modeling App.")
    st.write("Use the sidebar to navigate to different sections.")
    
elif page == "Data Summary":
    st.switch_page("pages/2_Data_Summary.py")

elif page == "Exploratory Data Analysis":
    st.switch_page("pages/3_EDA.py")

elif page == "Model Creation":
    st.switch_page("pages/4_Model_Creation.py")

elif page == "Output Generation":
    st.switch_page("pages/5_Output_Generation.py")
