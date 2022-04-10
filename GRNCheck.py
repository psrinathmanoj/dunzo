import pandas as pd
import streamlit as st
#from datetime import datetime
def run_grncheck():
    
    dock2 = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSWhQtfrE1ot7aRfpsx5SiAKMeDEmjKGN1tt_o2bIgdFpBZUpdFAGQR6QK7U7r196ZSy_n9vYhrFuRS/pub?gid=1581027234&single=true&output=csv')
    dock1 = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSWhQtfrE1ot7aRfpsx5SiAKMeDEmjKGN1tt_o2bIgdFpBZUpdFAGQR6QK7U7r196ZSy_n9vYhrFuRS/pub?gid=159525948&single=true&output=csv')
    dock = pd.concat([dock1, dock2])
    dock = dock[['Date', 'Vendor name','Inv no.', 'SKU Name','SKU Code','Invoice Qty','Phy Qty','Diff']]
    dt = st.date_input("Dock Inboud Date")
    dt2 = dt.strftime("%d/%m/%Y")
    #dt = datetime.strptime(dt , "%Y/%m/%d").strftime("%d-%m-%Y")
    dock = dock[(dock['Date'] == dt2)]
    #dt2 = dt2[(dt2['Phy Qty'] == None)]
    st.write(dt2)
    phyqty = dock['Phy Qty'].sum()
    skuer = dock[(dock['SKU Name'] == 'Please enter name in Remarks')]
    skuer = skuer['Phy Qty'].sum()
    st.dataframe(dock)
