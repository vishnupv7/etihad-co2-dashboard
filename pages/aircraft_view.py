import streamlit as st
from utils.loader import unified_loader

def app():
    mode = st.sidebar.radio("Data Mode", ["Historic", "Live"], index=0)
    df = unified_loader(mode.lower())

    st.title("✈️ Aircraft Efficiency Overview")
    eff = df.groupby('Aircraft_Code')['Fuel_Burn_kg'].mean().reset_index()
    st.bar_chart(eff.set_index('Aircraft_Code'))

    st.write("### Fleet Fuel Burn Distribution")
    st.histogram(df['Fuel_Burn_kg'], bins=30)

    st.write("### Table: Average CO₂ by Aircraft")
    co2 = df.groupby('Aircraft_Code')['CO2_kg'].mean().reset_index()
    st.dataframe(co2.sort_values('CO2_kg'))

    st.markdown("#### Recommendations")
    st.write("• Deploy newer, more efficient aircraft on high-density routes for best results.")

app()
