
from fastapi import APIRouter
import pandas as pd

router = APIRouter()

@router.get("/get-dashboard-data")
def get_data():
    df = pd.read_csv("data/processed/final_dashboard_sample.csv")
    return df.sample(10).to_dict(orient="records")
    