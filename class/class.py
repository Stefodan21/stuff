import streamlit as st
import pandas as pd
import plotly.express as px  




st.title("Water Dashboard ")
st.header("Water Usage Overview")
st.subheader("Monthly Water Usage")

st.divider()

st.sidebar.header("File Upload")
st.sidebar.info("Upload your water usage data file here.")

uploaded_file = st.sidebar.file_uploader("Choose a file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

else:
    df  = pd.read_csv("2021-oct21.csv")

tables,plots, maps = st.tabs(["Tables", "Plots", "Maps"])

with tables:
    st.dataframe(df)
    st.caption("Raw data")
    st.dataframe(df.describe())
    st.caption("Descriptive statistics")

with plots:
    st.subheader("Line Chart")
    parameter = st.selectbox("Select parameter", options=df.columns.tolist())
    # add all possible parameters in the select box above
    # and dynamically change the y axis in the plot below to the selected parameter
    fig1 = px.line(df,
                   x="Time",
                   y=parameter,
                   title=f"{parameter} over Time")
    st.plotly_chart(fig1)
