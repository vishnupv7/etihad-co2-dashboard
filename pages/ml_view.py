# pages/ml_view.py

import streamlit as st
import pandas as pd
import plotly.express as px

def app():
    st.title("🤖 ML Anomaly & Prediction Insights")
    df = pd.read_csv('data/processed/final_dashboard_sample.csv')

    # Anomaly Table
    st.write("### Anomaly Flagged Flights")
    st.dataframe(df[df.get('anomaly_flag',0)==1][['Origin','Destination','Aircraft_Code','Fuel_Burn_kg','CO2_kg','route_efficiency_score']].head())

    # Feature Importance Plot (Simulated)
    st.write("### Feature Importances (Fuel Prediction)")
    # If you have SHAP values, plot here; else show sample importances
    feat_imp = pd.Series({'Weather_Penalty_Index': 0.87, 'Altitude_Drift': 0.07, 'Holding_Loop_Detected': 0.02, 'Unplanned_Reroute': 0.01, 'Seat_Count':0.01})
    st.bar_chart(feat_imp)

    # Prediction error histogram
    st.write("### Model Error Distribution (Historic)")
    if 'Fuel_Burn_kg' in df.columns and 'predicted_fuel' in df.columns:
        error = df['Fuel_Burn_kg'] - df['predicted_fuel']
        st.histogram(error, bins=30)
    else:
        st.info("Model error histogram will appear once predictions are available.")

    st.markdown("#### Alerts & Recommendations")
    st.write("• Investigate any flight flagged as anomaly for possible operational inefficiency.")
