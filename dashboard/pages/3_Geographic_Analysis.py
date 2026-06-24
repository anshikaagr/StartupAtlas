import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🌍 Geographic Analysis")
st.write("Explore startup distribution and funding across countries.")
country_df = pd.read_csv("data/processed/country_summary.csv")
st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
    padding-left: 0.5rem;
    padding-right: 0.5rem;
    max-width: 100% !important;
}
</style>
""", unsafe_allow_html=True)

total_countries = country_df["country_code"].nunique()

avg_funding = country_df["avg_funding"].mean()

top_country = (
    country_df
    .sort_values("startups", ascending=False)
    .iloc[0]["country_code"]
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🌍 Countries", total_countries)

with col2:
    st.metric("💰 Avg Funding", f"${avg_funding/1e6:.1f}M")

with col3:
    st.metric("🏆 Top Country", top_country)

st.markdown("---")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Top Startup Countries")

    top_countries = (
        country_df
        .sort_values("startups", ascending=False)
        .head(10)
    )

    fig = px.bar(top_countries,
        x="startups",
        y="country_code",
        orientation="h",
        color_discrete_sequence=["#C368F8"])

    st.plotly_chart(fig,use_container_width=True)

with col2:

    st.subheader("Top Funded Countries")

    top_funded = (
        country_df
        .sort_values("total_funding", ascending=False)
        .head(10)
    )

    fig2 = px.bar(
        top_funded,
        x="total_funding",
        y="country_code",
        orientation="h",
        color_discrete_sequence=["#5C76F6"]
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

st.markdown("---")

st.subheader("🚀 Top 15 Countries by Startups")

top15 = (
    country_df
    .sort_values("startups", ascending=False)
    .head(15)
)

fig3 = px.bar(
    top15,
    x="startups",
    y="country_code",
    orientation="h",
    color="startups",
    color_continuous_scale=[
        "#8B5CF6",
        "#6940CA",
        "#421A9F"
    ]
)

fig3.update_layout(
    height=500,
    yaxis_title="Country",
    xaxis_title="Number of Startups",
    yaxis=dict(categoryorder="total ascending")
)

st.plotly_chart(fig3, use_container_width=True)

st.markdown("---")

region_map = {
    # North America
    "USA": "North America",
    "CAN": "North America",

    # South America
    "BRA": "South America",
    "ARG": "South America",
    "CHL": "South America",

    # Europe
    "GBR": "Europe",
    "FRA": "Europe",
    "DEU": "Europe",
    "ESP": "Europe",
    "NLD": "Europe",
    "SWE": "Europe",
    "CHE": "Europe",
    "RUS": "Europe",

    # East Asia
    "CHN": "East Asia",
    "JPN": "East Asia",
    "KOR": "East Asia",
    "TWN": "East Asia",

    # South Asia
    "IND": "South Asia",
    "PAK": "South Asia",
    "BGD": "South Asia",

    # Middle East
    "ISR": "Middle East",
    "SAU": "Middle East",
    "ARE": "Middle East",

    # Oceania
    "AUS": "Oceania",
    "NZL": "Oceania",

    # Africa
    "ZAF": "Africa",
    "EGY": "Africa",
    "NGA": "Africa"
}

country_df["region"] = (
    country_df["country_code"]
    .map(region_map)
    .fillna("Other")
)

region_df = (
    country_df
    .groupby("region")["startups"]
    .sum()
    .reset_index()
)

fig4 = px.treemap(
    region_df,
    path=["region"],
    values="startups",
    color="startups",
    color_continuous_scale=[
        "#8B5CF6",  # Purple
        "#3B82F6",  # Blue
        "#06B6D4",  # Cyan
        "#10B981",  # Emerald
        "#F59E0B",  # Amber
        "#EF4444",  # Red
        "#EC4899",  # Pink
        "#6366F1" 
    ]
)

fig4.update_layout(
    height=500,
    margin=dict(t=20, l=0, r=0, b=0)
)

st.plotly_chart(fig4, use_container_width=True)

st.markdown("---")
st.subheader("📌 Geographic Insights")

st.info("🇺🇸 USA dominates both startup count and total funding.")
st.info("🌍 Startup activity is concentrated in North America, Europe, and Asia.")
st.info("💰 Funding distribution varies significantly across countries.")