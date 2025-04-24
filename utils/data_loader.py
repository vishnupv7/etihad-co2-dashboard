import os
import pandas as pd

def load_data(filename, mode='historical'):
    """
    Loads a CSV file from either /data/processed (historical) or /data/live (live mode).
    mode: 'historical' | 'live'
    """
    root = os.path.join(os.path.dirname(__file__), '..', 'data')
    folder = 'processed' if mode == 'historical' else 'live'
    file_path = os.path.abspath(os.path.join(root, folder, filename))
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} does not exist.")
    return pd.read_csv(file_path)
