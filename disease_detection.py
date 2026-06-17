import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
from utils import set_bg

model = tf.keras.models.load_model("disease_model.keras")

def show_disease():

    set_bg("images/disease_bg.jpg")

    st.title("🦠 Disease Detection")

    if st.button("⬅ Back"):
        st.session_state.page = "home"
        st.rerun()

    crop = st.text_input("Enter Crop Name")

    file = st.file_uploader("Upload Image")

    if file:
        img = Image.open(file)
        st.image(img)

        if st.button("Detect"):
            arr = np.array(img.resize((128,128)))/255.0
            arr = arr.reshape(1,128,128,3)

            pred = model.predict(arr)
            st.success(f"Disease Detected")