import pandas as pd
import numpy as np

# === CONFIGURE DEFAULTS OR LOOKUPS AS NEEDED ===
DEFAULT_AIRCRAFT = "B77W"
DEFAULT_ENGINE = "GE90-115B"
DEFAULT_SEAT_COUNT = 368
DEFAULT_EST_PASSENGERS = 294

def engineer_live_features(live_path, output_path=None):
    # Load minimal live data
    live = pd.read_csv(live_path)
    
    # --- Map/calculate all required features ---
    live['Aircraft_Code'] = DEFAULT_AIRCRAFT
    live['Engine_Code'] = DEFAULT_ENGINE
    live['Seat_Count'] = DEFAULT_SEAT_COUNT
    live['Estimated_Passengers'] = DEFAULT_EST_PASSENGERS
    
    # Example weather penalty feature (tweak as per your model logic)
    live['Weather_Penalty_Index'] = live['wind'] * 0.02 + np.maximum(0, (30 - live['temp'])) * 0.01

    # Add other engineered/required columns as zeros or suitable logic
    live['Altitude_Drift'] = 0
    live['Unplanned_Reroute'] = 0
    live['Holding_Loop_Detected'] = 0
    live['Adjusted_Fuel_Burn_kg'] = 0
    live['Adjusted_CO2_kg'] = 0
    live['RTK'] = 0
    live['CO2_per_RTK'] = 0
    live['Predicted_CO2_per_RTK'] = 0
    live['Yield_USD_per_RPK'] = 0

    # (Add/adjust more features if your model expects)
    
    # Reorder columns for model (adjust this list as per your model’s training set)
    features_for_model = [
        'Aircraft_Code', 'Engine_Code', 'Seat_Count', 'Estimated_Passengers',
        'Weather_Penalty_Index', 'Altitude_Drift', 'Unplanned_Reroute',
        'Holding_Loop_Detected', 'Adjusted_Fuel_Burn_kg', 'Adjusted_CO2_kg',
        'RTK', 'CO2_per_RTK', 'Predicted_CO2_per_RTK', 'Yield_USD_per_RPK'
    ] + [col for col in live.columns if col not in [
        'Aircraft_Code', 'Engine_Code', 'Seat_Count', 'Estimated_Passengers',
        'Weather_Penalty_Index', 'Altitude_Drift', 'Unplanned_Reroute',
        'Holding_Loop_Detected', 'Adjusted_Fuel_Burn_kg', 'Adjusted_CO2_kg',
        'RTK', 'CO2_per_RTK', 'Predicted_CO2_per_RTK', 'Yield_USD_per_RPK'
    ]]

    live = live[features_for_model]
    
    # Save engineered live file if path given
    if output_path:
        live.to_csv(output_path, index=False)
        print(f"Engineered live features saved to: {output_path}")

    return live

# === Usage Example ===
if __name__ == "__main__":
    engineered = engineer_live_features(
        live_path='/content/drive/MyDrive/Etihad_CO2_Optimization/etihad-co2-dashboard/data/live/live_combined.csv',
        output_path='/content/drive/MyDrive/Etihad_CO2_Optimization/etihad-co2-dashboard/data/live/live_engineered.csv'
    )
    print(engineered.head())
