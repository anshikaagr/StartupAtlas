import streamlit as st

st.set_page_config(
    page_title="StartupAtlas",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 StartupAtlas")
st.caption("Data-driven insights into the global startup ecosystem.")

if "country_filter" not in st.session_state:
    st.session_state["country_filter"] = "All Countries"

if "market_filter" not in st.session_state:
    st.session_state["market_filter"] = "All Markets"

st.sidebar.header("🎛️ Global Filters")
st.sidebar.selectbox(
    "Country",
    ["All Countries"]
)
st.sidebar.selectbox(
    "Market",
    ["All Markets"]
)

st.session_state
st.session_state["country_filter"]
st.session_state["market_filter"]
