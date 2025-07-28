import streamlit as st
import pandas as pd
import time

# Layout
side_bar = st.sidebar

side_bar.header("A Side Bar with st.sidebar")
side_bar.caption("Side bar items")
st.write("This is the Main Page")

# load and diesplay tips.csv
df = pd.read_csv('tips.csv')
# st.dataframe(df)

columns = tuple(df.columns)

# create widget select box
select_column = side_bar.selectbox(
    "Select the column you want to display",
    columns
)

side_bar.write("You selected the column name = {}".format(select_column))

# display the datafrane
st.dataframe(df[[select_column]])


# layout columns
st.header("Columns: st.columns")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Column 1")
    st.image("image.jpg")

with col2:
    st.subheader("Column 2")
    st.dataframe(df)

with col3:
    st.subheader("Column 3")
    st.dataframe(df[[select_column]])


# expander layout
st.header('Expander: st.expander')
with st.expander('Some Explanation'):
    st.write("""
    This is some information about the expander.
    """)


# Loyout Containers
st.subheader('Containers: st.container')
with st.container():
    st.write('You are inside a container')


# Empty Laout
st.subheader('Empty: st.empty')
placeholder = st.empty()

for i in range(1, 11):
    placeholder.write('This message will disappear in {} seconds.'.format(10-i))
    time.sleep(1)

placeholder.empty()
