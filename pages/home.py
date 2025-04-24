# pages/home.py

import streamlit as st
import pandas as pd

def app():
    st.title("🏠 Etihad CO₂ Dashboard - Executive Summary")
    df = pd.read_csv('data/processed/final_dashboard_sample.csv')

    # KPIs
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Flights", f"{len(df):,}")
    col2.metric("Avg Fuel Burn (kg)", f"{df['Fuel_Burn_kg'].mean():,.0f}")
    col3.metric("Avg CO₂ (kg)", f"{df['CO2_kg'].mean():,.0f}")
    col4.metric("Anomaly %", f"{100 * df.get('anomaly_flag', 0).mean():.2f}%")

    st.subheader("Latest Live Predictions")
    live = pd.read_csv('data/live/etihad_live_predictions.csv')
    st.dataframe(live[['callsign','predicted_fuel','predicted_co2','anomaly_flag_pred','predicted_revenue']].head())

    st.subheader("Route Efficiency Score Distribution")
    st.bar_chart(df['route_efficiency_score'].value_counts().sort_index())

    st.subheader("ESG Compliance Score")
    st.metric("ESG Match %", f"{df['esg_match_percent'].mean():.2f}%")
    st.caption(f"Last updated: [get timestamp from live/last_updated.txt]")

    st.markdown("#### Recommendations")
    st.write("• Prioritize improving efficiency on flagged routes with low efficiency scores or recurring anomalies.")
    st.write("• Target weather-related penalties by optimizing flight planning and altitudes.")

    # Alert
    if live['anomaly_flag_pred'].eq('Anomaly').any():
        st.error("⚠️ Anomaly detected in live flights! Investigate flagged callsigns above.")
