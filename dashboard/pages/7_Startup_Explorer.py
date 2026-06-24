import streamlit as st
import pandas as pd
import plotly.express as px


st.title("🔍 Startup Explorer")
st.write("Explore startup ecosystems by country.")

country_df = pd.read_csv("data/processed/country_summary.csv")

st.markdown("""
<style>
.block-container {
    padding-top: 2.3rem;
    padding-left: 0.5rem;
    padding-right: 0.5rem;
    max-width: 100% !important;
}
</style>
""", unsafe_allow_html=True)

country_options = sorted(
    country_df["country_code"].unique()
)

default_index = country_options.index("USA")

selected_filter = st.session_state.get(
    "country_filter",
    "All Countries"
)

if selected_filter in country_options:
    default_index = country_options.index(
        selected_filter
    )

selected_country = st.selectbox(
    "Select Country",
    country_options,
    index=default_index
)

country_data = country_df[country_df["country_code"] == selected_country]

st.markdown("---")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "🚀 Startups",
        int(country_data["startups"].iloc[0])
    )

with col2:
    st.metric(
        "💰 Total Funding",
        f"${country_data['total_funding'].iloc[0]/1e9:.2f}B"
    )

with col3:
    avg_funding = country_data["avg_funding"].iloc[0]

    if pd.isna(avg_funding):
        avg_funding = 0

    st.metric(
        "📈 Avg Funding",
        f"${avg_funding/1e6:.2f}M"
    )


country_df["avg_funding"] = country_df["avg_funding"].fillna(0)
country_df["dna_score"] = (
    country_df["startups"].rank(pct=True) * 40 +
    country_df["total_funding"].rank(pct=True) * 40 +
    country_df["avg_funding"].rank(pct=True) * 20
)

country_data = country_df[country_df["country_code"] == selected_country]

with col4:
    st.metric(
        "🧬 DNA Score",
        f"{country_data['dna_score'].iloc[0]:.1f}"
    )

st.markdown("---")
country_rank = (
    country_df["dna_score"].rank(ascending=False)
)

rank = int(country_rank[country_df["country_code"] == selected_country].iloc[0])

st.success(
    f"🏆 {selected_country} ranks #{rank} out of {len(country_df)} countries based on Startup DNA Score."
)


st.markdown("---")
st.subheader("🌍 Global Top 10 Countries by DNA Score")
top10 = (country_df.sort_values("dna_score", ascending=False).head(10))
fig = px.bar(
    top10,
    y="country_code",
    x="dna_score",
    orientation="h",
    color="dna_score",
    color_continuous_scale=[
        "#FBCFE8",
        "#EC4899",
        "#BE185D"
    ]
)

fig.update_traces(
    width=0.37
)

fig.update_layout(
    coloraxis_showscale=False,
    height=450
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")
st.subheader("📌 Country Insights")

st.info(
    f"🚀 {selected_country} hosts {int(country_data['startups'].iloc[0]):,} startups."
)

st.info(
    f"💰 Total funding reached ${country_data['total_funding'].iloc[0]/1e9:.2f}B."
)

st.info(
    f"🧬 Startup DNA Score: {country_data['dna_score'].iloc[0]:.1f}"
)