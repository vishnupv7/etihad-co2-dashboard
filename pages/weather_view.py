import streamlit as st
import plotly.express as px
import pandas as pd

def app(df):
    required = ['Weather_Penalty_Index', 'Adjusted_Fuel_Burn_kg']
    if df.empty or not all(col in df.columns for col in required):
        st.error('❌ Final dashboard dataset not loaded.')
        return
    st.plotly_chart(px.scatter(df, x='Weather_Penalty_Index', y='Adjusted_Fuel_Burn_kg'))