import streamlit as st
import pandas as pd
import plotly.express as px

st.title("⚖️ Compare Countries")
st.write("Compare startup ecosystems across countries.")

country_df = pd.read_csv("data/processed/country_summary.csv")

country_df["avg_funding"] = (country_df["avg_funding"].fillna(0))

country_df["dna_score"] = (
    country_df["startups"].rank(pct=True) * 40 +
    country_df["total_funding"].rank(pct=True) * 40 +
    country_df["avg_funding"].rank(pct=True) * 20
)

col1, col2 = st.columns(2)

with col1:
    country1 = st.selectbox(
        "Country 1",
        sorted(country_df["country_code"].unique()),
        index=0
    )

with col2:
    country2 = st.selectbox(
        "Country 2",
        sorted(country_df["country_code"].unique()),
        index=1
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