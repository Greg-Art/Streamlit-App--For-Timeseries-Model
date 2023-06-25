import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt 

st.title("This is a page to Explore the EDA of Favorita Store")



##creating my web page 
   
df_ori= pd.read_csv("dataframes/original_dataframe.csv")
df_ori= df_ori.set_index("date")
st.subheader("A Chart of the Daily Sales Across Favorita Stores")
st.line_chart(df_ori["sales"])