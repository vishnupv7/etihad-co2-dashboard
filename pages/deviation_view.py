import streamlit as st
import pandas as pd

def app(df):
    required = ['Deviation_km_y', 'Callsign']
    if df.empty or not all(col in df.columns for col in required):
        st.error('❌ Final dashboard dataset not loaded.')
        return

    st.metric("🧭 Deviated Flights", df[df['Deviation_km_y'] > 0].shape[0])
    st.dataframe(df[df['Deviation_km_y'] > 0][['Callsign', 'Deviation_km_y']])
