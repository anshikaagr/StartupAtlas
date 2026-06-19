import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🏠 Overview")
st.caption(
    "Explore global startup trends, funding activity, market performance, and ecosystem strength."
)

country_df = pd.read_csv("data/processed/country_summary.csv")
market_df = pd.read_csv("data/processed/market_summary.csv")
status_df = pd.read_csv("data/processed/status_summary.csv")

st.markdown("""
<style>
.block-container {
    padding-top: 2.2rem;
    padding-left: 2rem;
    padding-right: 2rem;
    max-width: 100% !important;
}
</style>
""", unsafe_allow_html=True)

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

    st.subheader("📊 Startup Status Distribution")

    fig = px.pie(
        status_df,
        names="status",
        values="count",
        hole=0.5
    )
    fig.update_layout(
        height=350,
        margin=dict(l=10, r=10, t=20, b=10)
    )
    st.plotly_chart(
        fig,
        use_container_width=True
    )

with col2:

    st.subheader("🏭 Top 10 Markets")

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
    fig2.update_layout(
        height=350,
        margin=dict(l=10, r=10, t=20, b=10)
    )
    st.plotly_chart(
        fig2,
        use_container_width=True
    )

st.divider()

col3, col4 = st.columns(2)

with col3:

    st.subheader("📈 Funding Trend Over Time")

    funding_df = pd.read_csv(
        "data/processed/funding_summary.csv"
    )

    fig3 = px.line(
        funding_df,
        x="founded_year",
        y="total_funding",
        markers=True
    )
    fig3.update_layout(
        height=350,
        margin=dict(l=10, r=10, t=20, b=10)
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

with col4:

    st.subheader("🌍 Top 10 Countries")

    top_countries = (
        country_df
        .sort_values("startups", ascending=False)
        .head(10)
    )

    fig4 = px.bar(
        top_countries,
        x="startups",
        y="country_code",
        orientation="h"
    )
    fig4.update_layout(
        height=350,
        margin=dict(l=10, r=10, t=20, b=10)
    )
    st.plotly_chart(
        fig4,
        use_container_width=True
    )

st.markdown("---")
st.subheader("📌 Key Insights")

st.info("🌍 USA leads the startup ecosystem in funding and startup count.")
st.info("🏭 Software-related markets dominate the startup landscape.")
st.info("📈 Startup funding experienced significant growth over time.")
st.info("🧬 Countries with strong funding and startup activity achieve the highest DNA Scores.")