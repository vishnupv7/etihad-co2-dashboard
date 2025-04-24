# app.py

import streamlit as st
from utils.loader import unified_loader
from utils.feature_engineering import engineer_live_features_etihad
from utils.inference import run_inference_on_etihad_live

st.set_page_config(page_title="Etihad CO₂ Live Dashboard", layout="wide")

st.title("✈️ Etihad CO₂ Live Dashboard")
mode = st.sidebar.radio("Data Mode", ["Live", "Historic"])

# 1. Load data
df = unified_loader(mode='live' if mode == "Live" else 'historic')

# 2. For live mode, engineer features, run ML inference, show predictions
if mode == "Live":
    df_etihad = engineer_live_features_etihad(df, planes_path='data/reference/planes.dat')
    preds = run_inference_on_etihad_live(df_etihad, model_dir='dashboard/models')
    st.write("## Live Etihad Predictions")
    st.dataframe(preds[['callsign', 'predicted_fuel', 'predicted_co2', 'anomaly_flag_pred', 'predicted_revenue']])
else:
    st.write("## Historic Data Preview")
    st.dataframe(df.head(10))

# (Add visuals, summary KPIs, charts, etc. here as needed!)
