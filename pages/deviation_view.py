
import streamlit as st
import pandas as pd
import plotly.express as px

def app(df):
    if df.empty or 'Deviation_km' not in df.columns:
        st.error("❌ Deviation column missing.")
        return

    st.title("🔀 Deviation Insights")
    st.metric("🧭 Deviated Flights", df[df['Deviation_km'] > 0].shape[0])
    dev_origin = df[df['Deviation_km'] > 0]['Origin'].value_counts().reset_index()
    dev_origin.columns = ['Origin', 'count']
    st.plotly_chart(px.bar(dev_origin, x='Origin', y='count', title='Top Origins with Deviations'))
