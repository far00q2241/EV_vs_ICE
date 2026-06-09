# 🚗 EV vs ICE CO₂ Emissions Predictor

A Machine Learning web application that predicts vehicle CO₂ emissions based on vehicle specifications using a Random Forest Regressor model.

## 📌 Project Overview

This project compares Electric Vehicles (EVs) and Internal Combustion Engine (ICE) vehicles by estimating CO₂ emissions from vehicle characteristics such as engine size, fuel efficiency, and EV range.

The application is built with:

* Python
* Scikit-learn
* Pandas
* Streamlit

## 📊 Features

* Predict CO₂ emissions (g/mile)
* Interactive Streamlit interface
* Machine Learning pipeline for preprocessing and prediction
* Supports both EV and ICE vehicle specifications

## 🛠️ Input Features

* Year
* Engine Cylinders
* Engine Size (L)
* City MPG
* Highway MPG
* Combined MPG
* EV Range (miles)

## 🤖 Model

* Algorithm: Random Forest Regressor
* Feature Selection: SelectKBest
* Saved Model: `model_pipeline.pkl`

## 📁 Project Structure

```text
├── app.py
├── model_pipeline.pkl
├── requirements.txt
├── runtime.txt
└── README.md
```

## 🚀 Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 🌐 Deployment

The application is deployed using Streamlit Cloud.

## 📈 Results

The model predicts vehicle CO₂ emissions in grams per mile based on vehicle specifications and fuel efficiency metrics.

## 👨‍💻 Author

Farooq Khan
