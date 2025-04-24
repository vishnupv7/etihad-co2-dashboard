# utils/loader.py

import pandas as pd

def unified_loader(mode='historic'):
    if mode == 'historic':
        path = 'data/processed/final_dashboard_merged.csv'
    else:
        path = 'data/live/live_combined.csv'
    df = pd.read_csv(path, low_memory=False)
    df.columns = [c.strip() for c in df.columns]
    return df
