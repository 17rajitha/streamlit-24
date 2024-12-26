import pandas as pd
import streamlit as st
#import datetime 
import pickle

cars_df=pd.read_csv("./cars24_data.csv")

st.write(
    """
    Cars24 Used Car Price Prediction
    """
)

st.dataframe(cars_df.head())
col1,col2=st.columns(2)
fuel_type=col1.selectbox("Select the fuel type",
             ["Diesel","Petrol","CNG","LPG","Electric"])
engine=col1.slider("Set the Engine Power",
                    500,5000,step=100)
seats=col2.selectbox("Enter the number of Seats",
                              [4,5,7,9,11])
transmission_type=col2.selectbox("Select the transmission type",
                   ["Manual","Automatic"])
encode_dict={    
    "fuel_type":{'Diesel':1,'Petrol':2,'CNG':3,'LPG':4,'Electric':5},
    "seller_type":{'Deler':1, 'Indvidual':2,'Trustmark Dealer':3},
    "transmition_type":{'Manual':1,'Automatic':2}
}    
def model_pred(fuel_type,transmission_type,engine,seats):
    with open('path/to/car_pred(1)','rb') as file:
        reg_model=pickle.load(file)
        input_features=[[2018,0,1,4000,fuel_type,\
                         transmission_type,19.70,engine,86.30,\
                            seats]]
        return reg_model.predict(input_features)
if (st.button("predict_price")):
    fuel_type = encode_dict['fuel_type'][fuel_type]
    transmission_type=encode_dict['transmition_type']\
      [transmission_type]
    price=model_pred(fuel_type,transmission_type,engine,seats)
    st.text(f"The price of the car {price[0],round(2)} lakhs rupees.")




