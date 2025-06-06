# 🚗 Indian Car Market Dashboard

This Streamlit dashboard is built for a final project in **Digital Marketing Analysis**. It analyzes segmentation, brand positioning, and pricing factors in the Indian automobile market.

## Features

- 📊 Scatter plot: Price vs Engine_CC colored by clusters
- 📋 Cluster profile table
- 🧭 Perceptual positioning map (Performance vs Efficiency)
- 📈 Regression analysis: Key factors affecting price
- 🎯 Brand-based interactive filtering

## Files

- `car_dashboard.py`: Main dashboard script
- `IdianCarMarket_with_Cluster.csv`: Cleaned and clustered dataset

## Run locally

```bash
pip install streamlit pandas plotly statsmodels
streamlit run car_dashboard.py
