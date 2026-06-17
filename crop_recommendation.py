import streamlit as st
import numpy as np
import pickle
from utils import set_bg

model = pickle.load(open("RF.pkl", "rb"))

def show_crop():

    set_bg("images/crop_bg.jpg")

    st.title("🌾 Crop Recommendation")

    if st.button("⬅ Back"):
        st.session_state.page = "home"
        st.rerun()

    N = st.number_input("Nitrogen")
    P = st.number_input("Phosphorus")
    K = st.number_input("Potassium")

    temp = st.number_input("Temperature")
    hum = st.number_input("Humidity")

    ph = st.number_input("pH")
    rain = st.number_input("Rainfall")

    if st.button("Predict"):
        result = model.predict([[N,P,K,temp,hum,ph,rain]])[0]
        st.success(f"🌱 {result}")