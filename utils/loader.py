import pandas as pd
import os
import streamlit as st

def load_data_safely(filename):
    try:
        file_path = os.path.join(os.path.dirname(__file__), '..', filename)
        file_path = os.path.abspath(file_path)

        if not os.path.exists(file_path):
            st.error(f"🚫 File not found at path: {file_path}")
            return pd.DataFrame()  # Return empty DataFrame
        
        return pd.read_csv(file_path)
    except Exception as e:
        st.error(f"❌ Error loading dataset: {e}")
        return pd.DataFrame()
