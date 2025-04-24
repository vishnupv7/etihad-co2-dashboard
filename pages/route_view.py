import streamlit as st
from utils.loader import unified_loader
import plotly.express as px

def app():
    df = unified_loader(st.session_state["mode"].lower())

    st.title("🌍 Route Network & Emissions")
    st.metric("Routes Tracked", df.groupby(['Origin','Destination']).ngroups)
    top_routes = df.groupby(['Origin','Destination']).agg({'Fuel_Burn_kg':'mean', 'CO2_kg':'mean', 'route_efficiency_score':'mean'}).reset_index()
    st.write("### Top 10 Routes by Avg Fuel Burn")
    st.dataframe(top_routes.sort_values('Fuel_Burn_kg',ascending=False).head(10))

    st.write("### Route Efficiency Boxplot")
    st.box_chart(df['route_efficiency_score'])

    st.write("### Route Map (Top 20)")
    if {'Origin', 'Destination', 'latitude', 'longitude'}.issubset(df.columns):
        top = df.head(20)
        fig = px.scatter_geo(top, lat='latitude', lon='longitude', color='Fuel_Burn_kg',
                             hover_name='callsign', title="Top Route Segments (approx)")
        st.plotly_chart(fig)
    else:
        st.info("Geographic route map will appear when location columns are present.")

app()
