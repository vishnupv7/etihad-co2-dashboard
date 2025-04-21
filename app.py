
import streamlit as st
import pandas as pd
from pathlib import Path

from pages import (
    home,
    route_view,
    ml_view,
    esg_view,
    deviation_view,
    weather_view,
    aircraft_view
)

@st.cache_data
def load_local_data():
    try:
        csv_path = Path(__file__).parent / "final_dashboard_sample.csv"
        df = pd.read_csv(csv_path)
        return df
    except Exception as e:
        st.error(f"❌ Failed to load CSV: {e}")
        return pd.DataFrame()

df = load_local_data()

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
pages[selection].app(df)
