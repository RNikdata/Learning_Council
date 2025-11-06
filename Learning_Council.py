import streamlit as st
import pandas as pd


# --- Google Sheets setup ---
# --- Connect to Google Sheets using Streamlit secrets ---
service_account_info = st.secrets["google_service_account_learning_council"]
scopes = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
credentials = Credentials.from_service_account_info(service_account_info, scopes=scopes)
gc = gspread.authorize(credentials)

# # Your Google Sheet ID and worksheet name
SHEET_ID = "1tg4xQzY-zVu3_8QJWD6NNbrxUSbTCJYVABpCeVmCnVg"
sheet1 = "Certifications & Skill Gap Tracker"

data_sheet = gc.open_by_key(SHEET_ID).worksheet(sheet1)
# --- Load data from Google Sheets ---
df = get_as_dataframe(data_sheet, evaluate_formulas=True).dropna(how="all")

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
