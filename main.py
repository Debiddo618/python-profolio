import streamlit as st

st.set_page_config(layout="wide")

# create two columns
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("David Zheng")
    content="""
    Hi, I am David. I graduated in 2021 with a Bachelor of Science in Applied Mathematics. I am currently taking online classes and working on building my profolio.
    """
    st.info(content)
st.write("Below you can find some of the apps I have built in Python. Feel free to contact me!")
