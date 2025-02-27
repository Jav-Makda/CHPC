# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 10:26:18 2025

@author: javer
"""
import streamlit as st
import pandas as pd

# Title of the app
st.title("Researcher Profile Page")

# Collect basic information
name = "Future Dr. Javeria Makda"
field = "Astrophysics"
institution = "University of the Witwatersrand"

# Display basic profile information
st.header("Researcher Overview")
pic = st.file_uploader("Upload a picture of yourself",type = "jpg")

col1, col2 = st.columns(2)
with col1:
    st.write(f"**Name:** {name}")
    st.write(f"**Field of Research:** {field}")
    st.write(f"**Institution:** {institution}")
with col2:
    if pic is not None:
        st.image(pic, width = 200)


# Add a section for publications
st.header("Publications")
uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")

if uploaded_file:
    publications = pd.read_csv(uploaded_file)
    st.dataframe(publications)

    # Add filtering for year or keyword
    keyword = st.text_input("Filter by keyword", "")
    if keyword:
        filtered = publications[
            publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
        ]
        st.write(f"Filtered Results for '{keyword}':")
        st.dataframe(filtered)
    else:
        st.write("Showing all publications")

# Add a section for visualizing publication trends
st.header("Publication Trends")
if uploaded_file:
    if "Year" in publications.columns:
        year_counts = publications["Year"].value_counts().sort_index()
        st.bar_chart(year_counts)
    else:
        st.write("The CSV does not have a 'Year' column to visualize trends.")

# Add a contact section
st.header("Contact Information")
email = "javeriamakda@gmail.com"
st.write(f"You can reach {name} at {email}.")
