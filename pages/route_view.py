import streamlit as st
import pandas as pd
import plotly.express as px

def app(df):
    if df is None or df.empty:
        st.error("❌ Final dashboard dataset not loaded.")
        return

    st.title("🗺️ Route Overview")
    df["Route"] = df["Origin"] + " → " + df["Destination"]

    if all(col in df.columns for col in ["Origin_Lat", "Origin_Lon"]):
        st.map(df[["Origin_Lat", "Origin_Lon"]].dropna())

    route_stats = df["Route"].value_counts().reset_index()
    route_stats.columns = ["Route", "Flights"]
    st.plotly_chart(px.bar(route_stats.head(10), x="Route", y="Flights", title="Top 10 Routes"))
