# pages/deviation_view.py

import streamlit as st
import pandas as pd

def app():
    st.title("🔀 Route Deviations & Holding Patterns")
    df = pd.read_csv('data/processed/final_dashboard_sample.csv')
    if 'Deviation_km' in df.columns:
        deviated = df[df['Deviation_km'] > 0]
        st.metric("Deviated Flights", len(deviated))
        st.dataframe(deviated[['callsign','Origin','Destination','Deviation_km','Fuel_Burn_kg','CO2_kg']].head())
        st.histogram(deviated['Deviation_km'], bins=20)
        st.write("• Flights with major deviations should be prioritized for review.")
    else:
        st.info("Deviation data not found in current dataset.")
