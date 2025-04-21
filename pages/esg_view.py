from utils.loader import load_data_safely

import streamlit as st
import pandas as pd
import plotly.express as px
import os

def app(df):

    st.title("♻️ ESG View")
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(ROOT_DIR, "../data/processed/etihad_ml_anomaly_flags_esg_aligned.csv")
    df = load_data_safely(file_path)
    if df is None:
        st.error('❌ Failed to load data.')
        return

    esg_levels = pd.cut(df['esg_match_percent'], [0, 80, 90, 100], labels=["Low", "Med", "High"])
    esg_summary = esg_levels.value_counts().reset_index()
    st.plotly_chart(px.bar(esg_summary, x='index', y='count', title='ESG Band Overview'))
