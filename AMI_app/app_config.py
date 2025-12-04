import streamlit as st

def set_page_style():
    st.markdown("""
        <style>

        /* ===== MAIN APP BACKGROUND ===== */
        .stApp {
            background: radial-gradient(circle at top, #151b26 0%, #05070b 55%, #020305 100%);
        }

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

        /* ===== CUSTOM SIDEBAR MENU ===== */

        /* Sidebar container */
        section[data-testid="stSidebar"] {
            background: rgba(10, 15, 25, 0.94) !important;
            padding-top: 40px !important;
        }

        /* Sidebar links */
        section[data-testid="stSidebar"] .css-1n76uvr, 
        section[data-testid="stSidebar"] .css-qri22k {
            font-size: 19px !important;
            padding: 12px 16px !important;
            color: #dce7f3 !important;
            border-radius: 8px !important;
            margin-bottom: 4px !important;
        }

        /* Hover effect */
        section[data-testid="stSidebar"] .css-1n76uvr:hover,
        section[data-testid="stSidebar"] .css-qri22k:hover {
            background: rgba(255,255,255,0.08) !important;
            transition: 0.2s;
        }

        /* Active page highlight */
        section[data-testid="stSidebar"] .css-17eq0hr {
            background: rgba(13,166,166,0.30) !important;
            border-radius: 8px !important;
            color: #ffffff !important;
            font-weight: 700 !important;
        }

        /* Better scrollbar */
        ::-webkit-scrollbar {
            width: 8px;
        }
        ::-webkit-scrollbar-thumb {
            background: rgba(255,255,255,0.25);
            border-radius: 4px;
        }
        </style>
    """, unsafe_allow_html=True)
