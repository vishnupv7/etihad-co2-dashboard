from utils.loader import load_data_safely

import streamlit as st
import pandas as pd
import plotly.express as px
import os

def app():
    st.title("🌦️ Weather Impact Insights")
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(ROOT_DIR, "../data/processed/etihad_weather_adjusted.csv")
    df = load_data_safely(file_path)
    if df is None:
        st.error('❌ Failed to load data.')
        return

    st.plotly_chart(px.scatter(df, x='Weather_Penalty_Index', y='Adjusted_Fuel_Burn_kg',
                               title='Weather Penalty vs Adjusted Burn'))
