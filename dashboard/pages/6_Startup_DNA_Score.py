import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🧬 Startup DNA Score")
st.write("Measure startup ecosystem strength through a custom scoring model.")
country_df = pd.read_csv("data/processed/country_summary.csv")

country_df["dna_score"] = (
    country_df["startups"].rank(pct=True) * 40 +
    country_df["total_funding"].rank(pct=True) * 40 +
    country_df["avg_funding"].rank(pct=True) * 20
)

avg_score = country_df["dna_score"].mean()
highest_score = country_df["dna_score"].max()

top_country = (
    country_df.sort_values("dna_score", ascending=False).iloc[0]["country_code"]
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🧬 Average Score", f"{avg_score:.1f}")

with col2:
    st.metric("🏆 Highest Score", f"{highest_score:.1f}")

with col3:
    st.metric("🌍 Top Country", top_country)

st.markdown("---")

st.subheader("DNA Score Distribution")

fig = px.histogram(
    country_df,
    x="dna_score",
    nbins=20
)

st.plotly_chart(fig, use_container_width=True)


st.markdown("---")

st.subheader("Top Countries by DNA Score")

top_dna = (
    country_df
    .sort_values("dna_score", ascending=False)
    .head(10)
)

st.dataframe(
    top_dna[
        [
            "country_code",
            "startups",
            "total_funding",
            "dna_score"
        ]
    ],
    use_container_width=True
)


st.subheader("Top DNA Score Countries")

fig2 = px.bar(
    top_dna,
    x="country_code",
    y="dna_score"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

