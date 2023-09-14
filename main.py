import streamlit as st

st.set_page_config(layout="wide")

# create two columns
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("David Zheng")
    content="""
    Hi, I am David. I am an applied Math graduate. I am interest in math, data, and programming. I am currently taking online classes and working on buliding my profolio.
    This is a simple webpage showcasing some of the apps that I created using Python as the primary language
    """
    st.info(content)
