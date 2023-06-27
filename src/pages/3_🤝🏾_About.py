import streamlit as st
from st_functions import st_button, load_css
from PIL import Image
import sys

sys.path.append('/src') ##appending my src path so that I can import a function from another py file

st.title("Learn More About Me:") ## my title 

load_css()   ##loading css customizations from st_function file 

col1, col2, col3 = st.columns(3)
col2.image(Image.open('src/dp.PNG'))   ##loading my image

st.header('Gregory Arthur: The Data Guy')

st.info('Volunteer, Data Analyst, Aspiring Data Engineer with an interest in Data Science and Finances')

icon_size = 20

st.subheader("I Can Help Your Business To: ")

st.write("""
- Perform descriptive analysis to extract valuable insights from your business' dataset.
- Develop regression, time series, and classification models for accurate predictions and forecasting.
- Build visually appealing dashboards displaying KPIs and business metrics for easy assimilation.

""")

st.subheader("Connect With Me: ")

st_button('medium', 'https://medium.com/@gregoryarthur98', 'Read my Blogs', icon_size)
st_button('github', 'https://github.com/Greg-Art', 'Checkout My Respoitories', icon_size)
st_button('linkedin', 'https://www.linkedin.com/in/gregory-kwaku-arthur-b68a28252/', 'Follow me on LinkedIn', icon_size)
st_button('mail', 'gregoryarthur98@gmail.com', 'Send me a mail', icon_size)
