
import pandas as pd
df = pd.read_csv('data/processed/final_dashboard_sample.csv')
expected_columns = ['Weather_Penalty_Index', 'Deviation_km_y', 'esg_match_percent', 'Anomaly_Score', 'SHAP_Top_Feature']
missing = [col for col in expected_columns if col not in df.columns]
if missing:
    print('❌ Missing columns:', missing)
else:
    print('✅ All columns are present.')
    