import streamlit as st
import numpy as np
import pandas as pd
import joblib 
from datetime import date
from prophet.plot import plot_plotly, plot_components

##adding my title
st.title("Favorita Store Sales Prediction App with Facebook Prophet")
    ##adding my description 
st.markdown("On this Page you can predict daily sales across all Favorita Stores")

##loading my model again

model= joblib.load("C:/Users/Gregory Arthur/Desktop/models/fbpmodel.joblib")

##loading my test data

test=pd.read_csv("dataframes/test.csv")

test=test.drop(["holiday", "locale", "transferred"], axis= 1)

result= model.predict(test)

##defining my inputs 
st.header("Make a Forecast Here: ")
ds= st.date_input(label= "Please enter the date you want to forecast")
transactions= st.number_input(label= "Please enter the total number of expected transactions")
onpromotion= st.number_input(label= "Please enter the total number of expected items to be on promotions")

##creating a dataframe for my inputs 

input_data= [ds, onpromotion, transactions]
inputs= pd.DataFrame([input_data], columns=["ds", "onpromotion", "transactions"])
forecast= model.predict(inputs)

##creating an output for my output
st.header("Your Prediction is Displayed Below: ")

##telling my model to return the yhat of my input
st.write(forecast["yhat"])
