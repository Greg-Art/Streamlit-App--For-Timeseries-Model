import streamlit as st

st.set_page_config(page_title="Welcome to Greg's Time Series Forecast App", 
                   page_icon="waving hands"
                   )

st.title("Welcome to My Homepage")
st.sidebar.success("Please Select the Page")

st.write("""Favorita Corporation is an Ecuadorian company that creates, 
         and invests in the commercial, industrial and real estate areas. 
         Its subsidiaries have activities in six countries in the region, 
         including Panama, Paraguay, Peru, Colombia, Costa Rica and Chile. 
         They offer the best products, services and experiences in an efficient,sustainable and responsible way 
         to improve the quality of life.In this app, 
         I will be using Facebook Prophet to Predict the Daily sales Across all Favorita Store""")
