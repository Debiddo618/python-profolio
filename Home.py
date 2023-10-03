import streamlit as st
import pandas as pd

df = pd.read_csv("data.csv", sep=";")

st.set_page_config(layout="wide")
# create two columns
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("David Zheng")
    content="""Hi, I am David. I graduated in 2021 with a Bachelor of Science in Applied Mathematics from the 
    University of Maryland, College Park. I am currently taking online classes and working on building my profolio. ( 
    This is one of my favorite photos when I was traveling in Japan with my classmates from high school in 2019. I am 
    the guy in the middle wearing the dark blue yukata.)"""
    st.info(content)
st.write("Below you can find some of the apps I have built in Python. Note: Some of these apps are just fillers and "
         "are not implemented. They are used to fill in space and for the visual appearance of the webpage. Clicking "
         "on the source of filler projects will redirect you to https://pythonhow.com. The "
         "Contact Us page is full functional. Feel free to contact me!")

col3,empty_col, col4 = st.columns([1.5,.5,1.5])

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write("[Source Code]({})".format(row["url"]))

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write("[Source Code]({})".format(row["url"]))
