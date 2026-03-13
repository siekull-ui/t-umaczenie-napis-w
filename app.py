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

        /* KONTENER HERO - Stylizacja satynowa */
        #hero-canvas {
            position: fixed;
            top: 1cm;
            bottom: 1cm;
            left: 1cm;
            right: 1cm;
            
            /* Jasne tło 90% przepustowości */
            background: rgba(255, 255, 255, 0.9);
            
            /* Efekt Glassmorphism / Satyna */
            backdrop-filter: blur(25px) saturate(160%);
            -webkit-backdrop-filter: blur(25px) saturate(160%);
            
            /* Zaokrąglenie 1cm i obramowanie */
            border-radius: 1cm;
            border: 1px solid rgba(255, 255, 255, 0.4);
            
            /* Cień dla głębi */
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.05);
            
            z-index: 1000;
        }

        /* Usunięcie marginesów domyślnych Streamlit, aby nie przesuwały widoku */
        .main .block-container {
            padding: 0 !important;
        }
        </style>

        <div id="hero-canvas"></div>
    """, unsafe_allow_html=True)

# Wywołanie układu
apply_hero_layout()
