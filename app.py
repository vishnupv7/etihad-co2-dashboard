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

# Load dataset (local CSV)
@st.cache_data
def load_local_data():
    try:
        csv_path = Path(__file__).parent / "final_dashboard_sample.csv"
        df = pd.read_csv(csv_path)
        return df
    except Exception as e:
        st.error(f"❌ Failed to load CSV: {e}")
        return pd.DataFrame()

# Load dataset into df
df = load_local_data()

# Sidebar for navigation and auto-refresh toggle
st.sidebar.title("🧭 Etihad CO₂ Optimization Dashboard")

# Toggle to enable auto-refresh
autorefresh_mode = st.sidebar.checkbox("🔁 Auto-Refresh Dashboard", value=True)

# Auto-refresh functionality with manual override
if autorefresh_mode:
    count = st_autorefresh(interval=60000, key="auto_refresh")  # Refresh every 60 seconds
    st.sidebar.success(f"Auto-refresh enabled. Refresh count: {count}")
else:
    st.sidebar.info("Auto-refresh is off. Manually refresh to update.")

# Pages for navigation
pages = {
    "🏠 Home": home,
    "🗺️ Route Overview": route_view,
    "📉 ML Anomaly Detection": ml_view,
    "🌱 ESG Alignment": esg_view,
    "🔀 Deviation Insights": deviation_view,
    "⛅ Weather Impact": weather_view,
    "✈️ Aircraft Efficiency": aircraft_view,
}

# Page selection
selection = st.sidebar.radio("Navigate", list(pages.keys()))
pages[selection].app(df)  # Pass df to selected page
