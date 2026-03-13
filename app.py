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
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500&display=swap');

        /* Ukrycie elementów systemowych Streamlit */
        [data-testid="stHeader"], [data-testid="stFooter"], [data-testid="stToolbar"] {
            display: none !important;
        }

        /* Tło aplikacji - Pełny róż */
        .stApp {
            background-color: #F0D3DE !important;
        }

        /* KONTENER HERO */
        #hero-canvas {
            position: fixed;
            top: 1cm;
            bottom: 1cm;
            left: 1cm;
            right: 1cm;
            
            background: rgba(255, 255, 255, 0.25);
            backdrop-filter: blur(25px) saturate(150%);
            -webkit-backdrop-filter: blur(25px) saturate(150%);
            
            border-radius: 1cm;
            border: none;
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
            
            z-index: 1000;
        }

        /* --- NAWIGACJA (MENU W PRAWYM GÓRNYM ROGU) --- */
        .hero-nav {
            position: absolute;
            top: 40px; /* Odstęp od góry wewnątrz kontenera */
            right: 50px; /* Odstęp od prawej wewnątrz kontenera */
            display: flex;
            gap: 30px; /* Odstępy między słowami */
            align-items: center;
            font-family: 'Poppins', sans-serif;
        }

        .hero-nav a {
            color: #1a1a1a; /* Ciemny, elegancki grafit */
            text-decoration: none;
            font-size: 14px;
            font-weight: 500;
            cursor: pointer;
            transition: color 0.2s ease;
            text-underline-offset: 8px; /* Odsunięcie fali od tekstu */
        }

        /* Efekt najechania i aktywnej zakładki - FALOWANA LINIA */
        .hero-nav a:hover, 
        .hero-nav a.active {
            /* Dziki, intensywny róż w stylu obrazka */
            text-decoration: underline wavy #FF2A5F 2px;
        }

        /* Ikonka lupki (wyszukiwania) */
        .hero-nav .search-icon {
            margin-left: 10px;
            display: flex;
            align-items: center;
        }

        .hero-nav .search-icon svg {
            width: 18px;
            height: 18px;
            stroke: #1a1a1a;
            stroke-width: 2;
            transition: stroke 0.2s ease;
        }

        .hero-nav .search-icon:hover svg {
            stroke: #FF2A5F; /* Lupka też reaguje na hover */
        }

        /* Usunięcie marginesów domyślnych Streamlit */
        .main .block-container {
            padding: 0 !important;
        }
        </style>

        <div id="hero-canvas">
            <nav class="hero-nav">
                <a class="active">Home</a>
                <a>About</a>
                <a>Services</a>
                <a>Portfolio</a>
                <a>Testimonials</a>
                <a>Contact</a>
                <a class="search-icon">
                    <svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round">
                        <circle cx="11" cy="11" r="8"></circle>
                        <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                    </svg>
                </a>
            </nav>
        </div>
    """, unsafe_allow_html=True)

# Wywołanie układu
apply_hero_layout()
