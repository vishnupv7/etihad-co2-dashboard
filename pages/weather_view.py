import streamlit as st
from utils.loader import unified_loader
import plotly.express as px

def app():
    mode = st.sidebar.radio("Data Mode", ["Historic", "Live"], index=0)
    df = unified_loader(mode.lower())

    st.title("⛅ Weather & Fuel Penalty Analysis")
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

app()
