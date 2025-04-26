import streamlit as st
from utils.loader import unified_loader

def app():
    mode = st.session_state.get("mode", "Historic")
    df = unified_loader(mode.lower())

    st.title("🏠 Etihad CO₂ Dashboard - Executive Summary")
    if df is not None and not df.empty:
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Total Flights", f"{len(df):,}")
        col2.metric("Avg Fuel Burn (kg)", f"{df['Fuel_Burn_kg'].mean():,.0f}" if 'Fuel_Burn_kg' in df else "N/A")
        col3.metric("Avg CO₂ (kg)", f"{df['CO2_kg'].mean():,.0f}" if 'CO2_kg' in df else "N/A")
        col4.metric("Anomaly %", f"{100 * df.get('anomaly_flag', 0).mean():.2f}%" if 'anomaly_flag' in df else "N/A")

        st.subheader("Latest Live Predictions")
        try:
            import pandas as pd
            live = pd.read_csv('data/live/etihad_live_predictions.csv')
            if not live.empty:
                st.dataframe(live[['callsign','predicted_fuel','predicted_co2','anomaly_flag_pred','predicted_revenue']].head())
                if 'anomaly_flag_pred' in live and live['anomaly_flag_pred'].eq('Anomaly').any():
                    st.error("⚠️ Anomaly detected in live flights! Investigate flagged callsigns above.")
            else:
                st.info("No live predictions available.")
        except Exception:
            st.info("No live predictions available.")

        st.subheader("Route Efficiency Score Distribution")
        if 'route_efficiency_score' in df:
            st.bar_chart(df['route_efficiency_score'].value_counts().sort_index())
        else:
            st.info("Route efficiency scores not available.")

        st.subheader("ESG Compliance Score")
        if 'esg_match_percent' in df:
            st.metric("ESG Match %", f"{df['esg_match_percent'].mean():.2f}%")
        st.caption(f"Last updated: [get timestamp from live/last_updated.txt]")

        st.markdown("#### Recommendations")
        st.write("• Prioritize improving efficiency on flagged routes with low efficiency scores or recurring anomalies.")
        st.write("• Target weather-related penalties by optimizing flight planning and altitudes.")

app()
