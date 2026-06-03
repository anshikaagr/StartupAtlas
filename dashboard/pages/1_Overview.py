import streamlit as st
import pandas as pd
import plotly.express as px

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

st.markdown("---")

col1, col2 = st.columns(2)

with col1:

    st.subheader("Startup Status Distribution")

    fig = px.pie(
        status_df,
        names="status",
        values="count",
        hole=0.5
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with col2:

    st.subheader("Top 10 Markets")

    top_markets = (
        market_df
        .sort_values("startups", ascending=False)
        .head(10)
    )

    fig2 = px.bar(
        top_markets,
        x="startups",
        y="market",
        orientation="h"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )
