import streamlit as st 
from joblib import load 


model = load('./salary_food_model.joblib')

st.title("Test Predict")

income = st.number_input("Enter: ")

predict_but = st.button("Predict")

if predict_but:
    input_data = [[income/1000]]
    
    prediction = model.predict(input_data)
    
    st.write(prediction*100)