import streamlit as st
import os

from pages import (
    home,
    route_view,
    ml_view,
    esg_view,
    deviation_view,
    weather_view,
    aircraft_view
)

from utils.loader import load_data_safely

# Load dataset (main)
df = load_data_safely("https://drive.google.com/uc?id=1yh9ASDuVEa7ckNclK4s5pn6RfS1k8wMC")


# Sidebar navigation
st.sidebar.title("🧭 Etihad CO₂ Optimization Dashboard")
pages = {
    "🏠 Home": home,
    "🗺️ Route Overview": route_view,
    "📉 ML Anomaly Detection": ml_view,
    "🌱 ESG Alignment": esg_view,
    "🔀 Deviation Insights": deviation_view,
    "⛅ Weather Impact": weather_view,
    "✈️ Aircraft Efficiency": aircraft_view,
}
selection = st.sidebar.radio("Navigate", list(pages.keys()))
pages[selection].app()
