
import streamlit as st
import pandas as pd
import plotly.express as px

def app(df):
    if df.empty:
        st.error("❌ Data not loaded.")
        return

    st.title("📉 ML Anomaly Detection")
    high_anomaly = df[df['Anomaly_Score'] > 0.5]
    st.metric("🔺 High Anomaly Flights", high_anomaly.shape[0])
    st.dataframe(high_anomaly[['FlightDate', 'Callsign', 'Anomaly_Score', 'Model_Confidence']])

    shap = df['SHAP_Top_Feature'].value_counts().reset_index()
    shap.columns = ['SHAP_Top_Feature', 'count']
    st.plotly_chart(px.pie(shap, names="SHAP_Top_Feature", values="count", title="SHAP Top Feature Breakdown"))
