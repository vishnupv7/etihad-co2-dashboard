import streamlit as st
from utils.loader import unified_loader
import plotly.express as px

def app():
    df = unified_loader(st.session_state["mode"].lower())

    st.title("⛅ Weather & Fuel Penalty Analysis")
    st.write("### Fuel Burn vs. Weather Penalty")
    if 'Weather_Penalty_Index' in df.columns and 'Fuel_Burn_kg' in df.columns:
        fig = px.scatter(df, x='Weather_Penalty_Index', y='Fuel_Burn_kg', color='CO2_kg',
                         title="Fuel Burn vs Weather Penalty Index")
        st.plotly_chart(fig)

    st.write("### Weather Penalty Histogram")
    if 'Weather_Penalty_Index' in df.columns:
        st.histogram(df['Weather_Penalty_Index'], bins=20)

    st.write("### Correlation Matrix")
    cols = ['Fuel_Burn_kg','CO2_kg','Weather_Penalty_Index','temp','wind','pressure']
    st.dataframe(df[[col for col in cols if col in df.columns]].corr())

    st.markdown("#### Insights")
    st.write("• Significant wind/temperature penalties can be seen during high CO₂ flights.")
