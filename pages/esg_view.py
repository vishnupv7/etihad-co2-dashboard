import streamlit as st
import pandas as pd

def app(df):
    required = ['esg_match_percent']
    if df.empty or not all(col in df.columns for col in required):
        st.error('❌ Final dashboard dataset not loaded.')
        return
    st.write(df['esg_match_percent'].describe())
