import pandas as pd
import os

def load_dashboard_data():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.abspath(os.path.join(base_dir, "../data/processed/final_dashboard_dataset.csv"))
    return pd.read_csv(csv_path, low_memory=False)
