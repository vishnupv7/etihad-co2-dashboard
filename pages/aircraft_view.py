import streamlit as st
import pandas as pd

def app(df):
    required = ['Aircraft_Code', 'Fuel_Burn_kg']
    if df.empty or not all(col in df.columns for col in required):
        st.error('❌ Final dashboard dataset not loaded.')
        return
    st.bar_chart(df.groupby('Aircraft_Code')['Fuel_Burn_kg'].mean())
