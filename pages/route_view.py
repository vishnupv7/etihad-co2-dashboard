import streamlit as st
from utils.data_loader import load_data

def app(mode_val):
    st.header("Route View")
    try:
        filename = 'final_dashboard_sample.csv' if mode_val == 'historical' else 'live_combined.csv'
        df = load_data(filename, mode=mode_val)
        st.write(df.head())
        st.success(f"Data loaded in {mode_val} mode. Shape: {df.shape}")
        # Example validation metrics
        mae = 42.0  # Replace with real value
        esg_match = 97.3  # Replace with real value
        col1, col2, col3 = st.columns(3)
        col1.metric("Current Mode", mode_val)
        col2.metric("Model MAE", f"{mae:.2f}")
        col3.metric("ESG Match %", f"{esg_match:.1f}%")
    except Exception as e:
        st.error(f"Failed to load data: {e}")
