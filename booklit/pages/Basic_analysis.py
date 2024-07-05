import streamlit as st
from src import utils
st.header("Book Summaries")

# get the books from kindleexports

#uploaded_raw_clips = st.file_uploader("Add your kindle clippings here")
raw_clips = utils.read_raw_clippings("src/My Clippings.txt")

st.multiselect("Select the books to see the summaries",options=["book2","book3"])
