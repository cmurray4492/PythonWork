import streamlit as st
import pandas as pd
import numpy as np

# display almost anythiong
# st.write

st.write("Hello, World!")
st.write("Welcome to Streamlit App API")
st.write(1234)

df = pd.DataFrame({
    "first_column": [1, 2, 3, 4],
    "second_column": [10, 20, 30, 40]
})

st.write(df)

# display a Numpy array
st.write(np.array([1, 2, 3, 4]))

# -------------------Magic ----------------------#
st.write("Magic Commands")

df1 = pd.DataFrame({'col': [1, 2, 3, 4]})
df1

x = 10
x
