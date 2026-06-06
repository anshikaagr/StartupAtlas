import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🔍 Startup Explorer")
st.write("Explore startup ecosystems by country.")

country_df = pd.read_csv("data/processed/country_summary.csv")

selected_country = st.selectbox(
    "Select Country",sorted(country_df["country_code"].unique())
)
country_data = country_df[country_df["country_code"] == selected_country]

st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "🚀 Startups",
        int(country_data["startups"].iloc[0])
    )

with col2:
    st.metric(
        "💰 Total Funding",
        f"${country_data['total_funding'].iloc[0]/1e9:.2f}B"
    )

with col3:
    avg_funding = country_data["avg_funding"].iloc[0]

    if pd.isna(avg_funding):
        avg_funding = 0

    st.metric(
        "📈 Avg Funding",
        f"${avg_funding/1e6:.2f}M"
    )