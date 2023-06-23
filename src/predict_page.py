import streamlit as st
import numpy as np
import pandas as pd
import joblib 
from datetime import date
from prophet.plot import plot_plotly, plot_components

##loading my model again

model= joblib.load("C:/Users/Gregory Arthur/Desktop/models/fbpmodel.joblib")

##loading my test data

test=pd.read_csv("dataframes/test.csv")

test=test.drop(["holiday", "locale", "transferred"], axis= 1)

result= model.predict(test)


##creating my web page 


##adding my title
st.title("Favorita Store Sales Prediction APP with Facebook Propher")
    ##adding my description 
st.markdown("This app predicts daily sales across all Favorita Stores")
    
df_ori= pd.read_csv("dataframes/original_dataframe.csv")
df_ori= df_ori.set_index("date")
st.subheader("A Chart of the Daily Sales Across Favorita Stores")
st.line_chart(df_ori["sales"])
    

##defining my inputs 
st.header("Make a Forecast Here: ")
ds= st.date_input(label= "please enter the date you want to forecast")
transcations= st.number_input(label= "Please enter the total number of transactions to be run")
onpromotion= st.number_input(label= "Please enter the total number of promotions to be run")

##creating a fucntion for my inputs 

def input(ds, transactions, onpromotion):
    input_data= [ds, onpromotion, transactions]
    inputs= pd.DataFrame([input_data], columns=["ds", "onpromotion", "transactions"])
    return inputs

