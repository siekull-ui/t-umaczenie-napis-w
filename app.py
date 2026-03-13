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

        /* UKRYTE WEJŚCIA STERUJĄCE LOGIKĄ (Niewidoczne dla użytkownika) */
        input[type="radio"], input[type="checkbox"] {
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
            overflow: hidden; /* Utrzymuje elementy wewnątrz zaokrągleń */
        }

        /* --- NAWIGACJA GŁÓWNA --- */
        .hero-nav {
            position: absolute;
            top: 40px;
            right: 50px;
            display: flex;
            align-items: center;
            justify-content: flex-end; /* Elementy wyrównane do prawej */
            font-family: 'Poppins', sans-serif;
            z-index: 100;
        }

        .nav-links {
            display: flex;
            gap: 60px;
            align-items: center;
            /* Płynne przesuwanie w lewo po rozwinięciu lupy */
            transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);
        }

        .nav-links label {
            color: #1a1a1a;
            font-size: 14px;
            font-weight: 500;
            cursor: pointer;
            position: relative;
        }

        /* Fala pod tekstami (domyślnie ukryta) */
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

        /* AKTYWACJA FALI W ZALEŻNOŚCI OD WYBRANEJ ZAKŁADKI */
        #tab-1:checked ~ .hero-nav .nav-links label[for="tab-1"]::after,
        #tab-2:checked ~ .hero-nav .nav-links label[for="tab-2"]::after,
        #tab-3:checked ~ .hero-nav .nav-links label[for="tab-3"]::after,
        #tab-4:checked ~ .hero-nav .nav-links label[for="tab-4"]::after,
        #tab-5:checked ~ .hero-nav .nav-links label[for="tab-5"]::after {
            opacity: 1;
        }

        /* --- PASEK WYSZUKIWANIA (LUPKA) --- */
        .search-container {
            display: flex;
            align-items: center;
            margin-left: 60px; /* Odstęp od ostatniego napisu */
            background: rgba(255, 255, 255, 0);
            border-radius: 30px; /* Mocne zaokrąglenia dla kontenerka */
            padding: 0;
            /* Ultra-płynna animacja całego kontenera */
            transition: all 0.6s cubic-bezier(0.16, 1, 0.3, 1);
            overflow: hidden;
        }

        .search-input {
            width: 0; /* Domyślnie schowany */
            opacity: 0;
            border: none;
            background: transparent;
            outline: none;
            font-family: 'Poppins', sans-serif;
            font-size: 14px;
            color: #1a1a1a;
            transition: all 0.6s cubic-bezier(0.16, 1, 0.3, 1);
            padding: 0;
        }

        .search-input::placeholder {
            color: #a0a0a0;
        }

        .search-icon-label {
            cursor: pointer;
            display: flex;
            align-items: center;
            padding: 8px; /* Zwiększony obszar kliknięcia */
            border-radius: 50%;
            transition: background 0.3s ease;
        }

        .search-icon-label svg {
            width: 18px;
            height: 18px;
            stroke: #1a1a1a;
            stroke-width: 2;
            transition: stroke 0.3s ease;
        }

        /* EFEKT PO KLIKNIĘCIU W LUPKĘ */
        #search-toggle:checked ~ .hero-nav .search-container {
            background: #ffffff; /* Białe tło po wysunięciu */
            padding: 2px 15px 2px 20px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
            /* Zmniejszamy trochę margines, by płynniej pchnąć menu */
            margin-left: 40px; 
        }

        #search-toggle:checked ~ .hero-nav .search-container .search-input {
            width: 160px; /* Pole się rozszerza */
            opacity: 1; /* Pojawia się */
            padding-right: 10px;
        }

        #search-toggle:checked ~ .hero-nav .search-container .search-icon-label svg {
            stroke: #FF2A5F; /* Zmiana koloru lupy na aktywny */
        }

        /* --- STREFA ZAWARTOŚCI NA ŚRODKU (1, 2, 3, 4, 5) --- */
        .content-area {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 100%;
            height: 100%;
            pointer-events: none; /* Żeby liczby nie blokowały kliknięć np. pod spodem */
        }

        .content-item {
            position: absolute;
            top: 50%;
            left: 50%;
            /* Zaczynamy animację lekko z dołu (-45%) dla efektu wypłynięcia */
            transform: translate(-50%, -45%); 
            font-family: 'Poppins', sans-serif;
            font-size: 150px;
            font-weight: 300; /* Cienki, nowoczesny wariant */
            color: rgba(26, 26, 26, 0.8); /* Lekko prześwitujący grafit */
            opacity: 0;
            transition: all 0.7s cubic-bezier(0.16, 1, 0.3, 1);
        }

        /* POJAWIANIE SIĘ TREŚCI ZGODNIE Z ZAKŁADKĄ */
        #tab-1:checked ~ .content-area #content-1,
        #tab-2:checked ~ .content-area #content-2,
        #tab-3:checked ~ .content-area #content-3,
        #tab-4:checked ~ .content-area #content-4,
        #tab-5:checked ~ .content-area #content-5 {
            opacity: 1;
            transform: translate(-50%, -50%); /* Liczba wjeżdża idealnie na środek */
        }

        /* Usunięcie domyślnych zachowań Streamlit */
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
            <input type="checkbox" id="search-toggle">

            <nav class="hero-nav">
                <div class="nav-links">
                    <label for="tab-1">Home</label>
                    <label for="tab-2">About</label>
                    <label for="tab-3">Services</label>
                    <label for="tab-4">Portfolio</label>
                    <label for="tab-5">Contact</label>
                </div>
                
                <div class="search-container">
                    <input type="text" class="search-input" placeholder="Wyszukaj...">
                    <label for="search-toggle" class="search-icon-label">
                        <svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round">
                            <circle cx="11" cy="11" r="8"></circle>
                            <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                        </svg>
                    </label>
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

# Wywołanie układu
apply_hero_layout()
