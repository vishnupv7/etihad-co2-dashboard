
import streamlit as st
import pandas as pd
from streamlit_autorefresh import st_autorefresh
from pathlib import Path

st.set_page_config(page_title="Etihad CO₂ Live Dashboard", layout="wide")
st_autorefresh(interval=60000, key="datarefresh")

FALLBACK_PATH = Path(__file__).parent / "final_dashboard_sample.csv"
LIVE_PATH = Path(__file__).parent / "data" / "live" / "live_combined.csv"

use_live = st.sidebar.toggle("🌐 Use Live Data", value=True)

@st.cache_data
def load_data(live=True):
    try:
        path = LIVE_PATH if live else FALLBACK_PATH
        df = pd.read_csv(path)
        return df
    except:
        st.error("❌ Failed to load data.")
        return pd.DataFrame()

df = load_data(use_live)
st.success(f"📊 Loaded {'Live' if use_live else 'Fallback'} Data → {df.shape}")
st.dataframe(df.head(10), use_container_width=True)

if use_live and not df.empty:
    import plotly.express as px
    st.plotly_chart(px.scatter(df, x="temp", y="wind", color="callsign",
        title="Live Weather Impact per Etihad Flight"), use_container_width=True)
