import streamlit as st

# App Title
st.title("Your Title")

# Section Header
st.header("Main Header")

# Sub Header
st.subheader("This is a sub header")

# Markdown
st.markdown("This is some **markdown text**")
st.markdown("# Header 1")
st.markdown("## Header 2")
st.markdown("### Header 3")

# Caption
st.caption("This is a caption")

# Code Block
st.code(""" import pandas as pd
pd.read_csv('my_csv_file')
""")

# text
st.text("Some text for the app")

# Latex
st.latex("x = 2^3")

# Divider
st.text("Some text for the app, above the divider")
st.divider()
st.text("Some more text for the app, below the divider")

# st.write can take a lot of different parameters
st.write("Some text from st.write")
