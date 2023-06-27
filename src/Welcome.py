import streamlit as st
import json
import requests
from streamlit_lottie import st_lottie ##to get animations from lottie web

##defining a function to dowload animation from Lottie Web
def load_lottiefile(url: str):
    r= requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

##downloading  the animation

lottie_hello= load_lottiefile("https://assets5.lottiefiles.com/packages/lf20_M9p23l.json")

##buidling my welcome page

st.set_page_config(page_title="Welcome to Greg's Time Series Forecast App", 
                   page_icon="👋"
                   )

st.title("Welcome To My Forecasting App for Favorita Corp.")

st_lottie(lottie_hello, height= 200) ##inserting my animation

st.sidebar.success("Please Select the Page") ##creating my sidebar 

st.write("""Favorita Corporation is an Ecuadorian company that creates, 
         and invests in the commercial, industrial and real estate areas. 
         Its subsidiaries have activities in six countries in the region, 
         including Panama, Paraguay, Peru, Colombia, Costa Rica and Chile. 
         They offer the best products, services and experiences in an efficient,sustainable and responsible way 
         to improve the quality of life. On this website, I will be using Facebook Prophet to Predict the Daily sales Across all Favorita Store""")

st.subheader("Things You Can Do On This Website: ")

st.write("""

- Forecast Sales of a Specific Date for Favorita Store
- Explore the Performance of the Model
- Get to Know More About Greg

""")
