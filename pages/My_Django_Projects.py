import streamlit as st
import pandas as pd

df = pd.read_csv("django_data.csv", sep=";")

st.set_page_config(layout="wide")
# create two columns
col1, col2 = st.columns(2)

with col1:
    st.image("django_images/maxresdefault.jpg")

with col2:
    st.title("My Django Projects")
    content="""This is a webpage showcasing some of the django projects that I have worked on. Almost all of these 
    projects are created using Django, Bootstrap5, JavaScript, HTML, CSS, and Jinja2"""
    st.info(content)
st.write("Note: I am only showing a picture of the homepage of the website and sharing the source code. Only some of "
         "these projects are deployed. If the projects are deployed, I might add a link to the website in the future.")

col3,empty_col, col4 = st.columns([1.5,.5,1.5])

with col3:
    for index, row in df[:3].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("django_images/" + row["image"])
        st.write("[Source Code]({})".format(row["url"]))

with col4:
    for index, row in df[3:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("django_images/" + row["image"])
        st.write("[Source Code]({})".format(row["url"]))
