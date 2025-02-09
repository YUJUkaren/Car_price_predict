import streamlit as st
import pickle 
import pandas as pd 


st.title('Car Price Prediction in India')
st.write('This wed app predicts the **Car Price** in India')

model= pickle.load(open('model_uu.pkl','rb'))

name=st.text_input('Name')
location=st.text_input('Location')
year=st.text_input('Year')
kilo_driven=st.number_input('Kilometers Driven')
fuel_type=st.number_input('Fuel Type')
transmission=st.number_input('Transmission')
owner_type=st.number_input('Owner Type')
mileage=st.number_input('Mile Age')
engine=st.number_input('Engine')
power=st.number_input('Power')
seats=st.number_input('Seats')

user_data=pd.DataFrame({'Name':name,
'Location':location,
'Year':year,
'Kilometers Driven':kilo_driven,
'Fuel Type':fuel_type,
'Transmission':transmission,
'Owner Type':owner_type,
'Mile Age':mileage,
'Engine':engine,
'Power':power,
'seats':seats}, index=[0])

prediction=model.predict(user_data)
if st.button('Predict'):
    st.write(f'The predicted car price is {predicetion[0]*100000}')


