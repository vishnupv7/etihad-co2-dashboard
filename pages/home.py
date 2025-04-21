import streamlit as st

def app(df):
    st.title("🏠 Etihad CO₂ Dashboard – Home")

    st.metric("✈️ Total Flights", len(df))

    if 'CO2_per_RTK' in df.columns:
        st.metric("🌍 Avg CO₂ per RTK", round(df['CO2_per_RTK'].mean(), 2))
    else:
        st.warning("⚠️ Column missing: CO2_per_RTK")

    if 'esg_match_percent' in df.columns:
        st.metric("✅ ESG Match %", f"{round(df['esg_match_percent'].mean(), 1)}%")
    else:
        st.warning("⚠️ Column missing: esg_match_percent")

    st.subheader("📈 CO₂ Emission Trends")

    if 'FlightDate' in df.columns and 'Total_Emissions' in df.columns:
        df['FlightDate'] = pd.to_datetime(df['FlightDate'])
        daily = df.groupby(df['FlightDate'].dt.date)['Total_Emissions'].sum().reset_index()
        st.line_chart(daily.set_index('FlightDate'))
    else:
        st.warning("📉 Emission trend data not available.")
