# pages/home.py
import streamlit as st
from PIL import Image  # For image handling

def show():
    st.title("Credit Risk Modeling App Overview")
    st.header("Home")
    st.subheader("Data Summary --> EDA --> Modelling --> Output Analysis")

    # Loan images from the docs folder
    image1 = Image.open("docs/data_summary.png")
    image2 = Image.open("docs/eda.png")
    image3 = Image.open("docs/modelling.png")
    image4 = Image.open("docs/output_analysis.png")

    ## Creating a 2*2 Layout using columns
    col1,col2 = st.columns(2)

    with col1:
        st.image(image1,caption="Data Summary",use_container_width=True)
    with col2:
        st.image(image2,caption="Exploratory Data Analysis",use_container_width=True)

    col3,col4 = st.columns(2)

    with col3:
        st.image(image3,caption = "Modelling",use_container_width=True)
    with col4:
        st.image(image4,caption = "Output Analysis", use_container_width= True)


### Ensure the script only runs when executed

if __name__ == "__main__":
    show()

    
