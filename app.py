import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="EV vs ICE CO₂ Emissions Predictor",
    page_icon="🚗",
    layout="centered"
)

# Load trained pipeline
model = joblib.load("model_pipeline.pkl")

st.title("🚗 EV vs ICE CO₂ Emissions Predictor")
st.write("Predict vehicle CO₂ emissions based on vehicle specifications.")

st.subheader("Enter Vehicle Details")

year = st.number_input(
    "Year",
    min_value=2015,
    max_value=2026,
    value=2024
)

engine_cylinders = st.number_input(
    "Engine Cylinders",
    min_value=0,
    max_value=16,
    value=4
)

engine_size = st.number_input(
    "Engine Size (L)",
    min_value=0.0,
    max_value=10.0,
    value=2.0,
    step=0.1
)

city_mpg = st.number_input(
    "City MPG",
    min_value=0,
    max_value=200,
    value=25
)

highway_mpg = st.number_input(
    "Highway MPG",
    min_value=0,
    max_value=250,
    value=35
)

combined_mpg = st.number_input(
    "Combined MPG",
    min_value=0,
    max_value=250,
    value=30
)

ev_range = st.number_input(
    "EV Range (miles)",
    min_value=0,
    max_value=600,
    value=0
)

if st.button("Predict CO₂ Emissions"):

    input_data = pd.DataFrame({
        "Year": [year],
        "Engine_Cylinders": [engine_cylinders],
        "Engine_Size_L": [engine_size],
        "City_MPG": [city_mpg],
        "Highway_MPG": [highway_mpg],
        "Combined_MPG": [combined_mpg],
        "EV_Range_miles": [ev_range]
    })

    prediction = model.predict(input_data)[0]

    st.success(
        f"Predicted CO₂ Emissions: {prediction:.2f} g/mile"
    )
