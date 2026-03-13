import streamlit as st

# --- 1. KONFIGURACJA ---
st.set_page_config(
    page_title="Blank",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. CZYSTY INTERFEJS GLASSMORPHISM ---
st.markdown("""
    <style>
    /* Ukrycie elementów systemowych */
    [data-testid="stHeader"], [data-testid="stFooter"], [data-testid="stToolbar"] {
        display: none !important;
    }

    /* Tło aplikacji */
    .stApp {
        background-color: #F0D3DE !important;
        overflow: hidden;
    }

    /* Główny kontener "Hero" */
    .main .block-container {
        /* Stylistyka: Jasny, 90% krycia + Blur */
        background: rgba(255, 255, 255, 0.9) !important;
        backdrop-filter: blur(20px) saturate(180%);
        -webkit-backdrop-filter: blur(20px) saturate(180%);
        
        /* Geometria: Marginesy 1cm i dopasowanie do ekranu */
        margin: 1cm !important;
        border-radius: 1cm !important;
        
        /* Precyzyjne wymiary */
        min-height: calc(100vh - 2cm) !important;
        height: calc(100vh - 2cm) !important;
        max-width: calc(100% - 2cm) !important;
        
        /* Detale wykończenia */
        border: 1px solid rgba(255, 255, 255, 0.4);
        box-shadow: 0 10px 40px 0 rgba(0, 0, 0, 0.03);
        
        /* Reset paddingów Streamlit */
        padding: 0 !important;
    }

    /* Usunięcie domyślnych odstępów pionowych */
    [data-testid="stVerticalBlock"] {
        gap: 0 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Kontener jest teraz gotowy i pusty.
