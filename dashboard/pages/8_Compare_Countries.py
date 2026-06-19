import streamlit as st
import pandas as pd
import plotly.express as px

st.title("⚖️ Compare Countries")
st.write("Compare startup ecosystems across countries.")

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

country_df["avg_funding"] = (country_df["avg_funding"].fillna(0))

country_df["dna_score"] = (
    country_df["startups"].rank(pct=True) * 40 +
    country_df["total_funding"].rank(pct=True) * 40 +
    country_df["avg_funding"].rank(pct=True) * 20
)

col1, col2 = st.columns(2)

with col1:
    country_options = sorted(
        country_df["country_code"].unique()
    )

    default_index = 0

    selected_filter = st.session_state.get(
    "country_filter",
    "All Countries"
    )

    if selected_filter in country_options:
        default_index = country_options.index(
            selected_filter
    )

    country1 = st.selectbox(
        "Country 1",
        country_options,
        index=default_index
    )

with col2:
    country2 = st.selectbox(
        "Country 2",
        sorted(country_df["country_code"].unique()),
        index=1,
        key="compare_country2"
    )

data1 = country_df[
    country_df["country_code"] == country1
]

data2 = country_df[
    country_df["country_code"] == country2
]

st.markdown("---")
col1, col2 = st.columns(2)

with col1:

    st.subheader(country1)

    st.metric(
        "🚀 Startups",
        int(data1["startups"].iloc[0])
    )

    st.metric(
        "💰 Total Funding",
        f"${data1['total_funding'].iloc[0]/1e9:.2f}B"
    )

    st.metric(
        "📈 Avg Funding",
        f"${data1['avg_funding'].iloc[0]/1e6:.2f}M"
    )

    st.metric(
        "🧬 DNA Score",
        f"{data1['dna_score'].iloc[0]:.1f}"
    )

with col2:

    st.subheader(country2)

    st.metric(
        "🚀 Startups",
        int(data2["startups"].iloc[0])
    )

    st.metric(
        "💰 Total Funding",
        f"${data2['total_funding'].iloc[0]/1e9:.2f}B"
    )

    st.metric(
        "📈 Avg Funding",
        f"${data2['avg_funding'].iloc[0]/1e6:.2f}M"
    )

    st.metric(
        "🧬 DNA Score",
        f"{data2['dna_score'].iloc[0]:.1f}"
    )

st.markdown("---")
st.subheader("📊 Country Comparison")

compare_df = pd.DataFrame({
    "Metric": [
        "Startups",
        "Total Funding",
        "Avg Funding",
        "DNA Score"
    ],
    country1: [
        data1["startups"].iloc[0],
        data1["total_funding"].iloc[0],
        data1["avg_funding"].iloc[0],
        data1["dna_score"].iloc[0]
    ],
    country2: [
        data2["startups"].iloc[0],
        data2["total_funding"].iloc[0],
        data2["avg_funding"].iloc[0],
        data2["dna_score"].iloc[0]
    ]
})

compare_long = compare_df.melt(
    id_vars="Metric",
    var_name="Country",
    value_name="Value"
)

fig = px.bar(
    compare_long,
    x="Metric",
    y="Value",
    color="Country",
    barmode="group"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")
st.subheader("🧬 DNA Score Comparison")

dna_df = pd.DataFrame({
    "Country": [country1, country2],
    "DNA Score": [
        data1["dna_score"].iloc[0],
        data2["dna_score"].iloc[0]
    ]
})

fig2 = px.bar(
    dna_df,
    x="Country",
    y="DNA Score",
    text="DNA Score"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)


winner = (
    country1
    if data1["dna_score"].iloc[0] >data2["dna_score"].iloc[0]
    else country2
)
st.success(f"🏆 {winner} has the stronger startup ecosystem based on DNA Score.")

startup_winner = country1 if data1["startups"].iloc[0] > data2["startups"].iloc[0] else country2
funding_winner = country1 if data1["total_funding"].iloc[0] > data2["total_funding"].iloc[0] else country2
st.markdown("---")
st.subheader("📌 Key Insights")
st.info(f"🚀 {startup_winner} has more startups.")
st.info(f"💰 {funding_winner} attracts more funding.")
st.success(f"🧬 {winner} has the stronger Startup DNA Score.")

