# Etihad CO₂ Optimization Dashboard

## Data Modes

This dashboard works in two modes:

- **Historical Data Mode:** Loads from /data/processed/ (for demo, benchmarking, and model validation)
- **Live API Mode:** Loads from /data/live/ (for real-time dashboard and analytics)

Use the sidebar toggle to switch between modes. In live mode, the dashboard auto-refreshes every 60 seconds.

## Model Validation

Each dashboard run displays:
- Current Data Mode
- Model MAE (Mean Absolute Error)
- ESG Match % (comparison to Etihad/ICAO benchmark)
