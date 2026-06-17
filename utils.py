import base64
import os
import streamlit as st

def set_bg(image_path):

    if not os.path.exists(image_path):
        st.error(f"❌ Background not found: {image_path}")
        return

    with open(image_path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}

        h1, h2, h3, h4, h5, h6, p, label {{
            color: white !important;
        }}

        .stButton > button {{
            background-color: #2e7d32;
            color: white;
            border-radius: 10px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )