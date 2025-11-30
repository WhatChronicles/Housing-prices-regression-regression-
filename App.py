import os
import streamlit as st
import pandas as pd
import joblib

def load_model():
    base_dir = os.path.dirname(__file__)
    model_path = os.path.join(base_dir, "models", "best_model.pkl")
    encoder_path = os.path.join(base_dir, "models", "label_encoders.pkl")
    if not os.path.exists(model_path) or not os.path.exists(encoder_path):
        st.error("Model or encoder file not found. Please run src/model.py to train and generate them.")
        st.stop()
    model = joblib.load(model_path)
    encoders = joblib.load(encoder_path)
    return model, encoders

def predict_price(model, encoders, inputs):
    df = pd.DataFrame([inputs])
    for col in encoders:
        df[col] = encoders[col].transform(df[col])
    prediction = model.predict(df)[0]
    return round(prediction, 2)

st.title("House Price Predictor")

model, encoders = load_model()

mainroad = st.selectbox("Main Road", encoders["mainroad"].classes_)
guestroom = st.selectbox("Guest Room", encoders["guestroom"].classes_)
basement = st.selectbox("Basement", encoders["basement"].classes_)
hotwaterheating = st.selectbox("Hot Water Heating", encoders["hotwaterheating"].classes_)
airconditioning = st.selectbox("Air Conditioning", encoders["airconditioning"].classes_)
prefarea = st.selectbox("Preferred Area", encoders["prefarea"].classes_)
furnishingstatus = st.selectbox("Furnishing Status", encoders["furnishingstatus"].classes_)

area = st.slider("Area", 500, 20000, 7500)
bedrooms = st.slider("Bedrooms", 1, 10, 3)
bathrooms = st.slider("Bathrooms", 1, 10, 2)
stories = st.slider("Stories", 1, 4, 2)
parking = st.slider("Parking Spaces", 0, 4, 2)

inputs = {
    "mainroad": mainroad,
    "guestroom": guestroom,
    "basement": basement,
    "hotwaterheating": hotwaterheating,
    "airconditioning": airconditioning,
    "prefarea": prefarea,
    "furnishingstatus": furnishingstatus,
    "area": area,
    "bedrooms": bedrooms,
    "bathrooms": bathrooms,
    "stories": stories,
    "parking": parking
}

if st.button("Predict House Price"):
    price = predict_price(model, encoders, inputs)
    st.success(f"Estimated House Price: ₹{price}")