import streamlit as st
import numpy as np
import pandas as pd

df = pd.read_csv('tips.csv')

# st.dataframe to display a Pandas dataframce
st.header("st.dataframe")
st.caption("Display a dataframe as an interactive table")

st.dataframe(data=df, width=500, height=500)

# st.table
st.header("st.table")
st.caption("Display a static table")

st.table(data=df.head())

# st.json
st.header("st.json")
st.caption("Display object of formated json string")

json_values = df.head(3).to_dict()

st.json(json_values)
