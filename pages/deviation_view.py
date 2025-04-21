import streamlit as st
import pandas as pd

def app(df):
    required = ['Deviation_km', 'Callsign']
    if df.empty or not all(col in df.columns for col in required):
        st.error('❌ Final dashboard dataset not loaded.')
        return
    st.metric('Deviated Flights', df[df['Deviation_km'] > 0].shape[0])
