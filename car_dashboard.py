
import streamlit as st
import pandas as pd
import plotly.express as px
import statsmodels.api as sm

# Load CSV
df = pd.read_csv("IdianCarMarket_with_Cluster.csv")
df["Cluster"] = df["Cluster"].astype(str)

# Sidebar filter
brands = st.sidebar.multiselect("Select Brands", df["Brand"].unique(), default=df["Brand"].unique())
filtered_df = df[df["Brand"].isin(brands)]

st.title("🚗 Indian Car Market Dashboard")

# 1. Scatter Plot – Engine_CC vs Price
st.subheader("Cluster Visualization: Price vs Engine_CC")
fig1 = px.scatter(filtered_df, x="Engine_CC", y="Price", color="Cluster", hover_data=["Brand", "Model"])
st.plotly_chart(fig1)

# 2. Cluster Profile Table
st.subheader("Cluster Profile Summary")
cluster_profile = filtered_df.groupby("Cluster")[["Price", "Mileage", "Engine_CC", "Service_Cost"]].mean().reset_index()
st.dataframe(cluster_profile)

# 3. Perceptual Map (Performance vs Efficiency)
st.subheader("Perceptual Positioning Map")
brand_avg = filtered_df.groupby("Brand").agg({
    "Price": "mean",
    "Engine_CC": "mean",
    "Mileage": "mean",
    "Service_Cost": "mean"
}).reset_index()

brand_avg["Performance"] = (brand_avg["Price"] + brand_avg["Engine_CC"]) / 2
brand_avg["Efficiency"] = brand_avg["Mileage"] - brand_avg["Service_Cost"]

fig2 = px.scatter(brand_avg, x="Performance", y="Efficiency", text="Brand")
st.plotly_chart(fig2)

# 4. Regression Analysis
st.subheader("Regression Analysis – Factors Affecting Price")

X = df[["Mileage", "Engine_CC", "Seating_Capacity", "Service_Cost"]]
X = sm.add_constant(X)
y = df["Price"]
model = sm.OLS(y, X).fit()

results = pd.DataFrame({
    "Variable": model.params.index,
    "Coefficient": model.params.values,
    "p-value": model.pvalues.values
})

st.dataframe(results)

fig3 = px.bar(results[results["Variable"] != "const"], x="Variable", y="Coefficient", color="Coefficient",
              color_continuous_scale="RdBu", title="Regression Coefficients")
st.plotly_chart(fig3)
