import streamlit as st
from utils.loader import unified_loader
import plotly.express as px

def app():
    mode = st.session_state.get("mode", "Historic")
    df = unified_loader(mode.lower())

    st.title("🌍 Route Network & Emissions")
    if df is not None and not df.empty:
        if {'Origin', 'Destination'}.issubset(df.columns):
            st.metric("Routes Tracked", df.groupby(['Origin','Destination']).ngroups)
            top_routes = df.groupby(['Origin','Destination']).agg({'Fuel_Burn_kg':'mean', 'CO2_kg':'mean', 'route_efficiency_score':'mean'}).reset_index()
            st.write("### Top 10 Routes by Avg Fuel Burn")
            st.dataframe(top_routes.sort_values('Fuel_Burn_kg',ascending=False).head(10))
        else:
            st.info("Route columns not found.")

        st.write("### Route Efficiency Boxplot")
        if 'route_efficiency_score' in df:
            st.box_chart(df['route_efficiency_score'])
        else:
            st.info("Route efficiency scores not found.")

        st.write("### Route Map (Top 20)")
        geo_cols = {'Origin', 'Destination', 'latitude_1', 'longitude_1'}
        if geo_cols.issubset(df.columns):
            top = df.head(20)
            fig = px.scatter_geo(top, lat='latitude_1', lon='longitude_1', color='Fuel_Burn_kg',
                                 hover_name='callsign' if 'callsign' in top.columns else None,
                                 title="Top Route Segments (approx)")
            st.plotly_chart(fig)
        else:
            st.info("Geographic route map will appear when location columns are present.")

app()
