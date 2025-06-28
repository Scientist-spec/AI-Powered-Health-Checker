# ai_health_checker.py

import streamlit as st
import cohere
import os

# Set your Cohere API key (store in environment variable for safety)
cohere_api_key = os.getenv("COHERE_API_KEY", "Pon8ziLYhsHaCki967lGu5IzmiclOeDIrYCYgMWd")
co = cohere.Client(cohere_api_key)

# Streamlit UI
st.set_page_config(page_title="AI Health Checker", layout="centered")
st.title("AI-Powered Health Checker (Cohere)")

st.write("Answer a few quick questions to check your overall health status.")

# Gender Selection
gender = st.selectbox("Select your gender:", ["Male", "Female"])

# Symptom Questions
st.subheader("Health Check-In")
symptoms = st.text_area("Describe any symptoms you're experiencing today (e.g., fatigue, headache, low appetite, etc.)")

vitals = st.text_input("Enter known vitals (optional) - e.g., BP: 120/80, Sugar: 90mg/dL")

if st.button("Check My Health"):
    with st.spinner("Analyzing your health report..."):
        prompt = f"""
You are a virtual health assistant. A {gender.lower()} user reports the following symptoms:
{symptoms}
Their vital info is: {vitals if vitals else 'Not provided'}.

Based on this, provide:
1. Possible health insights
2. Recommendations (diet, rest, hydration, etc.)
3. Any red flags that need urgent care

Keep it concise and supportive.
"""

        try:
            response = co.generate(
                model="command-r-plus",
                prompt=prompt,
                max_tokens=500,
                temperature=0.7
            )

            result = response.generations[0].text.strip()
            st.success("Health Report Generated!")
            st.markdown(result)

        except Exception as e:
            st.error(f"Something went wrong: {e}")
