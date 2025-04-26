import streamlit as st
from utils.loader import unified_loader

def app():
    df = unified_loader(st.session_state["mode"].lower())

    st.title("✈️ Aircraft Efficiency Overview")
    if 'Aircraft_Code' in df.columns and 'Fuel_Burn_kg' in df.columns:
        eff = df.groupby('Aircraft_Code')['Fuel_Burn_kg'].mean().reset_index()
        st.bar_chart(eff.set_index('Aircraft_Code'))

        st.write("### Fleet Fuel Burn Distribution")
        st.histogram(df['Fuel_Burn_kg'], bins=30)

        st.write("### Table: Average CO₂ by Aircraft")
        co2 = df.groupby('Aircraft_Code')['CO2_kg'].mean().reset_index()
        st.dataframe(co2.sort_values('CO2_kg'))

    st.markdown("#### Recommendations")
    st.write("• Deploy newer, more efficient aircraft on high-density routes for best results.")
