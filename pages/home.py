
import streamlit as st
import pandas as pd
import plotly.express as px
import os

from utils.loader import load_data_safely

def app():
    path = "/content/drive/MyDrive/Etihad_CO2_Optimization/data/processed/final_dashboard_dataset.csv"
    df = load_data_safely(path)
    if df is None:
        st.error("❌ Final dashboard dataset not loaded.")
        return
    st.title("🏠 Etihad CO₂ Dashboard – Home")
    st.metric("✈️ Total Flights", len(df))
    st.metric("🌍 Avg CO₂ per RTK", round(df['CO2_per_RTK'].mean(), 2))
    st.metric("✅ ESG Match %", f"{round(df['esg_match_percent'].mean(), 2)}%")

    st.subheader("📈 CO₂ Emission Trends")
    co2_trend = df.groupby('FlightDate')['CO2_kg'].mean().reset_index()
    st.plotly_chart(px.line(co2_trend, x='FlightDate', y='CO2_kg', title='Avg Daily CO₂ Emissions'))

    st.subheader("🛫 CO₂ Share by Aircraft")
    aircraft_co2 = df.groupby('Aircraft_Code')['CO2_kg'].sum().reset_index()
    st.plotly_chart(px.pie(aircraft_co2, names='Aircraft_Code', values='CO2_kg'))

    st.subheader("📘 ESG Compliance Over Time")
    esg = df.groupby('FlightDate')['esg_match_percent'].mean().reset_index()
    st.plotly_chart(px.line(esg, x='FlightDate', y='esg_match_percent'))
