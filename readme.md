# Creating a Web App for a Facebook Prophet Time Series Model 

The aim of this project is to deploy a time series regression analysis model. My model of choice was built using Facebook Prophet with external regressors (transaction and on promotions) and the in-built holiday effect feature of Facebook Prophet. 

- The model (Facebook Prophet) can be found in the model folder
- The source code can be found in the src folder
- The needed CSV files can be found in the data frames folder. 
- The Notebook folder contains the Notebook I used for my EDA and comparison of the model 
- I used the Virtualevn python environment



## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.txt file. 

```bash
pip install -r requirements.txt
```

## Usage

```python
import all the necessary library names. eg import Streamlit as st 

# run the app using the "Welcome.py" file
Streamlit run src/Welcome.py


```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate. Contact me via my email: gregoryarthur98@gmail.com
