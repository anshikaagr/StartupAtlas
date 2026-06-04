import streamlit as st
import pandas as pd
import plotly.express as px

st.title("💰 Funding Analysis")
st.write("Analyze startup funding patterns and investment trends.")

country_df = pd.read_csv("data/processed/country_summary.csv")
market_df = pd.read_csv("data/processed/market_summary.csv")
funding_df = pd.read_csv("data/processed/funding_summary.csv")

total_funding = market_df["total_funding"].sum()

avg_funding = market_df["avg_funding"].mean()

top_market = (
    market_df
    .sort_values("total_funding", ascending=False)
    .iloc[0]["market"]
)
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("💰 Total Funding", f"${total_funding/1e9:.1f}B")

with col2:
    st.metric("📈 Avg Funding", f"${avg_funding/1e6:.1f}M")

with col3:
    st.metric("🏆 Top Market", top_market)

st.markdown("---")

st.subheader("Funding Trend Over Time")

fig = px.line(
    funding_df,
    x="founded_year",
    y="total_funding",
    markers=True
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")

col1, col2 = st.columns(2)
with col1:

    st.subheader("Top Funded Markets")

    top_markets = (
        market_df
        .sort_values("total_funding", ascending=False)
        .head(10)
    )

    fig1 = px.bar(
        top_markets,
        x="total_funding",
        y="market",
        orientation="h"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )
with col2:

    st.subheader("Top Funded Countries")

    top_countries = (
        country_df
        .sort_values("total_funding", ascending=False)
        .head(10)
    )

    fig2 = px.bar(
        top_countries,
        x="total_funding",
        y="country_code",
        orientation="h"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )