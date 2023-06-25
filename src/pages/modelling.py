## libraries importation
##data handling 
import pandas as pd 
import numpy as np
###encoders and model
from prophet import Prophet
from sklearn.preprocessing import LabelEncoder 
from sklearn.preprocessing import OrdinalEncoder
from category_encoders import BinaryEncoder
##error metrics 
from sklearn.metrics import mean_absolute_error as MAE
from sklearn.metrics import mean_squared_log_error as MSLE
from sklearn.metrics import mean_squared_error as MSE
from statsmodels.tools.eval_measures import rmse
##visualization and webapp
import plotly.express as ex
import plotly.offline as po
from prophet.plot import plot_plotly, plot_components_plotly 
import streamlit as st
import matplotlib.pyplot as plt 
import seaborn as sns 

##model loading
import joblib 

###importing my dataset

##our train
train= pd.read_csv("dataframes/train.csv")
train= train.drop("Unnamed: 0", axis=1)
train_target= train[["y"]]

##getting our test with target

t_w_target= pd.read_csv("dataframes/test_with_y.csv")

##filtering out our y

test= pd.read_csv("dataframes/test.csv")
test_target= t_w_target[["sales"]]



##creating a copy of my train

train_copy= train.copy()


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

model=Prophet(yearly_seasonality= True, seasonality_mode= "multiplicative", seasonality_prior_scale=25)

##stating my exogenous variables (extra regressors)
exo_cols=[ 'holiday_0', 'holiday_1', 'holiday_2', 'locale', 'transferred', 'onpromotion', 'transactions']

for cols in exo_cols:
        model.add_regressor(cols, standardize=True)

##concating my train features with my train target to allow me fit

full_train= pd.merge(left= train, right= train_target,left_index=True, right_index=True)

full_train

##fitting out data on the full train
model.fit(full_train)


##let's make a prediction on our test

###before that I will make a copy of my test sample 

test_features= test.copy()

test_features= test_features.drop("Unnamed: 0", axis= 1)

test_features
##rename the date column

test_features= test_features.rename(columns= {"date": "ds"})

##using my binary encoder to transform it
##transforming my test 
test_features[["locale"]]= OE.transform(test_features[["locale"]])

test_features["transferred"]= LE.transform(test_features["transferred"])
test_features= BE.transform(test_features)

test_features
##making predictions on my test data

eval_fbp= model.predict(test_features)

##filtering out my yhat to let me calculate my error metrics
eval= eval_fbp[["yhat"]]

##error metrics 
## i will be evaluating the model's performance using MAE, MSE, and RMSLE

mean_abs_err= (MAE(eval,test_target)/test_target.mean())*100

rmsle= np.sqrt(MSLE(eval,test_target))

rmse=np.sqrt(MSE(eval,test_target))

rmsle
mean_abs_err
rmse
###Our model is working well, so we will go ahead and dump the various components
final_results= pd.DataFrame({"MAE":mean_abs_err, "RMSLE": rmsle, "RMSE":rmse })
final_results

##plotting my outcome
model.plot(eval_fbp)
plt.show()

### I am going to drop my prophet and thhen 


"""in this section, I am going to drop the holidays column and then use the inbuilt Facebook Prophet Holiday 
feature
"""
##loading my dataframes again

##dropping the holiday columns for the new training dataframe
train_2= train_copy.drop(columns= ["holiday", "locale", "transferred"], axis= 1)

train_2
##dropping the holiday columns for the new test dataframe

test_2= test.drop(columns= ["Unnamed: 0","holiday", "locale", "transferred"], axis= 1)

test_2

train_2

##instatiating my model

model_2= Prophet(yearly_seasonality= True,
                 seasonality_mode= "multiplicative", seasonality_prior_scale=25)

##adding the holiday effect 
model_2.add_country_holidays(country_name= "ECU")

##adding my regressors (exogenous variables)

for col in train_2.drop(columns=["ds", "y"], axis= 1):
    model_2.add_regressor(col, standardize=True, prior_scale=20)


model_2.fit(train_2)

eval_2_fbp=model_2.predict(test_2)

##getting my predicted values 

eval_2= eval_2_fbp[["yhat"]]

##evaluating my model's performance

mae_2= (MAE(test_target,eval_2)/test_target.mean()) * 100

rmsle_2= np.sqrt(MSLE(test_target,eval_2))

rmse_2= np.sqrt(MSE(test_target,eval_2))

final_error_2= pd.DataFrame({"MAE":mae_2, "RMSLE": rmsle_2, "RMSE":rmse_2 })

final_error_2

final_results

model_2.plot_components(eval_2_fbp)
model_2.plot(eval_2_fbp)
plt.show()

""" our second model with embedded holiday effects did pretty well by giving us a much lower rmsle than our 
initial model where we used had to hard-encode our holiday effect
"""
##saving my Facebook Prophet model
joblib.dump(model_2,"C:/Users/Gregory Arthur/Desktop/models/fbpmodel.joblib")

"""
Note: Since we used facebook prophet's inbuilt holiday effect, we will not need to save any of the encoders
"""