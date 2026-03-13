import streamlit as st

# --- CONFIG ---
st.set_page_config(
    page_title="Blank",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- UI STRUCTURE ---
st.markdown("""
    <style>
    /* Ukrycie UI systemowego */
    [data-testid="stHeader"], [data-testid="stFooter"], [data-testid="stToolbar"] {
        display: none !important;
    }

    /* Tło bazowe */
    .stApp {
        background-color: #F0D3DE !important;
        overflow: hidden;
    }

    /* Kontener Hero - Glassmorphism */
    .main .block-container {
        /* Wygląd: 90% bieli + satynowy blur */
        background: rgba(255, 255, 255, 0.9) !important;
        backdrop-filter: blur(25px) saturate(150%);
        -webkit-backdrop-filter: blur(25px) saturate(150%);
        
        /* Geometria i marginesy */
        margin: 1cm !important;
        border-radius: 1cm !important;
        
        /* Dopasowanie do ekranu */
        height: calc(100vh - 2cm) !important;
        min-height: calc(100vh - 2cm) !important;
        max-width: calc(100vw - 2cm) !important;
        
        /* Detale krawędzi */
        border: 1px solid rgba(255, 255, 255, 0.5);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
        
        /* Resetowanie wnętrza */
        padding: 0 !important;
    }

    [data-testid="stVerticalBlock"] {
        gap: 0 !important;
    }
    </style>
    """, unsafe_allow_html=True)
