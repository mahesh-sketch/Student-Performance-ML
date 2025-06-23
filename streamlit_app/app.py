import streamlit as st
import requests

st.set_page_config(page_title="🎓 Student Exam Performance Predictor")

st.title("📊 Student Exam Performance Indicator")
st.markdown("### Fill the form below to predict the **Math Score**")

with st.form("prediction_form"):
    gender = st.selectbox("Gender", ["male", "female"])
    
    ethnicity = st.selectbox("Race or Ethnicity", [
        "group A", "group B", "group C", "group D", "group E"
    ])
    
    parental_level_of_education = st.selectbox("Parental Level of Education", [
        "associate's degree", "bachelor's degree", "high school", 
        "master's degree", "some college", "some high school"
    ])
    
    lunch = st.selectbox("Lunch Type", ["free/reduced", "standard"])
    
    test_preparation_course = st.selectbox("Test Preparation Course", ["none", "completed"])
    
    reading_score = st.slider("Writing Score (out of 100)", 0, 100, 70)
    
    writing_score = st.slider("Reading Score (out of 100)", 0, 100, 70)

    submitted = st.form_submit_button("🎯 Predict your Math Score")

if submitted:
    input_data = {
        "gender": gender,
        "race_ethnicity": ethnicity,
        "parental_level_of_education": parental_level_of_education,
        "lunch": lunch,
        "test_preparation_course": test_preparation_course,
        "reading_score": reading_score,
        "writing_score": writing_score
    }

    try:
        response = requests.post("http://localhost:8000/predict/", json=input_data)
        if response.status_code == 200:
            prediction = response.json()["prediction"]
            st.success(f"🧮 Predicted Math Score: `{prediction}`")
        else:
            st.error("⚠️ Server error! Please check FastAPI logs.")
    except Exception as e:
        st.error(f"🔌 Connection error: {e}")
