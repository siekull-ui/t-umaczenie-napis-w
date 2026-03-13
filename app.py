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

        /* KONTENER HERO - Prawdziwy Glassmorphism */
        #hero-canvas {
            position: fixed;
            top: 1cm;
            bottom: 1cm;
            left: 1cm;
            right: 1cm;
            
            /* KLUCZ: Duża przezroczystość bieli (tylko 25% krycia), aby blur zadziałał */
            background: rgba(255, 255, 255, 0.25);
            
            /* Efekt Glassmorphism / Satyna - mocne rozmycie i nasycenie kolorów tła */
            backdrop-filter: blur(25px) saturate(150%);
            -webkit-backdrop-filter: blur(25px) saturate(150%);
            
            /* Zaokrąglenie 1cm i wyraźniejsza, "szklana" krawędź */
            border-radius: 1cm;
            border: 1px solid rgba(255, 255, 255, 0.6);
            
            /* KLUCZ 2: Mocny, wyraźny cień, który podnosi kontener i nadaje głębi */
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.2);
            
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
