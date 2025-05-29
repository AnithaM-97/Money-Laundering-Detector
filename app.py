#Step-6: Deployment code for Online Money Laundering


# Importing Libraries
import streamlit as st
import pandas as pd

# Load cyber crime dataset
cyber_data = pd.read_csv("Cyber_crime_data.csv")  

st.title("Early Detection of Online Money Laundering")
st.write("Enter Aadhar and PAN number to check if the account is linked to any known cyber crime report")

# Input fields
aadhar = st.text_input("Enter Aadhar Number")
pan = st.text_input("Enter PAN Number")

if st.button("Check Risk"):
    if not aadhar or not pan:
        st.warning("Please enter both Aadhar and PAN numbers.")
    else:
        aadhar_match = (cyber_data['Aadhar_number'] == aadhar).any()
        pan_match = (cyber_data['Pan_number'] == pan).any()

        if aadhar_match or pan_match:
            st.error("This account is linked to a cyber crime record. HIGH RISK.")
        else:
            st.success("No match found in cyber crime records. This account is NOT flagged.")
