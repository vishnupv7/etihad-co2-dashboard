import streamlit as st
from utils.loader import unified_loader

def app():
    mode = st.session_state.get("mode", "Historic")
    df = unified_loader(mode.lower())

    st.title("🔀 Route Deviations & Holding Patterns")
    if df is not None and not df.empty:
        if 'Deviation_km' in df.columns:
            deviated = df[df['Deviation_km'] > 0]
            st.metric("Deviated Flights", len(deviated))
            st.dataframe(deviated[['callsign','Origin','Destination','Deviation_km','Fuel_Burn_kg','CO2_kg']].head())
            st.histogram(deviated['Deviation_km'], bins=20)
            st.write("• Flights with major deviations should be prioritized for review.")
        else:
            st.info("Deviation data not found in current dataset.")
    else:
        st.info("No deviation data available.")

app()
