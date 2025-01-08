import streamlit as st
mport streamlit as st
import pickle

st.set_page_config(page_title="Saraton Kasalligi Tashxisi", page_icon="🩺", layout="centered")

model_path = "model.pkl"
with open(model_path, 'rb') as file:
    model = pickle.load(file)

bio_features = [
    "ALB (Albumin)", "ALP (Alkaline Phosphatase)", "ALT (Alanine Transaminase)",
    "AST (Aspartate Transaminase)", "BIL (Bilirubin)", "CHE (Cholinesterase)",
    "CHOL (Cholesterol)", "CREA (Creatinine)", "GGT (Gamma-GT)", "PROT (Total Protein)"
]

result_mapping = {
    0: "Donor (Sog'lom)",
    1: "Gepatit (Jigar yallig'lanishi)",
    2: "Fibroz (Jigar to'qima o'zgarishi)",
    3: "Sirroz (Jigar yetishmovchiligi)",
    4: "Donor gumon qilinmoqda (Kasallik ehtimoli)"
}


st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to right top, #051937, #004d7a, #008793, #00bf72, #a8eb12);
        color: ##ffffff;
        font-family: 'Arial', sans-serif;
    }
 
    .main {
        background-color: rgba(255, 255, 255, 0.9); 
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.2);
    }
    h1, h2, h3 {
        color: #2c3e50;
        text-align: center;
    }
            
    label {
        font-weight: bold;
        font-size: 14px;
    }
    .stButton > button {
        background-color: #4caf50;
        color: white;
        font-size: 16px;
        padding: 10px 20px;
        border-radius: 5px;
        border: none;
        cursor: pointer;
    }
    .stButton > button:hover {
        background-color: #45a049;
    .footer {
        text-align: center;
        margin-top: 50px;
        font-size: 14px;
        color: #6c757d;
    }

   .footer {
        text-align: center; 
        margin-top: 40px; 
    }
    .footer a {
        color: #007bff;
        text-decoration: none;
        margin: 0 10px; 
        display: inline-block; 
    }
    .footer a:hover {
        text-decoration: underline; 
    }
    }
    </style>
""", unsafe_allow_html=True)



st.title("Saraton Kasalligi Tashxisi")
st.write("""
<div style="text-align: center; font-size: 16px; color: #c8dbc8;">
Ushbu dastur bioximik test natijalaringizga asoslanib saraton kasalligi ehtimolini bashorat qiladi. 
Kerakli parametrlarni kiriting va natijani ko'ring.
</div>
""", unsafe_allow_html=True)

st.header("Shaxsiy Ma'lumotlar")
AGE = st.number_input("Yoshingizni kiriting", min_value=1, max_value=100, value=25, step=1)
GENDER = st.radio("Jinsingizni tanlang", options=["Erkak", "Ayol"])
GENDER = 1 if GENDER == "Erkak" else 0

st.header("Bioximik Parametrlari")
SMOKING = []
for feature in bio_features:
    value = st.number_input(f"{feature} (Chekish yoki chekmasligi)", value=0.0, step=0.1)
    GENDER.append(value)

user_data = [AGE, GENDER] + GENDER

if st.button("Natijani Ko'rish"):
    prediction = model.predict([user_data])
    result = result_mapping.get(prediction[0], "Aniqlab bo'lmadi")
    st.success(f"**Bashorat:** {result}")
    

st.markdown(
    """
    <div class='footer'>
      Ushbu ilova jigar kasalligi bo'yicha bashorat qiladi. Muallif: Eshmurodova Sabrinna<br>
        <a href='https://colab.research.google.com/drive/1bHgqcRkcOtDEQDCCiNKXaX0_GMlnCTA5?usp=sharing' target='_blank'>
            📰 Colab
        </a>
        
    </div>
    """,
    unsafe_allow_html=True,
)
