import streamlit as st

st.title("Campaign Intelligence Assistant")

st.write("Upload campaign data to analyze performance.")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    st.success("File uploaded successfully")
    st.write("Processing will be added in next phase...")