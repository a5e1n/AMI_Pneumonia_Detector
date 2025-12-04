import streamlit as st

def set_page_style():
    st.markdown("""
        <style>

        /* ===== MAIN APP BACKGROUND ===== */
        .stApp {
            background: radial-gradient(circle at top, #151b26 0%, #05070b 55%, #020305 100%);
        }

        /* ===== DEFAULT TEXT COLOR ===== */
        h1, h2, h3, h4, h5, h6, p, span, label {
            color: #e6e6e6 !important;
        }

        /* ===== BUTTON STYLE ===== */
        .stButton > button {
            background-color: #0da6a6 !important;
            padding: 10px 28px !important;
            border-radius: 10px;
            border: none;
            font-size: 18px !important;
            color: white !important;
        }

        .stButton > button:hover {
            background-color: #11bbbb !important;
            transform: scale(1.05);
            transition: 0.15s ease;
        }

        /* ===== SIDEBAR ===== */
        section[data-testid="stSidebar"] {
            background-color: rgba(0,0,0,0.80) !important;
            backdrop-filter: blur(8px);
        }

        /* ===== GLOW BOX (Home) ===== */
        @keyframes glow {
            0%   { box-shadow: 0 0 6px #0da6a6; }
            50%  { box-shadow: 0 0 18px #0da6a6; }
            100% { box-shadow: 0 0 6px #0da6a6; }
        }

        .glow-box {
            animation: glow 2.5s infinite;
            padding: 15px;
            border-radius: 12px;
            background: rgba(0,0,0,0.45);
            text-align: center;
            width: 70%;
            margin: 0 auto;
        }

        /* ===== CENTER ALL IMAGES (X-ray, Grad-CAM, Logo, Photo…) ===== */
        [data-testid="stImage"] img {
            display: block;
            margin-left: auto;
            margin-right: auto;
        }

        </style>
    """, unsafe_allow_html=True)
