import streamlit as st
import pandas as pd
import plotly.express as px

def app(df):
    if df is None or df.empty or 'Anomaly_Score' not in df.columns:
        st.error("❌ Anomaly data not available in current dataset.")
        return

    st.title("📉 ML Anomaly Detection")
    st.metric("🔺 High Anomaly Flights", df[df['Anomaly_Score'] > 0.5].shape[0])
    st.dataframe(df[df['Anomaly_Score'] > 0.5][['FlightDate', 'Callsign', 'Anomaly_Score']])

    shap = df['SHAP_Top_Feature'].value_counts().reset_index()
    st.plotly_chart(px.pie(shap, names="index", values="SHAP_Top_Feature", title="Top SHAP Contributors"))
