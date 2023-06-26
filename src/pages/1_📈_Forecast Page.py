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

model= joblib.load("models/fbpmodel.joblib")

##loading my test data

test=pd.read_csv("dataframes/test.csv")

test=test.drop(["holiday", "locale", "transferred"], axis= 1)

##testing my model 
result= model.predict(test)

##defining my inputs 
st.header("Make a Forecast Here: ")
ds= st.date_input(label= "Please enter the date you would want to forecast")
transactions= st.number_input(label= "Please enter the total number of expected transactions")
onpromotion= st.number_input(label= "Please enter the total number of expected items to be on promotions")

##creating a dataframe for my inputs 

input_data= [ds, onpromotion, transactions]
inputs= pd.DataFrame([input_data], columns=["ds", "onpromotion", "transactions"])
forecast= model.predict(inputs)
forecast_value= forecast["yhat"]
forecast_output = f"Your sales on {ds} will be ${forecast_value.values[0]:.2f}"

##I am creating an empty dataframe which will be displayed until the user clicks on submit
forecast_emp = forecast.applymap(lambda x: np.nan)
forecast_emp= forecast_emp.replace(np.nan,0)


##adding a button
output= st.button("Submit")


st.subheader("Your Sales Forecast is Displayed Below: ")

##telling my model to return the yhat if the submit button is clicked
if output:
    st.write(forecast_output)
else:
    st.write("Your sales on ...... will be .....")

st.subheader("Your Forecast Dataframe is Displayed Below: ")
##creating an output for my output
if output:
    st.write(forecast)
else:
    st.write(forecast_emp)