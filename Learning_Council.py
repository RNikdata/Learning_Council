import streamlit as st
import pandas as pd
import numpy as np
import gspread
from gspread_dataframe import get_as_dataframe, set_with_dataframe
from google.oauth2.service_account import Credentials
import time
import hashlib


# --- Google Sheets setup ---
# --- Connect to Google Sheets using Streamlit secrets ---
service_account_info = st.secrets["google_service_account_learning_council"]
scopes = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
credentials = Credentials.from_service_account_info(service_account_info, scopes=scopes)
gc = gspread.authorize(credentials)

# # Your Google Sheet ID and worksheet name
SHEET_ID = "1tg4xQzY-zVu3_8QJWD6NNbrxUSbTCJYVABpCeVmCnVg"
sheet1 = "Certifications & Skill Gap Tracker"
sheet2 = "Knowledge Enablement Program Oversight - Coles"

data_sheet = gc.open_by_key(SHEET_ID).worksheet(sheet1)
data_sheet1 = gc.open_by_key(SHEET_ID).worksheet(sheet2)

# --- Load data from Google Sheets ---
df = get_as_dataframe(data_sheet, evaluate_formulas=True).dropna(how="all")
df1 = get_as_dataframe(data_sheet1, evaluate_formulas=True).dropna(how="all")

st.set_page_config(layout="wide")
 
# --- Tabs ---
tab1, tab2, tab3 = st.tabs(["🎓✅ Certifications & Skill Gap Tracker", "📘📅 Knowledge Enablement Program Oversight", "🛠️🧩 Prototyping Engagement & Session Planning"])
 
# --- Page design ---
with tab1:
 st.subheader("📊 Skill Gap Tracker")
    #st.markdown("<br>", unsafe_allow_html=True)
 
 st.dataframe(
     df,
     use_container_width=True,
     hide_index=True
 )
 
 if st.button("Refresh") :
     st.rerun()

with tab2:
 st.markdown("<br>", unsafe_allow_html=True)
 st.subheader("Knowledge Enablement Program Oversight")
 st.markdown("<br>", unsafe_allow_html=True)

 st.dataframe(
  df1,
  use_container_width = True,
  hide_index = True
 )
