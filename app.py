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

# ✅ Auto-refresh every 60s for live mode
REFRESH_INTERVAL = 60 * 1000  # in milliseconds
st_autorefresh(interval=REFRESH_INTERVAL, key="datarefresh")

# ✅ Sidebar toggle: Live or Offline
st.sidebar.title("🧭 Etihad CO₂ Optimization Dashboard")
use_live = st.sidebar.toggle("🔌 Enable Real-Time Mode", value=True)

@st.cache_data(ttl=30)
def load_data():
    try:
        if use_live:
            df = pd.read_csv("/content/drive/MyDrive/Etihad_CO2_Optimization/data/live/live_combined.csv")
        else:
            df = pd.read_csv(Path(__file__).parent / "final_dashboard_sample.csv")
        return df
    except Exception as e:
        st.error(f"❌ Failed to load data: {e}")
        return pd.DataFrame()

df = load_data()

# ✅ Navigation
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
