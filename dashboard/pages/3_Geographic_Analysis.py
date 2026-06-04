import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🌍 Geographic Analysis")
st.write("Explore startup distribution and funding across countries.")
country_df = pd.read_csv("data/processed/country_summary.csv")

total_countries = country_df["country_code"].nunique()

avg_funding = country_df["avg_funding"].mean()

top_country = (
    country_df
    .sort_values("startups", ascending=False)
    .iloc[0]["country_code"]
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🌍 Countries", total_countries)

with col2:
    st.metric("💰 Avg Funding", f"${avg_funding/1e6:.1f}M")

with col3:
    st.metric("🏆 Top Country", top_country)

st.markdown("---")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Top Startup Countries")

    top_countries = (
        country_df
        .sort_values("startups", ascending=False)
        .head(10)
    )

    fig = px.bar(top_countries,
        x="startups",
        y="country_code",
        orientation="h")

    st.plotly_chart(fig,use_container_width=True)

with col2:

    st.subheader("Top Funded Countries")

    top_funded = (
        country_df
        .sort_values("total_funding", ascending=False)
        .head(10)
    )

    fig2 = px.bar(
        top_funded,
        x="total_funding",
        y="country_code",
        orientation="h"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

st.markdown("---")

st.subheader("Country Funding Distribution")

fig3 = px.scatter(
    country_df,
    x="startups",
    y="total_funding",
    size="startups",
    hover_name="country_code"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)