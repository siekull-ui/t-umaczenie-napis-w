import streamlit as st

# --- 1. MINIMALISTYCZNA KONFIGURACJA ---
st.set_page_config(
    page_title="Blank",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. CZYSTY BIAŁY INTERFEJS ---
st.markdown("""
    <style>
    /* Ukrycie elementów systemowych */
    [data-testid="stHeader"], [data-testid="stFooter"], [data-testid="stToolbar"] {
        display: none !important;
    }

    /* Reset tła do czystej bieli */
    .stApp {
        background-color: white !important;
    }

    /* Usunięcie marginesów i paddingów */
    .main .block-container {
        padding: 0 !important;
        max-width: 100% !important;
    }
    </style>
    """, unsafe_allow_html=True)
