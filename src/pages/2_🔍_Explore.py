import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt 
from prophet.plot import plot_plotly, plot_components_plotly
import joblib
import plotly.express as px

##reloading my model

model_2= joblib.load("models/fbpmodel.joblib")

##loading my test
test=pd.read_csv("dataframes/test.csv")
test_target= pd.read_csv("dataframes/test_with_y.csv")

test= test.drop(columns=["Unnamed: 0", "holiday", "locale", "transferred"], axis= 1)

test_target= test_target[["sales"]]

test_target.columns= ["y"]


st.title("This is a page to Explore the EDA of Favorita Store")

##creating my web page 
df_ori= pd.read_csv("dataframes/original_dataframe.csv")
df_ori= df_ori.set_index("date")
st.subheader("A Chart of the Daily Sales Across Favorita Stores")
st.line_chart(df_ori["sales"])

##adding a visual of my model's forecast 

result= model_2.predict(test)

##plotting the  visualization of my model 
st.subheader("A Visualization of the Model's Evalaution")
fig= plot_plotly(model_2, result)
st.plotly_chart(fig)

##plotting the various componenets of the model
st.subheader("A Visualization of the Components of the Model's Prediction")
fig_2=model_2.plot_components(result)
st.write(fig_2)

