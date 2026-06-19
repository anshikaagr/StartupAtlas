import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🏭 Market Analysis")
st.write("Explore startup activity and funding across markets.")

market_df = pd.read_csv("data/processed/market_summary.csv")
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
total_markets = market_df["market"].nunique()

avg_funding = market_df["avg_funding"].mean()

top_market = (
    market_df.sort_values("startups", ascending=False).iloc[0]["market"]
)
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🏭 Markets", total_markets)

with col2:
    st.metric("💰 Avg Funding", f"${avg_funding/1e6:.1f}M")

with col3:
    st.metric("🏆 Top Market", top_market)

st.markdown("---")
col1, col2 = st.columns(2)
with col1:

    st.subheader("Top Markets by Startups")

    top_markets = (
        market_df
        .sort_values("startups", ascending=False)
        .head(10)
    )

    fig1 = px.bar(
        top_markets,
        x="startups",
        y="market",
        orientation="h"
    )

    st.plotly_chart(fig1, use_container_width=True)

with col2:

    st.subheader("Top Markets by Funding")

    top_funded = (
        market_df
        .sort_values("total_funding", ascending=False)
        .head(10)
    )

    fig2 = px.bar(
        top_funded,
        x="total_funding",
        y="market",
        orientation="h"
    )

    st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")

st.subheader("Top Markets by Average Funding")

top_avg = (
    market_df
    .sort_values("avg_funding", ascending=False)
    .head(15)
)

fig3 = px.bar(
    top_avg,
    x="avg_funding",
    y="market",
    orientation="h"
)

st.plotly_chart(fig3, use_container_width=True)

