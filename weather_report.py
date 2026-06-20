import streamlit as st
import requests

API_KEY = "Enter your api key"   # 🔥 replace with your key


# ============================
# GET WEATHER DATA
# ============================
def get_weather(city):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        return None

    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather = data["weather"][0]["description"]
    wind = data["wind"]["speed"]
    icon = data["weather"][0]["icon"]

    return temperature, humidity, weather, wind, icon


# ============================
# WEATHER UI
# ============================
def show_weather():


    if st.button("⬅ Back to Dashboard"):
        st.session_state.page = "home"
        st.rerun()

    st.title("🌦 Weather Report")

    city = st.text_input("Enter City")

    if st.button("Get Weather"):

        result = get_weather(city)

        if result is None:
            st.error("❌ City not found")
            return

        temp, humidity, weather, wind, icon = result

        icon_url = f"http://openweathermap.org/img/wn/{icon}@2x.png"

        # CSS
        st.markdown("""
        <style>
        .weather-card {
            background: linear-gradient(135deg,#4facfe,#00f2fe);
            padding: 30px;
            border-radius: 20px;
            color: white;
            text-align: center;
            box-shadow: 0px 10px 30px rgba(0,0,0,0.2);
        }
        </style>
        """, unsafe_allow_html=True)

        st.markdown('<div class="weather-card">', unsafe_allow_html=True)

        col1, col2 = st.columns([1,2])

        with col1:
            st.image(icon_url)

        with col2:
            st.markdown(f"### {city.title()}")
            st.markdown(f"## 🌡 {temp} °C")
            st.markdown(f"🌥 {weather}")

        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("### Details")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("💧 Humidity", f"{humidity}%")

        with col2:
            st.metric("🌬 Wind Speed", f"{wind} m/s")
