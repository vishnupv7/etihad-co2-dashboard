import streamlit as st
import pandas as pd
from pathlib import Path
from streamlit_autorefresh import st_autorefresh

from pages import (
    home,
    route_view,
    ml_view,
    esg_view,
    deviation_view,
    weather_view,
    aircraft_view
)

# ✅ Auto-refresh every 60 seconds
st_autorefresh(interval=60000, limit=None, key="dashboardrefresh")

# ✅ Try to load real-time data if available
@st.cache_data
def load_dashboard_data():
    live_path = Path("data/live/final_dashboard_sample.csv")
    fallback_path = Path("final_dashboard_sample.csv")

    if live_path.exists():
        df = pd.read_csv(live_path)
        return df, "🟢 LIVE"
    elif fallback_path.exists():
        df = pd.read_csv(fallback_path)
        return df, "⚪ OFFLINE"
    else:
        return pd.DataFrame(), "🔴 MISSING"

# ✅ Load the data
df, mode = load_dashboard_data()

# ✅ Dashboard UI
st.sidebar.title("🧭 Etihad CO₂ Optimization Dashboard")
st.sidebar.markdown(f"**Data Mode:** {mode}")

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
