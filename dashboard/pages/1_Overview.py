import streamlit as st
import pandas as pd

st.title("🏠 Overview")

country_df = pd.read_csv("data/processed/country_summary.csv")
market_df = pd.read_csv("data/processed/market_summary.csv")
status_df = pd.read_csv("data/processed/status_summary.csv")

total_startups = country_df["startups"].sum()
total_funding = country_df["total_funding"].sum()
total_countries = len(country_df)
total_markets = len(market_df)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("🚀 Startups", f"{total_startups:,}")

with col2:
    st.metric("💰 Funding", f"${total_funding/1e9:.1f}B")

with col3:
    st.metric("🌍 Countries", total_countries)

with col4:
    st.metric("🏭 Markets", total_markets)

