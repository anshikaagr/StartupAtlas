import streamlit as st

st.set_page_config(
    page_title="StartupAtlas",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 StartupAtlas")
st.caption("Data-driven insights into the global startup ecosystem.")

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

st.session_state
st.session_state["country_filter"]
st.session_state["market_filter"]
