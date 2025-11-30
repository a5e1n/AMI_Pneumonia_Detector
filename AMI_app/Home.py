import streamlit as st
from app_config import set_page_style
import os

set_page_style()

# =============================
#   PAGE TITLE + SUBTITLE
# =============================

st.markdown("""
<style>
.title-text {
    text-align: center;
    color: #0da6a6;
    font-size: 42px;
    font-weight: 800;
    margin-top: 10px;
    margin-bottom: 5px;
}

/* Glass subtitle box */
.glass-sub {
    margin: auto;
    padding: 15px 25px;
    max-width: 650px;
    background: rgba(255, 255, 255, 0.06);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border-radius: 14px;
    border: 1px solid rgba(255, 255, 255, 0.2);
    box-shadow: 0 6px 25px rgba(0,0,0,0.35);
}
.glass-sub p {
    text-align: center;
    font-size: 20px;
    color: #e8e8e8;
    margin: 0;
}

/* Start button styling */
.stButton>button {
    background: linear-gradient(135deg, #0da6a6, #0b8080);
    color: white;
    border-radius: 10px;
    padding: 12px 18px;
    font-size: 18px;
    font-weight: 600;
    border: none;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.25);
}
.stButton>button:hover {
    background: linear-gradient(135deg, #12c8c8, #0da6a6);
    transform: scale(1.02);
}

.footer-text {
    text-align:center;
    color:#bbb;
    margin-top: 30px;
    font-size: 14px;
}
</style>

<h1 class="title-text">🩻 AMI Pneumonia Detection System</h1>

<div class="glass-sub">
    <p>AI-powered diagnostic assistant for chest X-ray analysis</p>
</div>
""", unsafe_allow_html=True)


st.write("")  # spacing


# =============================
#   CENTER BUTTON
# =============================

col1, col2, col3 = st.columns([1,1,1])
with col2:
    start = st.button("Start Diagnosis", use_container_width=True)

if start:
    st.switch_page("pages/0_Main_Detector.py")


st.write("---")


# =============================
#   LOGOS (CENTERED)
# =============================

center_row = st.columns([1,2,1])
with center_row[1]:
    logos = st.columns([1,1])

    with logos[0]:
        if os.path.exists("AMI_app/static/university_logo.png"):
            st.image("AMI_app/static/university_logo.png", width=100)

    with logos[1]:
        if os.path.exists("AMI_app/static/ami_logo.png"):
            st.image("AMI_app/static/ami_logo.png", width=140)


# =============================
#   FOOTER
# =============================

st.markdown(
    "<p class='footer-text'>© AMI — Ameen Medical Intelligence.</p>",
    unsafe_allow_html=True
)
