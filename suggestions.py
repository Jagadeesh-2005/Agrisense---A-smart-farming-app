from openai import OpenAI
import streamlit as st

client = OpenAI(api_key="Enter your Api key")
def generate_suggestions(crop):

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": f"Give farming tips for {crop}"}]
        )

        return response.choices[0].message.content

    except Exception as e:
        return "⚠ AI service unavailable (quota exceeded). Please try later."
    
    
def show_suggestions():

    st.title("🌱 AI Farming Suggestions")

    if st.button("⬅ Back"):
        st.session_state.page = "home"
        st.rerun()

    crop = st.text_input("🌾 Enter Crop Name")

    if st.button("Generate Suggestions"):

        if crop.strip() == "":
            st.warning("⚠ Please enter crop name")
            return

        with st.spinner("🤖 Generating AI suggestions..."):
            result = generate_suggestions(crop)

        st.success("✅ AI Generated Suggestions")
        st.write(result)
