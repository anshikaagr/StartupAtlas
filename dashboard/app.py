import streamlit as st

st.markdown("""
<style>
.block-container {
    padding-top: 2.2rem;
    padding-left: 0.5rem;
    padding-right: 0.5rem;
    max-width: 100% !important;
}
</style>
""", unsafe_allow_html=True)
st.markdown("""
# 🚀 StartupAtlas

Welcome to StartupAtlas.

Use the navigation menu on the left to explore:

- 🌍 Geographic Analysis
- 💰 Funding Analysis
- 🏭 Market Analysis
- 📈 Time Trends
- 🧬 Startup DNA Score
- 🔍 Startup Explorer
- ⚖️ Compare Countries

Apply global filters from the sidebar to customize analysis.
""")

st.info(
    "Dataset contains startup funding records from Crunchbase and covers startup activity primarily up to 2014."
)
st.warning(
    "📅 Note: Later years may contain fewer records in the dataset. Apparent declines after peak years can be influenced by dataset coverage rather than actual startup activity."
)

if "country_filter" not in st.session_state:
    st.session_state["country_filter"] = "All Countries"

if "market_filter" not in st.session_state:
    st.session_state["market_filter"] = "All Markets"


import pandas as pd

country_df = pd.read_csv("data/processed/country_summary.csv")

countries = ["All Countries"] + sorted(
    country_df["country_code"].dropna().unique().tolist()
)
market_df = pd.read_csv("data/processed/market_summary.csv")

markets = ["All Markets"] + sorted(
    market_df["market"].dropna().unique().tolist()
)

st.sidebar.header("🎛️ Global Filters")
st.session_state["country_filter"] = st.sidebar.selectbox(
    "Country",
    countries
)
st.session_state["market_filter"] = st.sidebar.selectbox(
    "Market",
    markets
)
