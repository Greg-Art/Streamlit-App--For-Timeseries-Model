## libraries importation
import streamlit as st
import pandas as pd 
import numpy as np
from prophet import Prophet
from sklearn.preprocessing import LabelEncoder 
from sklearn.preprocessing import OrdinalEncoder
from category_encoders import BinaryEncoder

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
df_sample= pd.read_csv("models/test.csv")
df_sample= df_sample.drop("Unnamed: 0", axis=1)
st.subheader("This should be the format of your input: y is your sales, ds is your date")
st.dataframe(df_sample)

train= pd.read_csv("models/train.csv")
train= train.drop("Unnamed: 0", axis=1)

##creating a copy of my train

train_copy= train.copy()
##model deployment

st.header("Prediction with Facebook Prophet")

## data encoding

##importing my binary encoder
BE= BinaryEncoder(cols= "holiday")

##fitting and transforming my train dataset

train= BE.fit_transform(train)

##instatiating and using my ordinal encoder
##creating a rank
rank= ["National", "Regional", "Local", "Not Holiday"]
OE= OrdinalEncoder(categories=[rank])
train[["locale"]]=OE.fit_transform(train[["locale"]])

##finally my label encoder 
LE= LabelEncoder()
##transforming our train
train["transferred"]=LE.fit_transform(train["transferred"])

##loading my train set again

train.head()

##everything has works so let's fit our model once again

model=Prophet(interval_width= 0.95, yearly_seasonality= True,seasonality_mode= "multiplicative", seasonality_prior_scale=20 )

##stating my exogenous variables (extra regressors)
exo_cols=[ 'holiday_0', 'holiday_1', 'holiday_2', 'locale', 'transferred', 'onpromotion', 'transactions']

for cols in exo_cols:
    model.add_regressor(cols, standardize= True)

model.fit(train)

##let's make a prediction on our test

df_sample



