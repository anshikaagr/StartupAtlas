import streamlit as st

st.set_page_config(
    page_title="StartupAtlas",
    page_icon="🚀",
    layout="wide"
)
st.sidebar.markdown("""
<div style="
padding:5px;
border-radius:12px;
background:#1F2937;
text-align:center;
margin-bottom:10px;">
<h2>🚀 StartupAtlas</h2>
<p>Startup Intelligence Platform</p>
</div>
""", unsafe_allow_html=True)

st.title("🚀 StartupAtlas")
st.caption("Data-driven insights into the global startup ecosystem.")

if "country_filter" not in st.session_state:
    st.session_state["country_filter"] = "All Countries"

if "market_filter" not in st.session_state:
    st.session_state["market_filter"] = "All Markets"

st.markdown("""
<style>
[data-testid="stSidebar"] {
    background: #111827;
}

[data-testid="stSidebar"] * {
    color: white;
}
</style>
""", unsafe_allow_html=True)

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
