import streamlit as st
import joblib
import numpy as np
import pandas as pd

pipeline = joblib.load('sleep_pipeline.pkl')
le_target = joblib.load('le_target.pkl')

st.title("Sleep Disorder Risk Predictor")
st.write("Enter your sleep and health data below:")

age = st.slider("Age", 18, 80, 30)
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
bmi = st.slider("BMI", 15.0, 45.0, 25.0)
sleep_duration = st.slider("Sleep Duration (hrs)", 3.0, 10.0, 7.0)
sleep_quality = st.slider("Sleep Quality Score (1-10)", 1.0, 10.0, 6.0)
rem = st.slider("REM Sleep %", 10.0, 40.0, 22.0)
deep_sleep = st.slider("Deep Sleep %", 5.0, 40.0, 18.0)
sleep_latency = st.slider("Sleep Latency (mins)", 1, 60, 15)
wake_episodes = st.slider("Wake Episodes per Night", 0, 10, 2)
caffeine = st.slider("Caffeine before bed (mg)", 0, 200, 0)
alcohol = st.slider("Alcohol units before bed", 0.0, 5.0, 0.0)
screen_time = st.slider("Screen time before bed (mins)", 0, 180, 30)
exercise = st.slider("Exercise today (mins)", 0, 120, 30)
steps = st.slider("Steps today", 0, 20000, 8000)
nap = st.slider("Nap duration (mins)", 0, 120, 0)
stress = st.slider("Stress Score (1-10)", 1.0, 10.0, 5.0)
work_hours = st.slider("Work hours today", 0.0, 16.0, 8.0)
heart_rate = st.slider("Resting Heart Rate (bpm)", 40, 100, 65)
sleep_aid = st.selectbox("Sleep aid used?", [0, 1])
shift_work = st.selectbox("Shift work?", [0, 1])
room_temp = st.slider("Room temperature (°C)", 15.0, 30.0, 20.0)
weekend_diff = st.slider("Weekend sleep difference (hrs)", 0.0, 4.0, 1.0)
cognitive = st.slider("Cognitive performance score", 0.0, 100.0, 70.0)
felt_rested = st.selectbox("Felt rested?", [0, 1])
chronotype = st.selectbox("Chronotype", ["Morning", "Evening", "Neutral"])
mental_health = st.selectbox("Mental health condition", ["Healthy", "Anxiety", "Depression", "Both"])
season = st.selectbox("Season", ["Spring", "Summer", "Autumn", "Winter"])
day_type = st.selectbox("Day type", ["Weekday", "Weekend"])
country = st.selectbox("Country", ["USA", "UK", "India", "Australia", "Canada", "Germany", "Japan", "Brazil", "China", "France", "Spain", "Italy", "Mexico", "Netherlands", "Sweden"])
occupation = st.selectbox("Occupation", ["Engineer", "Doctor", "Teacher", "Student", "Manager", "Nurse", "Lawyer", "Driver", "Sales", "Artist", "Accountant", "Software Engineer"])

if st.button("Predict"):
    input_data = pd.DataFrame([{
        'age': age, 'gender': gender, 'bmi': bmi,
        'sleep_duration_hrs': sleep_duration, 'sleep_quality_score': sleep_quality,
        'rem_percentage': rem, 'deep_sleep_percentage': deep_sleep,
        'sleep_latency_mins': sleep_latency, 'wake_episodes_per_night': wake_episodes,
        'caffeine_mg_before_bed': caffeine, 'alcohol_units_before_bed': alcohol,
        'screen_time_before_bed_mins': screen_time, 'exercise_day': exercise,
        'steps_that_day': steps, 'nap_duration_mins': nap,
        'stress_score': stress, 'work_hours_that_day': work_hours,
        'heart_rate_resting_bpm': heart_rate, 'sleep_aid_used': sleep_aid,
        'shift_work': shift_work, 'room_temperature_celsius': room_temp,
        'weekend_sleep_diff_hrs': weekend_diff, 'cognitive_performance_score': cognitive,
        'felt_rested': felt_rested, 'chronotype': chronotype,
        'mental_health_condition': mental_health, 'season': season,
        'day_type': day_type, 'country': country, 'occupation': occupation
    }])

    prediction = pipeline.predict(input_data)
    result = le_target.inverse_transform(prediction)[0]

    colors = {
        "Healthy": "green",
        "Mild": "orange", 
        "Moderate": "red",
        "Severe": "darkred"
    }

    st.markdown(f"### Predicted Risk: :{colors[result]}[{result}]")