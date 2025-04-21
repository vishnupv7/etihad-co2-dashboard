import streamlit as st
import pandas as pd

def app(df):
    required = ['Anomaly_Score', 'SHAP_Top_Feature']
    if df.empty or not all(col in df.columns for col in required):
        st.error('❌ Final dashboard dataset not loaded.')
        return
    st.write(df[['Anomaly_Score', 'SHAP_Top_Feature']].head())
