import streamlit as st
import pandas as pd
import plotly.express as px

st.title("💰 Funding Analysis")
st.write("Analyze startup funding patterns and investment trends.")

country_df = pd.read_csv("data/processed/country_summary.csv")
market_df = pd.read_csv("data/processed/market_summary.csv")
funding_df = pd.read_csv("data/processed/funding_summary.csv")

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

st.markdown("""
    <div style="
        background-color:#DCFCE7;
        padding:15px;
        border-radius:12px;
        border-left:6px solid #10B981;
        color:#166534;
        font-weight:500;">
    💰 Global startup funding exceeds $625B. 
    🏆 Biotechnology leads all markets in total funding. 
    📈 Average funding per startup is $14M.
""", unsafe_allow_html=True)

st.markdown("---")

st.subheader("Funding Trend Over Time")

fig = px.line(
    funding_df,
    x="founded_year",
    y="total_funding",
    markers=True,
    color_discrete_sequence=["#10B981"]
)
fig.update_traces(line_width=3)
fig.update_layout(
    height=450,
    xaxis_title="Year",
    yaxis_title="Funding (USD)",
    hovermode="x unified"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

st.subheader("🏆 Top 10 Markets by Funding")

top_funding_markets = (
    market_df
    .sort_values("total_funding", ascending=False)
    .head(10)
)

fig2 = px.bar(
    top_funding_markets,
    x="total_funding",
    y="market",
    orientation="h",
    color="total_funding",
    color_continuous_scale="Greens"
)

fig2.update_layout(
    height=450,
    yaxis_title="Market",
    xaxis_title="Total Funding (USD)"
)

st.plotly_chart(
    fig2,
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

    fig1 = px.treemap(
    top_markets,
    path=["market"],
    values="total_funding",
    color="total_funding",
    color_continuous_scale=[
    "#353A33",
    "#5E785A",
    "#64886C",
    "#7DD4A7",
    "#AFF6D1"
    ]
)

    fig1.update_layout(
        height=450
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
        orientation="h",
        color_discrete_sequence=["#086E2D"]
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

st.markdown("---")
st.subheader("📌 Funding Insights")

st.success(
    f"🏆 {top_market} attracted the highest funding."
)

st.info(
    f"💰 Total startup funding reached ${total_funding/1e9:.1f}B."
)

st.info(
    f"📈 Average funding per startup is ${avg_funding/1e6:.1f}M."
)