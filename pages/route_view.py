import streamlit as st
import pandas as pd
import plotly.express as px

def app(df):
    st.title("🗺️ Route Overview")

    if df is None or df.empty:
        st.error("❌ Final dashboard dataset not loaded.")
        return

    # Top 10 most frequent routes
    df['Route'] = df['Origin'] + " → " + df['Destination']
    route_counts = df['Route'].value_counts().reset_index()
    route_counts.columns = ['Route', 'Flight_Count']

    st.subheader("📍 Top Routes by Frequency")
    st.plotly_chart(
        px.bar(route_counts.head(10), x='Route', y='Flight_Count', title='Top 10 Most Frequent Routes')
    )

    st.dataframe(route_counts.head(20))  # Show a table too
