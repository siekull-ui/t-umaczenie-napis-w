import streamlit as st

# --- 1. MINIMALISTYCZNA KONFIGURACJA ---
st.set_page_config(
    page_title="Blank Hero",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. KONSTRUKCJA INTERFEJSU (CSS + HTML) ---
def apply_hero_layout():
    st.markdown("""
        <style>
        /* Ukrycie elementów systemowych Streamlit */
        [data-testid="stHeader"], [data-testid="stFooter"], [data-testid="stToolbar"] {
            display: none !important;
        }

        /* Tło aplikacji - Pełny róż */
        .stApp {
            background-color: #F0D3DE !important;
        }

        /* KONTENER HERO - Satynowa tafle z delikatnym cieniem */
        #hero-canvas {
            position: fixed;
            top: 1cm;
            bottom: 1cm;
            left: 1cm;
            right: 1cm;
            
            /* Jasne tło: 90% nieprzezroczystości (0.9 alpha) */
            background: rgba(255, 255, 255, 0.9);
            
            /* Efekt Glassmorphism / Satyna */
            backdrop-filter: blur(20px) saturate(170%);
            -webkit-backdrop-filter: blur(20px) saturate(170%);
            
            /* Zaokrąglenie 1cm i subtelna krawędź */
            border-radius: 1cm;
            border: 1px solid rgba(255, 255, 255, 0.5);
            
            /* Bardzo delikatny, szeroki cień pod spodem */
            box-shadow: 0 12px 40px rgba(0, 0, 0, 0.04);
            
            z-index: 1000;
        }

        /* Usunięcie marginesów domyślnych Streamlit */
        .main .block-container {
            padding: 0 !important;
        }
        </style>

        <div id="hero-canvas"></div>
    """, unsafe_allow_html=True)

# Wywołanie układu
apply_hero_layout()
