# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 19:24:02 2025

@author: Craig Murray
"""
# Recurrent Neural Networks - Google Stock Price
# Part 1- Data Preprocessing
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Importing the training set 
dataset_train = pd.read_csv('../Data/Google_Stock_Price_Train.csv')
training_set = dataset_train.iloc[:, 1:2].values

# Feature Scaling 
from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler(feature_range=(0, 1))
training_set_scaled = sc.fit_transform(training_set)

# Create a dataset with 60 timesteps - use data from 60 steps to predict.
X_train = []
y_train = []

for i in range(60, 1258):
    X_train.append(training_set_scaled[i-60:i, 0])
    y_train.append(training_set_scaled[i, 0])
    
X_train, y_train = np.array(X_train), np.array(y_train)

# Reshaping
X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))

# Part 2 - Building the RNN
# importing the Keras packages
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout

# Initialing the RNN 
regressor = Sequential()

# Adding the first LSTM layer and some Dropout regularization
regressor.add(LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1], 1)))
regressor.add(Dropout(0.2))




# Part 3 - Making the predictions and visualizing the results
