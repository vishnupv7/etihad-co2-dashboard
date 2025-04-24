import streamlit as st
from utils.data_loader import load_data
import traceback

try:
    from streamlit_autorefresh import st_autorefresh
except ImportError:
    pass

st.sidebar.title("Data Source Mode")
mode = st.sidebar.radio(
    "Choose data source for dashboard:",
    options=["Historical Data", "Live API"],
    index=0
)
mode_val = 'historical' if mode == "Historical Data" else 'live'

if mode_val == 'live':
    try:
        st_autorefresh(interval=60 * 1000, key="datarefresh")
        st.info("⏱️ Live mode: dashboard auto-refreshes every 60s.")
    except Exception:
        st.warning("Auto-refresh not available (streamlit-autorefresh not installed).")

@st.cache_data
def get_dashboard_data(mode_val):
    try:
        if mode_val == 'historical':
            df = load_data('final_dashboard_sample.csv', mode=mode_val)
        else:
            df = load_data('live_combined.csv', mode=mode_val)
        return df
    except Exception as e:
        st.warning(f"Failed to load {mode_val} data. Falling back to historical.\n{e}")
        try:
            df = load_data('final_dashboard_sample.csv', mode='historical')
            return df
        except Exception as e2:
            st.error(f"Failed to load fallback data: {e2}")
            return None

df = get_dashboard_data(mode_val)
if df is not None:
    st.success(f"Loaded {mode.upper()} data. Shape: {df.shape}")
    # Example: call a module
    import pages.route_view as route_view
    route_view.app(mode_val)
else:
    st.error("No data available for display.")
