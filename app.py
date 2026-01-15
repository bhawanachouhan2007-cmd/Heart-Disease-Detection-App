import os 
import pickle
import streamlit as st
import numpy as  np

model_path = os.path.join(os.path.dirname(__file__),"Heart_model.pkl")
scaler_path = os.path.join(os.path.dirname(__file__),"scaler.pkl")
model = pickle.load(open(model_path, "rb"))
scaler = pickle.load(open(scaler_path,"rb"))
st.title(' ❤️ Heart Disease Prediction App')

age = st.number_input("Enter Age: " , 1 ,100)
gen = st.text_input("Enter Gender: ")
chol = st.number_input("Enter Cholesterol: ")
bp = st.number_input("Enter Blood Pressure: ")
smoke = st.text_input("Enter Smoking(Yes/No): ")
hr = st.number_input("Enter Heart Rate: ")
ai = st.text_input("Alcohol Intake (Heavy/Moderate/None): ")
di = st.text_input("Diabetes (Yes/No): ")
ob = st.text_input("Obesity (Yes/No):)")
ex = st.number_input("How many Hours do you Exercise ? ")
sl = st.number_input("What are your Stress Level (1-10) : ")
fh = st.text_input("Family History of Heart Disease (Yes/No): ")
e = st.text_input("Do you have Exercise Angina ? ")
p = st.text_input("Chest pain Type (Atypical Angina/ Typical Angina / Asymptomatic / Non-Anginal Pain): ")

if st.button("Predict"):
    data = np.array([[age , gen ,chol,bp,smoke,hr,ai,di,ob,ex,sl,fh,e,p]])
    result = model.predict(data)
    if result[0] == 1:
        st.error("⚠️ Heart Disease Detected")
    else :
        st.success("❤ No Heart Disease Detected")
