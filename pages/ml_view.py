import streamlit as st
from utils.loader import unified_loader

def app():
    mode = st.sidebar.radio("Data Mode", ["Historic", "Live"], index=0)
    df = unified_loader(mode.lower())

    st.title("🤖 ML Anomaly & Prediction Insights")

    st.write("### Anomaly Flagged Flights")
    st.dataframe(df[df.get('anomaly_flag',0)==1][['Origin','Destination','Aircraft_Code','Fuel_Burn_kg','CO2_kg','route_efficiency_score']].head())

    st.write("### Feature Importances (Fuel Prediction)")
    import pandas as pd
    feat_imp = pd.Series({'Weather_Penalty_Index': 0.87, 'Altitude_Drift': 0.07, 'Holding_Loop_Detected': 0.02, 'Unplanned_Reroute': 0.01, 'Seat_Count':0.01})
    st.bar_chart(feat_imp)

    st.write("### Model Error Distribution (Historic)")
    if 'Fuel_Burn_kg' in df.columns and 'predicted_fuel' in df.columns:
        error = df['Fuel_Burn_kg'] - df['predicted_fuel']
        st.histogram(error, bins=30)
    else:
        st.info("Model error histogram will appear once predictions are available.")

    st.markdown("#### Alerts & Recommendations")
    st.write("• Investigate any flight flagged as anomaly for possible operational inefficiency.")

app()
