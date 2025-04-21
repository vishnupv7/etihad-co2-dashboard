from utils.loader import load_data_safely

import streamlit as st
import pandas as pd
import plotly.express as px
import os

def app():
    st.title("✈️ Aircraft Efficiency Overview")
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(ROOT_DIR, "../data/processed/etihad_aircraft_fuel.csv")
    df = load_data_safely(file_path)
    if df is None:
        st.error('❌ Failed to load data.')
        return

    eff = df.groupby('Aircraft_Code')['Fuel_Burn_kg'].mean().reset_index()
    st.plotly_chart(px.bar(eff, x='Aircraft_Code', y='Fuel_Burn_kg', title='Avg Fuel Burn per Aircraft'))
