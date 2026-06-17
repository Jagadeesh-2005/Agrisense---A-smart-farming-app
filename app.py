import streamlit as st
from utils import set_bg

from crop_recommendation import show_crop
from disease_detection import show_disease
from suggestions import show_suggestions
from fertilizer_recommendation import show_fertilizer
from weather_report import show_weather

st.set_page_config(page_title="AgriSense", layout="wide")

if "page" not in st.session_state:
    st.session_state.page = "welcome"

if st.session_state.page == "welcome":

    set_bg("images/welcome_bg.jpeg")

    st.markdown("""
        <div style="
            display:flex;
            flex-direction:column;
            justify-content:center;
            align-items:center;
            height:80vh;
            color:white;
        ">
            <h1 style="font-size:60px;">AGRISENSE</h1>
            <h3>A Smart Farming App</h3>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([2,1,2])

    with col2:
        if st.button("🚀 Enter Dashboard"):
            st.session_state.page = "home"
            st.rerun()

elif st.session_state.page == "home":

    set_bg("images/dashboard_bg.jpg")

    st.markdown("<h1 style='text-align:center;'>🌾 WE PROVIDE SERVICES</h1>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    # 🌾 Crop
    with col1:
        st.image("images/crop_card.jpg", use_container_width=True)
        if st.button(" ", key="crop_btn"):
            st.session_state.page = "crop"
            st.rerun()
        st.markdown("<h4 style='text-align:center;'>Crop Recommendation</h4>", unsafe_allow_html=True)

    # 🧪 Fertilizer
    with col2:
        st.image("images/fertilizer_card.jpg", use_container_width=True)
        if st.button(" ", key="fert_btn"):
            st.session_state.page = "fertilizer"
            st.rerun()
        st.markdown("<h4 style='text-align:center;'>Fertilizer</h4>", unsafe_allow_html=True)

    # 🦠 Disease
    with col3:
        st.image("images/disease_card.jpg", use_container_width=True)
        if st.button(" ", key="dis_btn"):
            st.session_state.page = "disease"
            st.rerun()
        st.markdown("<h4 style='text-align:center;'>Disease Detection</h4>", unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    col4, col5, col6 = st.columns(3)

    # 🌱 Suggestions
    with col4:
        st.image("images/suggestion_card.jpg", use_container_width=True)
        if st.button(" ", key="sug_btn"):
            st.session_state.page = "suggestions"
            st.rerun()
        st.markdown("<h4 style='text-align:center;'>Suggestions</h4>", unsafe_allow_html=True)


    # 🌦 Weather
    with col5:
        st.image("images/weather_card.jpg", use_container_width=True)
        if st.button(" ", key="wea_btn"):
            st.session_state.page = "weather"
            st.rerun()
        st.markdown("<h4 style='text-align:center;'>Weather</h4>", unsafe_allow_html=True)


# ================================
# ROUTING PAGES
# ================================

elif st.session_state.page == "crop":
    show_crop()

elif st.session_state.page == "disease":
    show_disease()

elif st.session_state.page == "fertilizer":
    show_fertilizer()

elif st.session_state.page == "suggestions":
    show_suggestions()

elif st.session_state.page == "weather":
    show_weather()
