import streamlit as st
import pandas as pd
import gspread
from gspread_dataframe import get_as_dataframe
import datetime

st.set_page_config(
    page_title="Real-Time TVS Dunzo Dashboard",
    page_icon="✅",
    # layout="wide",
)

# Use your Google Account credentials to authenticate with the Google Sheets API
gc = gspread.service_account(filename='tvs-dunzo-1223551bd505.json')
# Open the desired spreadsheet using its URL or name
spreadsheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/1MLkJPNFsPLTcy33G971c06a_24GARp-yMvUp-zO5cxE/edit')

# Select the desired worksheet from the spreadsheet
SOH = spreadsheet.worksheet('SOH')
# Use the `get_as_dataframe` function to convert the data in the worksheet to a pandas DataFrame
df = get_as_dataframe(SOH)
st.title("TVS Dunzo Dashboard ")
df = df[["SKU","SKU Desc","Bin","Lot No","Available Qty", "Commited Qty","Shelf Life % Rem","Zone"]]
skulist = set(df["SKU"])
totalavl = df["Available Qty"].sum()
totalcom = df["Commited Qty"].sum()


today = datetime.datetime.today()
# Subtract one day from the current date
yesterday = today - datetime.timedelta(days=1)
yesterday = yesterday.strftime('%d/%m/%Y')
dailySOH = spreadsheet.worksheet('Daily SOH')
dailySOH = get_as_dataframe(dailySOH)
dailySOH = dailySOH[["Date","No Of SKU's","Qty"]]
yessoh = dailySOH[dailySOH["Date"] == yesterday]
yessku = yessoh["No Of SKU's"]
yessku = int(yessku.iloc[0])
yesto = int(len(skulist)) - yessku
yesav = yessoh["Qty"]
yesav = int(totalavl) - int(yesav.iloc[0])

col1, col2, col3 = st.columns(3)
col1.metric("No. of SKU's", len(skulist), yesto)
col2.metric("Total Avl", totalavl, yesav)
col3.metric("Total Commited Qty",totalcom)
df2 = df[["Zone","Available Qty","Commited Qty"]].groupby("Zone").sum()
st.bar_chart(df2)
