import streamlit as st
from utils.loader import unified_loader
import plotly.express as px
import pandas as pd

def app():
    mode = st.session_state.get("mode", "Historic")
    df = unified_loader(mode.lower())

    st.title("🌱 ESG Compliance & Benchmarking")
    if df is not None and not df.empty:
        if 'esg_match_percent' in df:
            st.metric("ESG Match %", f"{df['esg_match_percent'].mean():.2f}%")
        if 'FlightDate' in df.columns and 'CO2_kg' in df.columns:
            df['FlightDate'] = pd.to_datetime(df['FlightDate'], errors='coerce')
            by_month = df.groupby(df['FlightDate'].dt.to_period('M'))['CO2_kg'].mean().reset_index()
            fig = px.line(by_month, x='FlightDate', y='CO2_kg', title='Monthly CO₂ Emissions')
            st.plotly_chart(fig)

        st.write("### Best & Worst Flights by ESG Compliance")
        if 'esg_match_percent' in df and 'callsign' in df and 'CO2_kg' in df and 'Fuel_Burn_kg' in df:
            st.dataframe(df[['callsign','esg_match_percent','CO2_kg','Fuel_Burn_kg']].sort_values('esg_match_percent',ascending=False).head(5))
            st.dataframe(df[['callsign','esg_match_percent','CO2_kg','Fuel_Burn_kg']].sort_values('esg_match_percent').head(5))

        st.markdown("#### Recommendation")
        st.write("• Prioritize efficiency improvements on routes with low ESG compliance.")
    else:
        st.info("No ESG data available.")

app()
