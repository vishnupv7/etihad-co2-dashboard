import streamlit as st
from utils.loader import unified_loader
import plotly.express as px

def app():
    df = unified_loader(st.session_state["mode"].lower())

    st.title("🌱 ESG Compliance & Benchmarking")
    st.metric("ESG Match %", f"{df['esg_match_percent'].mean():.2f}%")

    if 'FlightDate' in df.columns and 'CO2_kg' in df.columns:
        import pandas as pd
        df['FlightDate'] = pd.to_datetime(df['FlightDate'])
        by_month = df.groupby(df['FlightDate'].dt.to_period('M'))['CO2_kg'].mean().reset_index()
        fig = px.line(by_month, x='FlightDate', y='CO2_kg', title='Monthly CO₂ Emissions')
        st.plotly_chart(fig)

    st.write("### Best & Worst Flights by ESG Compliance")
    st.dataframe(df[['callsign','esg_match_percent','CO2_kg','Fuel_Burn_kg']].sort_values('esg_match_percent',ascending=False).head(5))
    st.dataframe(df[['callsign','esg_match_percent','CO2_kg','Fuel_Burn_kg']].sort_values('esg_match_percent').head(5))

    st.markdown("#### Recommendation")
    st.write("• Prioritize efficiency improvements on routes with low ESG compliance.")

app()
