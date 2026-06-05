import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📈 Time Trends Analysis")
st.write("Explore startup growth and funding trends over time.")

funding_df = pd.read_csv("data/processed/funding_summary.csv")

peak_year = (
    funding_df.sort_values("total_funding", ascending=False).iloc[0]["founded_year"]
)

peak_funding = (funding_df["total_funding"].max())

total_years = funding_df["founded_year"].nunique()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📅 Years Covered", total_years)

with col2:
    st.metric("🏆 Peak Year", int(peak_year))

with col3:
    st.metric(
        "💰 Peak Funding",
        f"${peak_funding/1e9:.1f}B"
    )

st.markdown("---")

st.subheader("Funding Growth Over Time")

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

st.subheader("Funding Distribution by Year")

fig2 = px.bar(
    funding_df,
    x="founded_year",
    y="total_funding"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)
