import streamlit as st
from datetime import datetime

# ---- PAGE CONFIG ----
st.set_page_config(
    page_title="Etihad CO₂ Optimization Dashboard",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---- SIDEBAR ----
st.sidebar.image(
    "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Etihad_Airways_Logo.svg/512px-Etihad_Airways_Logo.svg.png",
    width=160
)
st.sidebar.title("Etihad CO₂ Dashboard")

# ✅ REAL global toggle using Session State!
if "mode" not in st.session_state:
    st.session_state["mode"] = "Historic"
st.session_state["mode"] = st.sidebar.radio("Data Mode", ["Historic", "Live"], index=0)

st.sidebar.markdown("---")
st.sidebar.markdown("**Built by:** [Vishnu Pv](https://www.linkedin.com/in/vishnu-p-v-)")
st.sidebar.markdown("[GitHub Repo](https://github.com/vishnupv7/etihad-co2-dashboard)")

# ---- LANDING HEADER ----
st.title("✈️ Etihad CO₂ & Fuel Efficiency Dashboard")
st.caption("A real-time, ML-powered, ESG-ready analytics solution for Etihad Airways.")

st.markdown(
    """
    ### Welcome!
    This dashboard integrates **Etihad Airways' flight, fuel, emissions, and weather data** with real-time and historic APIs.

    **What you can do:**
    - Analyze route/network CO₂ and fuel performance
    - Detect operational anomalies, inefficiencies, and reroutes
    - Benchmark against ESG/CO₂ targets (ICAO, Etihad annuals)
    - Visualize impact of weather, aircraft, and route choices
    - Track live KPIs and get actionable recommendations

    #### 👉 Use the sidebar to navigate:  
    - **Home** (this page): Executive summary, live update status
    - **Route View**: Map, route KPIs, top anomalies
    - **Aircraft View**: Fleet/engine performance
    - **Weather View**: Weather penalties & effects
    - **ML View**: Model predictions, feature importance
    - **Deviation View**: Holding/reroute impacts
    - **ESG View**: Compliance, trends, best/worst routes
    """
)

st.info("**Tip:** Data auto-refreshes in live mode. Use Historic mode for deeper model insights and validation.")

# ---- ABOUT/FOOTER ----
st.markdown("---")
st.markdown(
    f"""
    **About this project:**  
    Developed as part of a Data Science MBA project for Etihad Airways, this dashboard demonstrates the power of unified analytics, real-time prediction, and ESG benchmarking for modern airline operations.
    
    **Project version:** {datetime.now().strftime('%Y-%m-%d')}
    """
)
st.caption("© 2025 Vishnu Pv. For educational and demonstration purposes only.")
