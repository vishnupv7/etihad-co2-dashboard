import os
import pandas as pd

def load_data_safely(filepath, dtype_override=None):
    """Safely load a CSV file and return a DataFrame or None if it fails."""
    if not os.path.exists(filepath):
        return None

    try:
        if dtype_override:
            df = pd.read_csv(filepath, dtype=dtype_override)
        else:
            df = pd.read_csv(filepath, low_memory=False)
        return df
    except Exception as e:
        print(f"Failed to load {filepath} — {e}")
        return None