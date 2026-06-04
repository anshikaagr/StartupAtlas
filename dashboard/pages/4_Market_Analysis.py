import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🏭 Market Analysis")
st.write("Explore startup activity and funding across markets.")

market_df = pd.read_csv("data/processed/market_summary.csv")