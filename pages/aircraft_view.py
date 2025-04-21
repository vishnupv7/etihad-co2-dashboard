
import streamlit as st
import pandas as pd
import plotly.express as px

def app(df):
    if df.empty or 'Aircraft_Code' not in df.columns:
        st.error("❌ Aircraft data missing.")
        return

    st.title("✈️ Aircraft Efficiency Overview")
    eff = df.groupby('Aircraft_Code')['Fuel_Burn_kg'].mean().reset_index()
    st.plotly_chart(px.bar(eff, x='Aircraft_Code', y='Fuel_Burn_kg', title='Avg Fuel Burn per Aircraft'))
