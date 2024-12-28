import streamlit as st
import pickle
import pandas as pd

model_path = 'xgboost_model.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

st.title("Heart Disease Predictor")


GENDER = st.number_input("GENDER", min_value=0, max_value=120, value=30)
AGE = st.selectbox("AGE", options=[0, 1], format_func=lambda x: "Female" if x == 0 else "Male")
SMOKING = st.selectbox("Chest Pain Type", options=[1,2], format_func=lambda x: ["chekadi", "chekmaydi", "Non-anginal][x])
trestbps = st.number_input("Resting Blood Pressure (mm Hg)", min_value=0, max_value=300, value=120)
chol = st.number_input("Serum Cholesterol (mg/dl)", min_value=0, max_value=600, value=200)
YELLOW_FINGERS = st.selectbox("Fasting Blood Sugar > 120 mg/dl", options=[0, 1], format_func=lambda x: "False" if x == 0 else "True")
ANXIETY = st.selectbox("Resting Electrocardiographic Results", options=[0, 1], format_func=lambda x: ["Normal", "ST-T wave abnormality"][x])
PEER_PRESSURE = st.selectboxput("Maximum Heart Rate Achieved", , options=[0, 1], format_func=lambda x: ["Normal", "ST-T wave abnormality"][x])
CHRONIC DISEASE	 = st.selectbox("Exercise-CHRONIC DISEASE	", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
WHEEZINGk = st.selectbox("ST Depression", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
ALCOHOL CONSUMING = st.selectbox("Slope of the Peak Exercise ST Segment", options=[0, 1], format_func=lambda x: ["Upsloping", "Flat"][x])
COUGHING = st.selectbox("Number of Major Vessels Colored by Fluoroscopy", options=[0, 1])
SHORTNESS OF BREATH = st.selectbox("Thalassemia", options=[1, 2], format_func=lambda x: ["Normal", "Fixed defect"][x - 1])
SWALLOWING DIFFICULTY = st.selectbox("ST Depression", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
CHEST PAIN = st.selectbox("ST Depression", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")

if st.button("Predict Heart Disease"):
    user_input = [
        AGE, SMOKING, YELLOW_FINGERS, ANXIETY, PEER_PRESSURE, CHRONIC DISEASE, WHEEZING, ALCOHOL CONSUMING, COUGHING, SHORTNESS OF BREATH, SWALLOWING DIFFICULTY, CHEST PAIN
    ]

   
    features = [
        "AGE", "SMOKING", "YELLOW_FINGERS", "ANXIETY", "PEER_PRESSURE","CHRONIC DISEASE", "WHEEZING", "ALCOHOL CONSUMING", "COUGHING","SHORTNESS OF BREATH", "SWALLOWING DIFFICULTY", "CHEST PAIN"
    ]
    input_df = pd.DataFrame([user_input], columns=features)

 
    result = model.predict(input_df)

 
    if result[0] == 1:
        st.warning("Prognoz: o`pka saraton kasalligi xavfi yuqori!")
    else:
        st.success("Prognoz: o`pka saraton kasalligi xavfi past!")
