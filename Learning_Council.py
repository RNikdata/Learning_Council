import streamlit as st
import pandas as pd
 
st.set_page_config(layout="wide")
 
# --- Load Data ---
df = pd.read_excel(
    r"C:\Users\Aathikumar.p\Desktop\Learning council\Skill Gap Excel.xlsx"
)
 
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
