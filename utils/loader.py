import pandas as pd
import os
import streamlit as st

def load_data_safely(filename: str):
    base_path = os.path.dirname(__file__)  # this points to /utils
    file_path = os.path.join(base_path, "..", filename)
    file_path = os.path.abspath(file_path)

    try:
        return pd.read_csv(file_path)
    except Exception as e:
        st.error("❌ Final dashboard dataset not loaded.")
        st.stop()
