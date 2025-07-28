import streamlit as st
import pandas as pd
# import numpy as np
# import os

# load data
data = pd.read_csv('tips.csv')


def display_data_random(df):
    sample = df.sample(5)
    return sample


# Button Widget
st.header('Displaying Data with Button')
st.caption('Click the button to display data!')
button = st.button('Display Data')
# st.write(f'button = {button}')

if button:
    sample = display_data_random(data)
    st.dataframe(sample)
