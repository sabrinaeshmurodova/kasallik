import streamlit as st
import pickle
import pandas as pd

model_path = 'model.pkl'
with open(model, 'rb') as file:
    model = pickle.load(file)

st.title("saraton")


GENDER = st.number_input("GENDER", min_value=0, max_value=120, value=30)
AGE = st.selectbox("AGE", options=[0, 1], format_func=lambda x: "Female" if x == 0 else "Male")
SMOKING = st.selectbox("Chest Pain Type", options=[0,1], format_func=lambda x: ["chekadi", "chekmaydi"][x])
ANXIETY = st.selectbox("Resting Electrocardiographic Results", options=[0, 1], format_func=lambda x: ["Normal", "ST-T wave abnormality"][x])
PEER_PRESSURE = st.selectboxput("Maximum Heart Rate Achieved",options=[0, 1], format_func=lambda x: ["Normal", "ST-T wave abnormality"][x])
CHRONIC_DISEASE	 = st.selectbox("Exercise-CHRONIC DISEAS", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
ALCOHOL_CONSUMING = st.selectbox("Slope of the Peak Exercise ST Segment", options=[0, 1], format_func=lambda x: ["Upsloping", "Flat"][x])
COUGHING = st.selectbox("Number of Major Vessels Colored by Fluoroscopy", options=[0, 1])
SHORTNESS_OF_BREATH = st.selectbox("Thalassemia", options=[0, 1], format_func=lambda x: ["Normal", "Fixed defect"][x - 1])
CHEST_PAIN = st.selectbox("ST Depression", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")

if st.button("Predict Heart Disease"):
    user_input = [
        AGE, SMOKING, YELLOW_FINGERS, ANXIETY, PEER_PRESSURE, CHRONIC_DISEASE, WHEEZING, ALCOHOL_CONSUMING, COUGHING, SHORTNESS_OFBREATH, SWALLOWING_DIFFICULTY, CHEST_PAIN
    ]
    features = [
        "AGE", "SMOKING", "ANXIETY", "PEER_PRESSURE","CHRONIC_DISEASE", "ALCOHOL_CONSUMING", "COUGHING","SHORTNESS_OF_BREATH", "CHEST_PAIN"
    ]
    input_df = pd.DataFrame([user_input], columns=features)
    input_df = pd.DataFrame( columns=features)

    result = model.predict(input_df)


    if result[0] == 1:
        st.warning("Prognoz: o`pka saraton kasalligi xavfi yuqori!")
    else:
        st.success("Prognoz: o`pka saraton kasalligi xavfi past!")
