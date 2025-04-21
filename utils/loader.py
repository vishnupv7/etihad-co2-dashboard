import pandas as pd
import streamlit as st

def load_data_safely(filename: str):
    try:
        # If a GDrive ID is passed instead of a file path
        if filename.startswith("http"):

            st.info("📡 Loading from Google Drive link...")
            return pd.read_csv(filename)

        # Else: fallback to local file
        import os
        file_path = os.path.join(os.path.dirname(__file__), '..', filename)
        file_path = os.path.abspath(file_path)

        return pd.read_csv(file_path)
    except Exception as e:
        st.error(f"❌ Final dashboard dataset not loaded.\n\nReason: {e}")
        return pd.DataFrame()
