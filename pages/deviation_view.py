import streamlit as st
from utils.loader import unified_loader

def app():
    df = unified_loader(st.session_state["mode"].lower())

    st.title("🔀 Route Deviations & Holding Patterns")
    if 'Deviation_km' in df.columns:
        deviated = df[df['Deviation_km'] > 0]
        st.metric("Deviated Flights", len(deviated))
        st.dataframe(deviated[['callsign','Origin','Destination','Deviation_km','Fuel_Burn_kg','CO2_kg']].head())
        st.histogram(deviated['Deviation_km'], bins=20)
        st.write("• Flights with major deviations should be prioritized for review.")
    else:
        st.info("Deviation data not found in current dataset.")

app()
