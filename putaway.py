import pandas as pd
import streamlit as st

def run_putaway():
    
    st.header("GRN and putaway Checking")
    st.subheader("Inbound data")
    ib = st.file_uploader("Upload CSV", type= ["csv"])
    if ib is not None:
        st.write(type(ib))
        ib = pd.read_csv(ib)

    st.subheader("Putway data")
    pw = st.file_uploader("Upload XLSX", type= ["xlsx"])
    if pw is not None:
        st.write(type(pw))
        pw = pd.read_excel(pw)
    
    #ib = pd.read_csv(r'D:\python\report\ib22.csv')
    #pw = pd.read_excel(r'D:\python\report\pw22.xlsx')
    if st.button("Process"):
        ibgrn = ib[(ib['Inbound Type'] == 'Without PO')]
        ibgrn = ibgrn['Recieved Qty'].sum()

        rgrn = ib[(ib['Inbound Type'] != 'Without PO')]
        rgrn = rgrn['Recieved Qty'].sum()

        ib = ib[['SKU Name','SKU Code','Inbound No','Vendor Code','Recieved Qty']]
    #pw = pw[(pw['InbType'] == 'Without PO')]
        pw = pw[['SkuName','Sku','Inbound No','To Qty']]
        pw = pw.groupby(['SkuName','Sku','Inbound No']).sum()
        grn = ib.merge(pw, left_on=['SKU Name','SKU Code','Inbound No'], right_on=['SkuName','Sku','Inbound No'],how='left')
    #st.dataframe(df)
        grn = grn[['SKU Name', 'SKU Code', 'Inbound No', 'Recieved Qty', 'To Qty']]
        grn['status'] = grn['Recieved Qty'] - grn['To Qty']
        grnpending = grn[(grn['Recieved Qty']!=0)]  
        grnpending = grn[(grn['status']!=0)]
        
        sumib = grn['Recieved Qty'].sum()
        sumpw = pw['To Qty'].sum()   
    #grnpending.head()
    #st.subheader("Total Inbound Received for the day:")
    #st.subheader(sumib)
        
        col1, col2 = st.columns(2)
        col1.metric("Inbound GRN Qty",ibgrn)
        col2.metric("Return GRN Qty",rgrn)

        dif = sumib-sumpw
        col1, col2, col3 = st.columns(3)
        col1.metric("GRN Qty",sumib)
        col2.metric("Putaway Qty",sumpw)
        col3.metric("Putaway Pending",dif)

        if dif == 0:
            st.success("GRN and Putaway done Successfully")
        else:
    #st.metric("GRN Qty",sumib)
    #st.metric("Putaway Qty",sumpw)
            st.dataframe(grnpending)
            @st.cache
            def convert_df(grnpending):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
                return grnpending.to_csv().encode('utf-8')

            csv = convert_df(grnpending)

            st.download_button(
                label="Download data as CSV",
                data=csv,
                file_name='putawaypending.csv',
                mime='text/csv',
            )
            #grnpending.to_csv('D:\python\grnpending.csv')
