import pandas as pd
import streamlit as st
#from datetime import datetime

st.title("Hello World")
soh = st.file_uploader("Unload a CSV file of SOH")
df = pd.read_csv(soh)
df = df[["SKU","SKU Desc","Bin","Lot No","Available Qty","Committed Qty","Lottable03","Zone","Inv Bucket"]]

gsoh = df[df["Inv Bucket"] == "Good"]

df2 = gsoh.groupby("SKU Desc").sum()
st.dataframe(df2)
