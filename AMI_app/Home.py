import streamlit as st
from app_config import set_page_style
import os

set_page_style()

# TITLE
st.markdown("""
    <h1 style='text-align:center; color:#0da6a6;'>🩻 AMI Pneumonia Detection System</h1>
    <div class='glow-box'>
        <p style='text-align:center; font-size:20px;'>
            AI-powered diagnostic assistant for chest X-ray analysis
        </p>
    </div>
""", unsafe_allow_html=True)

st.write("")

# CENTER BUTTON
col1, col2, col3 = st.columns([1,1,1])
with col2:
    start = st.button("Start Diagnosis", use_container_width=True)

if start:
    st.switch_page("pages/0_Main_Detector.py")

st.write("---")

from streamlit.components.v1 import html

html("""
<div style="
    display: flex; 
    justify-content: center; 
    align-items: center;
    gap: 60px; 
    margin-top: 40px;
">
    <img src="AMI_app/static/university_logo.png" 
         style="width:130px; border-radius:10px;">

    <img src="AMI_app/static/ami_logo.png" 
         style="width:130px; border-radius:10px;">
</div>
""", height=200)

st.markdown(
    "<p style='text-align:center; color:#bbb;'>© AMI — Ameen Medical Intelligence.</p>",
    unsafe_allow_html=True
)
