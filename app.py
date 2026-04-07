import streamlit as st
import pandas as pd
from src.agents.ceo_agent import CEOAgent

st.set_page_config(page_title="BDE Operations", layout="centered")

# Visual Theme
st.markdown("""
    <style>
    .stApp { background-color: #008080; color: white; }
    .stButton>button { background-color: #FF7F50; color: white; border-radius: 20px; }
    .stMetric { background-color: #FF69B4; padding: 15px; border-radius: 15px; }
    h1, h2, h3 { color: #32CD32; }
    </style>
    """, unsafe_allow_html=True)

st.title("⚡ BDE Ops Center")

menu = st.sidebar.radio("Navigate", ["Strategy", "Finance", "Outreach"])

if menu == "Strategy":
    st.subheader("Strategic Governor")
    st.metric("System Confidence", "88%", "2%")
    if st.button("Run Daily Sync"):
        st.write("Syncing principles...")

elif menu == "Finance":
    st.subheader("Money Master")
    uploaded_file = st.file_uploader("Upload Statement", type="csv")
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df.head())

elif menu == "Outreach":
    st.subheader("The Amplifier")
    st.text_area("Pitch Draft", "Drafting new outreach for Tuke Aevy...")
    st.button("Refine Copy")
