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

        /* KONTENER HERO - Czysty Glassmorphism bez krawędzi */
        #hero-canvas {
            position: fixed;
            top: 1cm;
            bottom: 1cm;
            left: 1cm;
            right: 1cm;
            
            /* Tło - 25% krycia bieli */
            background: rgba(255, 255, 255, 0.25);
            
            /* Efekt rozmycia / satyny */
            backdrop-filter: blur(25px) saturate(150%);
            -webkit-backdrop-filter: blur(25px) saturate(150%);
            
            /* Zaokrąglenie i usunięcie obramowania */
            border-radius: 1cm;
            border: none;
            
            /* Zwarty, mocniejszy cień trzymający się blisko krawędzi */
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
            
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
