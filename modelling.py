## libraries importation
import streamlit as st
import pandas as pd 
import numpy as np
from prophet import Prophet
from sklearn.preprocessing import LabelEncoder 
from sklearn.preprocessing import OrdinalEncoder
from category_encoders import BinaryEncoder
import joblib
from sklearn.metrics import mean_absolute_error as MAE
from sklearn.metrics import mean_squared_log_error as MSLE
from sklearn.metrics import mean_squared_error as MSE
from statsmodels.tools.eval_measures import rmse



###importing my dataset

##our train
train= pd.read_csv("models/train.csv")
train= train.drop("Unnamed: 0", axis=1)
##getting our test with target

target= pd.read_csv("models/test_with_y.csv")
##filtering out our y
test_target= target[["sales"]]

train_target= train[["y"]]

##creating a copy of my train

train_copy= train.copy()
##model deployment

st.header("Prediction with Facebook Prophet")

## data encoding

##importing my binary encoder
BE= BinaryEncoder(cols= "holiday")

##fitting and transforming my train dataset

train= BE.fit_transform(train.drop("y", axis=1))


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

##concating my train features with my train target to allow me fit

full_train= pd.merge(left= train, right= train_target,left_index=True, right_index=True)

full_train

##fitting out data on the full train
model.fit(full_train)


##let's make a prediction on our test

###before that I will make a copy of my test sample (df_sample)

features= df_sample.copy()

features
##rename the date column

features= features.rename(columns= {"date": "ds"})

##using my binary encoder to transform it

features[["locale"]]= OE.transform(features[["locale"]])

features["transferred"]= LE.transform(features["transferred"])
features= BE.transform(features)

features
##making predictions on my test data

eval_fbp= model.predict(features)

##filtering out my yhat to let me calculate my error metrics
eval= eval_fbp[["yhat"]]

##error metrics 
## i will be evaluating the model's performance using MAE, MSE, and RMSLE

mean_abs_err= (MAE(eval,test_target)/test_target.mean())*100

rmsle= np.sqrt(MSLE(eval,test_target))

rmse=np.sqrt(MSE(eval,test_target))

###Our model is working well, so we will go ahead and dump the various components

