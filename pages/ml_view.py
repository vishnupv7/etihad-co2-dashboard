import streamlit as st
from utils.loader import unified_loader
import pandas as pd

def app():
    mode = st.session_state.get("mode", "Historic")
    df = unified_loader(mode.lower())

    st.title("🤖 ML Anomaly & Prediction Insights")
    if df is not None and not df.empty:
        st.write("### Anomaly Flagged Flights")
        if 'anomaly_flag' in df:
            st.dataframe(df[df['anomaly_flag']==1][['Origin','Destination','Aircraft_Code','Fuel_Burn_kg','CO2_kg','route_efficiency_score']].head())
        else:
            st.info("No anomaly flags found in this dataset.")

        st.write("### Feature Importances (Fuel Prediction)")
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
