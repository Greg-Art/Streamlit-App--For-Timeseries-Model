import streamlit as st
import numpy as np
import pandas as pd
import pickle as pk 

##adding my title

st.title("This is a Time Forecasting App with Facebook Prophet")

##adding my description 

st.markdown("This app predicts daily sales across all Favorita Stores")



## a plot of the Daily sales for favorita
df_ori= pd.read_csv("models/original_dataframe.csv")
df_ori= df_ori.set_index("date")
st.subheader("A Chart of the Daily Sales Across Favorita Stores")
st.line_chart(df_ori["sales"])

##showing the user a sample dataframe they should have 
df_sample= pd.read_csv("models/test.csv")
df_sample= df_sample.drop("Unnamed: 0", axis=1)
st.subheader("This should be the format of your input: y is your sales, ds is your date")
st.dataframe(df_sample)
