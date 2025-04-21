from utils.loader import load_data_safely

def app():
    path = "/content/drive/MyDrive/Etihad_CO2_Optimization/data/processed/final_dashboard_dataset.csv"
    df = load_data_safely(path)
    if df is None:
        st.error("❌ Final dashboard dataset not loaded.")
        return

    st.title("🗺️ Route Overview")

    # ✅ Only show flights with valid lat/lon
    if all(col in df.columns for col in ["Origin_Lat", "Origin_Lon"]):
        st.map(df[["Origin_Lat", "Origin_Lon"]].dropna().rename(columns={
            "Origin_Lat": "lat",
            "Origin_Lon": "lon"
        }).head(100))
    else:
        st.warning("⚠️ Latitude/Longitude data not available for mapping.")

    st.write("📍 Top routes (sample):")
    st.dataframe(df[["Flight_ID", "Origin", "Destination"]].head(10))
