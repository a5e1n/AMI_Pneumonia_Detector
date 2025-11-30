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

# LOGOS CENTERED
center_row = st.columns([1,2,1])
with center_row[1]:
    logos = st.columns([1,1])

from PIL import Image

with logos[0]:
    uni_path = "AMI_app/static/university_logo.png"
    if os.path.exists(uni_path):
        uni_img = Image.open(uni_path)
        st.image(uni_img, width=110)   # حجم صغير بدون فقد الجودة

with logos[1]:
    ami_path = "AMI_app/static/ami_logo.png"
    if os.path.exists(ami_path):
        ami_img = Image.open(ami_path)
        st.image(ami_img, width=150)   # حجم مناسب وبجودة عالية


st.markdown(
    "<p style='text-align:center; color:#bbb;'>© AMI — Ameen Medical Intelligence.</p>",
    unsafe_allow_html=True
)
