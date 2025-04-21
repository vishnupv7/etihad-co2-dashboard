
import streamlit as st
import pandas as pd
import plotly.express as px

def app(df):
    if df.empty:
        st.error("❌ Data not loaded.")
        return

    st.title("⛅ Weather Impact")
    required_cols = ['Weather_Penalty_Index', 'Adjusted_Fuel_Burn_kg']
    if all(col in df.columns for col in required_cols):
        fig = px.scatter(df, x='Weather_Penalty_Index', y='Adjusted_Fuel_Burn_kg',
                         title='Weather Penalty vs Adjusted Burn')
        st.plotly_chart(fig)
    else:
        st.warning(f"Missing columns: {set(required_cols) - set(df.columns)}")
