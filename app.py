import os 
import pickle
import streamlit as st
import pandas as pd 

model_path = os.path.join(os.path.dirname(__file__),"Heart_model.pkl")
scaler_path = os.path.join(os.path.dirname(__file__),"scaler.pkl")
model = pickle.load(open(model_path, "rb"))
scaler = pickle.load(open(scaler_path,"rb"))

st.title(' ❤️ Heart Disease Prediction App')
st.write("-----Enter Patient Details------ ")

age = st.number_input("Enter Age: " , 1 ,100)
gen = st.text_input("Enter Gender: ")
chol = st.number_input("Enter Cholesterol: ")
bp = st.number_input("Enter Blood Pressure: ")
smoke = st.selectbox("Enter Smoking:",["Yes","No"])
hr = st.number_input("Enter Heart Rate: ")
ai = st.selectbox("Alcohol Intake:", ["Heavy" , "Moderate", "None"])
di = st.selectbox("Diabetes:",["Yes","No"])
ob = st.selectbox("Obesity:",["Yes","No"])
ex = st.number_input("How many Hours do you Exercise ? ")
sl = st.slider("What are your Stress Level: " , 1 ,10)
fh = st.selectbox("Family History of Heart Disease : ",["Yes","No"])
e = st.selectbox("Do you have Exercise Angina ? ",["Yes","No"])
p = st.selectbox("Chest pain Type: ",["Atypical Angina","Typical Angina","Asymptomatic","Non-Anginal Pain"])

#Feature Alignment
feature_names = scaler.feature_names_in_
user_df = pd.dataframe(0,index=[0],columns=feature_names)

user_df['Age'] = age 
user_df['Cholestero'] = chol
user_df['Blood Pressure'] = bp
user_df['Heart Rate'] = heart_rate
user_df['Exercise Hours'] = exercise_hour
user_df['Stress Level'] = stress_level
user_df['Gender'] = 1 if gender == "Male" else 0 
user_df['Diabetes'] = 1 if diabetes == "Yes" else 0
user_df['Obesity'] = 1 if obesity == "Yes" else 0 
user_df['Family History'] = 1 of family_history == "Yes" else 0
user_df['Exercise Induced Angina'] = 1 if exercise_angina == "Yes" else 0

if smoking == "Yes" and "Smoking_Yes" in user_df.columns:
    user_df["Smoking_Yes"] = 1

if alcohol == "Heavy" and "Alcohol Intake_Heavy" in user_df.columns:
    user_df["Alcohol Intake_Heavy"] = 1
elif alcohol == "Moderate" and "Alcohol Intake_Moderate" in user_df.columns:
    user_df["Alcohol Intake_Moderate"] = 1

if chest_pain == "Atypical Angina" and "Chest Pain Type_Atypical Angina" in user_df.columns:
    user_df["Chest Pain Type_Atypical Angina"] = 1
elif chest_pain == "Non-anginal Pain" and "Chest Pain Type_Non-anginal Pain" in user_df.columns:
    user_df["Chest Pain Type_Non-anginal Pain"] = 1
elif chest_pain == "Asymptomatic" and "Chest Pain Type_Asymptomatic" in user_df.columns:
    user_df["Chest Pain Type_Asymptomatic"] = 1



if st.button("Predict"):
    scaled_input = scaler.transform(user_df)
    prediction = model.predict(scaled_input)
    probability = model.predict_proba(scaled_input)[0][1]
    
    if prediction[0] == 1:
        st.error("⚠️ Heart Disease Detected")
    else :
        st.success("❤ No Heart Disease Detected")

    if probability[0] > 0.7:
        st.error('High Risk')
    elif probability[0] > 0.4:
        st.warning('Medium Risk')
    else:
        st.success('Low Risk')
