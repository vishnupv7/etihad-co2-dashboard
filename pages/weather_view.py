# pages/weather_view.py

import streamlit as st
import pandas as pd
import plotly.express as px

def app():
    st.title("⛅ Weather & Fuel Penalty Analysis")
    df = pd.read_csv('data/processed/final_dashboard_sample.csv')

    st.write("### Fuel Burn vs. Weather Penalty")
    fig = px.scatter(df, x='Weather_Penalty_Index', y='Fuel_Burn_kg', color='CO2_kg',
                     title="Fuel Burn vs Weather Penalty Index")
    st.plotly_chart(fig)

    st.write("### Weather Penalty Histogram")
    st.histogram(df['Weather_Penalty_Index'], bins=20)

    st.write("### Correlation Matrix")
    st.dataframe(df[['Fuel_Burn_kg','CO2_kg','Weather_Penalty_Index','temp','wind','pressure']].corr())

    st.markdown("#### Insights")
    st.write("• Significant wind/temperature penalties can be seen during high CO₂ flights.")
