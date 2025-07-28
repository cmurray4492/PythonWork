import streamlit as st

# title
st.title("Using st.title() for  a title")
st.caption("This is a title caption")

# header
st.header("This is a header")
st.caption("This is a header caption")

# sub header
st.subheader("This is a sub-header")
st.caption("This is a subheader caption")

st.markdown("""---""")
st.subheader("Display Code")
# code
body = """
import numpy as np

print("Hello, World!")
"""
st.code(body, language='python')
