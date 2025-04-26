import streamlit as st
from utils.loader import unified_loader

def app():
    mode = st.session_state.get("mode", "Historic")
    df = unified_loader(mode.lower())
    st.title("🔀 Route Deviations & Holding Patterns")
    st.write(df.head())
app()