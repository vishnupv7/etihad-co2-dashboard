
import streamlit as st
import pandas as pd
import plotly.express as px

def app(df):
    if df.empty or 'esg_match_percent' not in df.columns:
        st.error('❌ Failed to load ESG data or column missing.')
        return

    st.title("🌱 ESG Alignment")
    esg_levels = pd.cut(df['esg_match_percent'], [0, 80, 90, 100],
                        labels=["<80%", "80–90%", "90–100%"])
    esg_summary = esg_levels.value_counts().reset_index()
    esg_summary.columns = ['ESG Score Band', 'count']
    st.plotly_chart(px.bar(esg_summary, x='ESG Score Band', y='count', title='ESG Match Distribution'))
