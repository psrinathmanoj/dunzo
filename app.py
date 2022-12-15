import streamlit as st
from pyzbar import pyzbar
import cv2
import numpy as np
import pandas as pd

import gspread
from gspread_dataframe import get_as_dataframe

# Use your Google Account credentials to authenticate with the Google Sheets API
gc = gspread.service_account(filename='tvs-dunzo-1223551bd505.json')
# Open the desired spreadsheet using its URL or name
spreadsheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/1LioVLgdMt1tezAM5eqvDtjc983X3cFGxOXQVLaRmy1Q/edit')

# Select the desired worksheet from the spreadsheet
worksheet = spreadsheet.worksheet('Sheet1')

# Use the `get_as_dataframe` function to convert the data in the worksheet to a pandas DataFrame
df = get_as_dataframe(worksheet)
st.title("Hello World")
#soh = st.file_uploader("Unload a CSV file of SOH")
# df = pd.read_csv(soh)
df = df[["SKU","SKU Desc","Bin","Lot No","Available Qty","Committed Qty","Lottable03","Zone","Inv Bucket"]]

gsoh = df[df["Inv Bucket"] == "Good"]

df2 = gsoh.groupby("SKU Desc").sum()
st.dataframe(df2)
