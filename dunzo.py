from secrets import choice
import streamlit as st
from GRNCheck import run_grncheck
from putaway import run_putaway

def main():
    st.title("Dunzo App")
    
    menu = ["Home","GRN Checker","Putaway Checker"]

    choice = st.sidebar.selectbox("Main",menu)
    
    if choice == "Home":
        st.subheader("Home")
    elif choice == "GRN Checker":
        run_grncheck()
    elif choice == "Putaway Checker":
        run_putaway()
    else:
        pass
    
    
    
if __name__ == '__main__':
    main()