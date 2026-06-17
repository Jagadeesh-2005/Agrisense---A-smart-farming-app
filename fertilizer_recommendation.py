import streamlit as st
import pickle
import numpy as np
from utils import set_bg

# ============================
# LOAD MODEL + ENCODERS
# ============================
@st.cache_resource
def load_model():
    return pickle.load(open("fertilizer_model.pkl", "rb"))

@st.cache_resource
def load_encoders():
    return (
        pickle.load(open("soil_encoder.pkl", "rb")),
        pickle.load(open("crop_encoder.pkl", "rb")),
        pickle.load(open("fertilizer_encoder.pkl", "rb"))
    )

fertilizer_model = load_model()
soil_encoder, crop_encoder, fertilizer_encoder = load_encoders()


# ============================
# MAIN FUNCTION
# ============================
def show_fertilizer():

    set_bg("images/fertilizer_bg.jpg")

    st.title("🧪 Fertilizer Recommendation")

    # 🔙 Back Button
    if st.button("⬅ Back"):
        st.session_state.page = "home"
        st.rerun()

    # ================= INPUTS =================
    col1, col2, col3 = st.columns(3)

    with col1:
        temperature = st.number_input("🌡 Temperature")
        humidity = st.number_input("💧 Humidity")

    with col2:
        moisture = st.number_input("🌱 Moisture")
        soil = st.selectbox("🪨 Soil Type", soil_encoder.classes_)

    with col3:
        crop = st.selectbox("🌾 Crop Type", crop_encoder.classes_)

    st.markdown("---")

    col4, col5, col6 = st.columns(3)

    with col4:
        nitrogen = st.number_input("Nitrogen")

    with col5:
        phosphorus = st.number_input("Phosphorus")

    with col6:
        potassium = st.number_input("Potassium")

    # ================= PREDICTION =================
    if st.button("🚀 Recommend Fertilizer"):

        soil_encoded = soil_encoder.transform([soil])[0]

        crop_encoded = st.text_input("🌾 Enter Crop Type")

        data = np.array([[
            temperature,
            humidity,
            moisture,
            soil_encoded,
            crop_encoded,
            nitrogen,
            phosphorus,
            potassium
        ]])

        prediction = fertilizer_model.predict(data)

        fertilizer_name = fertilizer_encoder.inverse_transform(prediction)[0]

        st.success(f"✅ Recommended Fertilizer: {fertilizer_name}")