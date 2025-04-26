import streamlit as st
from utils.loader import unified_loader
import plotly.express as px

def app():
    mode = st.session_state.get("mode", "Historic")
    df = unified_loader(mode.lower())

    st.title("⛅ Weather & Fuel Penalty Analysis")
    if df is not None and not df.empty:
        if 'Weather_Penalty_Index' in df and 'Fuel_Burn_kg' in df and 'CO2_kg' in df:
            st.write("### Fuel Burn vs. Weather Penalty")
            fig = px.scatter(df, x='Weather_Penalty_Index', y='Fuel_Burn_kg', color='CO2_kg',
                            title="Fuel Burn vs Weather Penalty Index")
            st.plotly_chart(fig)
            st.write("### Weather Penalty Histogram")
            st.histogram(df['Weather_Penalty_Index'], bins=20)
        else:
            st.info("Weather penalty or fuel data not found.")

        cor_cols = [c for c in ['Fuel_Burn_kg','CO2_kg','Weather_Penalty_Index','temp','wind','pressure'] if c in df]
        if len(cor_cols) > 1:
            st.write("### Correlation Matrix")
            st.dataframe(df[cor_cols].corr())
        else:
            st.info("Not enough columns for correlation matrix.")

        st.markdown("#### Insights")
        st.write("• Significant wind/temperature penalties can be seen during high CO₂ flights.")
    else:
        st.info("No weather data available.")

app()
