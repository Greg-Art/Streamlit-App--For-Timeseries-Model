## libraries importation
import streamlit as st
import pandas as pd 
import numpy as np
from prophet import Prophet

##adding my title

st.title("This is a Time Forecasting App with Facebook Prophet")

##adding my description 

st.markdown("This app predicts daily sales across all Favorita Stores")

###importing my dataset
df= pd.read_csv("models/fbtest.csv")

df.head()
df.info()

##importing my model 
st.subheader("This is a sample dataframe")
st.dataframe(df.head())

##creating a plot with our time series 

