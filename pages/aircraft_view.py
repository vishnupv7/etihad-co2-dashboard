import streamlit as st
from utils.loader import unified_loader
import pandas as pd

def app():
    mode = st.session_state.get("mode", "Historic")
    df = unified_loader(mode.lower())

    st.title("✈️ Aircraft Efficiency Overview")
    if df is not None and not df.empty:
        if 'Aircraft_Code' in df and 'Fuel_Burn_kg' in df:
            eff = df.groupby('Aircraft_Code')['Fuel_Burn_kg'].mean().reset_index()
            st.bar_chart(eff.set_index('Aircraft_Code'))
            st.write("### Fleet Fuel Burn Distribution")
            st.histogram(df['Fuel_Burn_kg'], bins=30)

        if 'Aircraft_Code' in df and 'CO2_kg' in df:
            st.write("### Table: Average CO₂ by Aircraft")
            co2 = df.groupby('Aircraft_Code')['CO2_kg'].mean().reset_index()
            st.dataframe(co2.sort_values('CO2_kg'))

        st.markdown("#### Recommendations")
        st.write("• Deploy newer, more efficient aircraft on high-density routes for best results.")
    else:
        st.info("No aircraft data available.")

app()
