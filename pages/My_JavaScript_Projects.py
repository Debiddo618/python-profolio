import streamlit as st
import pandas as pd

df = pd.read_csv("javascript_data.csv", sep=";")

st.set_page_config(layout="wide")
# create two columns
col1, col2 = st.columns(2)

with col1:
    st.image("javascript_images/html-css-javascript.png")

with col2:
    st.title("My JavaScript Projects")
    content="""This page shows some mini frontend projects I built using vanilla JavaScript, HTML, and CSS while taking a
    course on Udemy by Brad Traversy. All projects are hosted on github. Feel free to click on the link to view the final results."""
    st.info(content)

col3,empty_col, col4 = st.columns([1.5,.5,1.5])

with col3:
    for index, row in df[:4].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("javascript_images/" + row["image"])
        st.write("[Link to Webpage]({})".format(row["url"]))

with col4:
    for index, row in df[4:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("javascript_images/" + row["image"])
        st.write("[Link to Webpage]({})".format(row["url"]))
