from utils.loader import load_data_safely

import streamlit as st
import pandas as pd
import plotly.express as px
import os

def app(df):

    st.title("🤖 ML Anomaly Detection")
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(ROOT_DIR, "../data/processed/etihad_ml_anomaly_flags.csv")
    df = load_data_safely(file_path)
    if df is None:
        st.error('❌ Failed to load data.')
        return

    st.metric("🔺 High Anomaly Flights", df[df['Anomaly_Score'] > 0.5].shape[0])
    st.dataframe(df[df['Anomaly_Score'] > 0.5][['FlightDate', 'Callsign', 'Anomaly_Score']])

    shap = df['SHAP_Top_Feature'].value_counts().reset_index()
    st.plotly_chart(px.bar(shap, x='index', y='SHAP_Top_Feature', title='SHAP Feature Breakdown'))
