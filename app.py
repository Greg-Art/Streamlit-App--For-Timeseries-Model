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


## a plot of the Daily sales for favorita
df= pd.read_csv("models/original_dataframe.csv")
df= df.set_index("date")
st.subheader("A Chart of the Daily Sales Across Favorita Stores")
st.line_chart(df["sales"])

##showing the user a sample dataframe they should have 
df_sample= pd.read_csv("models/sample.csv")
df_sample= df_sample.drop("Unnamed: 0", axis= 1)
st.subheader("This should be the format of your input: y is your sales, ds is your date")
st.dataframe(df_sample)

##model deployment

st.header("Prediction with Facebook Prophet")

##data encoding

