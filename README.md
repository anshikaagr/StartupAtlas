# 🚀 StartupAtlas

StartupAtlas is an interactive data analytics dashboard that explores global startup ecosystems, funding trends, market performance, and ecosystem strength using historical startup funding data.

Built with Python, Pandas, Plotly, and Streamlit, the project transforms raw startup data into actionable insights through interactive visualizations and custom scoring models.

## 🌐 Live Demo

https://your-app-name.streamlit.app
---

## 📊 Dataset Overview

- 🚀 44,165 Startups
- 🌍 115 Countries
- 🏭 753 Markets
- 💰 $625B+ Total Funding
- 📅 Historical Crunchbase dataset (primarily up to 2014)

> **Note:** The dataset primarily covers startup activity up to 2014. Later-year trends may be affected by dataset coverage.

---

## ✨ Features

### 🌍 Geographic Analysis
- Startup distribution across countries
- Funding distribution by country
- Regional ecosystem comparison
- Geographic insights

### 💰 Funding Analysis
- Funding trends over time
- Top funded markets
- Top funded countries
- Funding insights

### 🏭 Market Analysis
- Market-wise startup distribution
- Funding concentration across sectors
- Market funding treemap
- Market insights

### 📈 Time Trends
- Startup funding growth over time
- Peak funding year analysis
- Historical trend exploration

### 🧬 Startup DNA Score
A custom ecosystem scoring model based on:
- Startup count
- Total funding
- Average funding

The DNA Score estimates startup ecosystem strength and enables cross-country comparisons.

### 🔎 Startup Explorer
- Explore individual countries
- Country rankings
- Ecosystem metrics
- DNA Score insights

### ⚖️ Compare Countries
- Side-by-side country comparison
- Startup ecosystem benchmarking
- Funding comparison
- DNA Score comparison

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Plotly
- Streamlit

---

## 📂 Project Structure

```text
StartupAtlas/
│
├── dashboard/
│   ├── app.py
│   ├── __pycache__/
│   └── pages/
│       ├── 1_Overview.py
│       ├── 2_Funding_Analysis.py
│       ├── 3_Geographic_Analysis.py
│       ├── 4_Market_Analysis.py
│       ├── 5_Time_Trends.py
│       ├── 6_Startup_DNA_Score.py
│       ├── 7_Startup_Explorer.py
│       └── 8_Compare_Countries.py
│
├── data/
│   ├── raw/
│   │   └── investments_VC.csv
│   │
│   └── processed/
│       ├── country_summary.csv
│       ├── funding_summary.csv
│       ├── market_summary.csv
│       ├── startup_dna_dataset.csv
│       └── status_summary.csv
│
├── notebooks/
│   └── notebooks/
│       ├── 01_data_understanding.ipynb
│       ├── 02_startup_success_analysis.ipynb
│       ├── 03_funding_analysis.ipynb
│       ├── 04_geographic_analysis.ipynb
│       ├── 05_market_industry_analysis.ipynb
│       ├── 06_time_trend_analysis.ipynb
│       ├── 07_startup_dna_score.ipynb
│       └── 08_dashboard_data_preparation.ipynb
│
├── outputs/
│
├── sql/
│
├── requirements.txt
├── README.md
└── .gitignore
```
---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/anshikaagr/StartupAtlas.git
cd StartupAtlas
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run dashboard/app.py
```
---

## 🎯 Key Insights

- USA dominates startup count and total funding.
- Biotechnology attracts the highest funding.
- Startup activity is concentrated in North America, Europe, and Asia.
- Startup funding experienced significant growth during the 2000s.
- Ecosystem strength varies significantly across countries.

---

## 🔮 Future Improvements

- Real-time startup datasets
- Interactive geographic maps
- Funding trend forecasting
- Investor ecosystem analysis
- Machine learning-based startup insights

---

## 👩‍💻 Author

**Anshika Agrawal**

B.Tech CSE (Data Science)  
VIT Vellore

GitHub: https://github.com/anshikaagr
