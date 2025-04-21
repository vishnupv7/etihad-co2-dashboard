from utils.loader import load_data_safely

import streamlit as st
import pandas as pd
import plotly.express as px
import os

def app():
    st.title("🔀 Deviation Insights")
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(ROOT_DIR, "../data/processed/etihad_with_deviation_tags.csv")
    df = load_data_safely(file_path)
    if df is None:
        st.error('❌ Failed to load data.')
        return

    st.metric("🧭 Deviated Flights", df[df['Deviation_km'] > 0].shape[0])
    dev_origin = df[df['Deviation_km'] > 0]['Origin'].value_counts().reset_index()
    st.plotly_chart(px.bar(dev_origin, x='index', y='Origin', title='Top Deviation Origins'))
