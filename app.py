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
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;700&display=swap');

        /* Ukrycie elementów systemowych Streamlit */
        [data-testid="stHeader"], [data-testid="stFooter"], [data-testid="stToolbar"] {
            display: none !important;
        }

        /* Tło aplikacji */
        .stApp {
            background-color: #F0D3DE !important;
        }

        /* UKRYTE WEJŚCIA STERUJĄCE LOGIKĄ (Tylko zakładki) */
        input[type="radio"] {
            display: none;
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
            overflow: hidden;
        }

        /* --- NAWIGACJA GŁÓWNA --- */
        .hero-nav {
            position: absolute;
            top: 40px;
            right: 50px;
            display: flex;
            align-items: center;
            justify-content: flex-end;
            font-family: 'Poppins', sans-serif;
            z-index: 100;
        }

        .nav-links {
            display: flex;
            gap: 60px;
            align-items: center;
        }

        .nav-links label {
            color: #1a1a1a;
            font-size: 14px;
            font-weight: 500;
            cursor: pointer;
            position: relative;
        }

        /* Fala pod tekstami */
        .nav-links label::after {
            content: '';
            position: absolute;
            bottom: -10px;
            left: -15px;
            right: -15px;
            height: 6px;
            background-image: url("data:image/svg+xml,%3Csvg width='30' height='6' viewBox='0 0 30 6' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M0 3C5 1 10 1 15 3C20 5 25 5 30 3' stroke='%23FF2A5F' stroke-width='1.5' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E");
            background-repeat: repeat-x;
            opacity: 0;
            transition: opacity 0.4s ease;
        }

        /* AKTYWACJA FALI W ZALEŻNOŚCI OD ZAKŁADKI */
        #tab-1:checked ~ .hero-nav .nav-links label[for="tab-1"]::after,
        #tab-2:checked ~ .hero-nav .nav-links label[for="tab-2"]::after,
        #tab-3:checked ~ .hero-nav .nav-links label[for="tab-3"]::after,
        #tab-4:checked ~ .hero-nav .nav-links label[for="tab-4"]::after,
        #tab-5:checked ~ .hero-nav .nav-links label[for="tab-5"]::after {
            opacity: 1;
        }

        /* --- STREFA ZAWARTOŚCI NA ŚRODKU --- */
        .content-area {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 100%;
            height: 100%;
            pointer-events: none;
        }

        .content-item {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -45%); 
            font-family: 'Poppins', sans-serif;
            font-size: 150px;
            font-weight: 300;
            color: rgba(26, 26, 26, 0.8);
            opacity: 0;
            transition: all 0.7s cubic-bezier(0.16, 1, 0.3, 1);
        }

        /* POJAWIANIE SIĘ TREŚCI */
        #tab-1:checked ~ .content-area #content-1,
        #tab-2:checked ~ .content-area #content-2,
        #tab-3:checked ~ .content-area #content-3,
        #tab-4:checked ~ .content-area #content-4,
        #tab-5:checked ~ .content-area #content-5 {
            opacity: 1;
            transform: translate(-50%, -50%);
        }

        .main .block-container {
            padding: 0 !important;
        }
        </style>

        <div id="hero-canvas">
            
            <input type="radio" name="tabs" id="tab-1" checked>
            <input type="radio" name="tabs" id="tab-2">
            <input type="radio" name="tabs" id="tab-3">
            <input type="radio" name="tabs" id="tab-4">
            <input type="radio" name="tabs" id="tab-5">

            <nav class="hero-nav">
                <div class="nav-links">
                    <label for="tab-1">Home</label>
                    <label for="tab-2">About</label>
                    <label for="tab-3">Services</label>
                    <label for="tab-4">Portfolio</label>
                    <label for="tab-5">Contact</label>
                </div>
            </nav>

            <div class="content-area">
                <div class="content-item" id="content-1">1</div>
                <div class="content-item" id="content-2">2</div>
                <div class="content-item" id="content-3">3</div>
                <div class="content-item" id="content-4">4</div>
                <div class="content-item" id="content-5">5</div>
            </div>

        </div>
    """, unsafe_allow_html=True)

# Wywołanie interfejsu
apply_hero_layout()
