import streamlit as st

def set_page_style():
    st.markdown("""
        <style>

        /* ===== MAIN APP BACKGROUND ===== */
        .stApp {
            background: radial-gradient(circle at top, #151b26 0%, #05070b 55%, #020305 100%);
        }

        /* ===== GLOBAL TEXT COLOR ===== */
        h1, h2, h3, h4, h5, h6, p, label, span {
            color: #e6e6e6 !important;
        }

        /* ===== BUTTON STYLING ===== */
        .stButton > button {
            background-color: #0da6a6 !important;
            padding: 10px 28px !important;
            border-radius: 10px !important;
            font-size: 18px !important;
            border: none !important;
            color: white !important;
            transition: 0.2s ease-in-out;
        }

        .stButton > button:hover {
            background-color: #11bbbb !important;
            transform: scale(1.05);
        }

        /* ===== SIDEBAR STYLING ===== */
        section[data-testid="stSidebar"] {
            background: rgba(10, 15, 25, 0.92) !important;
            border-right: 1px solid rgba(255,255,255,0.08);
            backdrop-filter: blur(6px);
        }

        /* Sidebar page name text */
        /* (Streamlit generates dynamic classes – these targets improve readability) */
        div[data-testid="stSidebar"] .css-1d391kg,
        div[data-testid="stSidebar"] .css-1n76uvr,
        div[data-testid="stSidebar"] .css-qri22k {
            font-size: 17px !important;
            font-weight: 600 !important;
            padding-top: 6px !important;
            padding-bottom: 6px !important;
            color: #dce7f3 !important;
        }

        /* ACTIVE page highlight */
        div[data-testid="stSidebar"] .css-17eq0hr, 
        div[data-testid="stSidebar"] .css-1y4p8pa {
            background: rgba(13,166,166,0.28) !important;
            color: #ffffff !important;
            border-radius: 8px !important;
            font-weight: 700 !important;
        }

        /* ===== Improve sidebar scrollbar ===== */
        ::-webkit-scrollbar {
            width: 8px;
        }
        ::-webkit-scrollbar-thumb {
            background: rgba(255,255,255,0.15);
            border-radius: 4px;
        }

        </style>
    """, unsafe_allow_html=True)
