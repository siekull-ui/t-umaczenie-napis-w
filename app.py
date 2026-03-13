import streamlit as st

# --- 1. KONFIGURACJA STRONY ---
st.set_page_config(
    page_title="Blank Hero",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. ZARZĄDZANIE STANEM (SESSION STATE) ---
if 'active_tab' not in st.session_state:
    st.session_state.active_tab = 'Home'

def set_tab(tab_name):
    st.session_state.active_tab = tab_name

# --- 3. GŁÓWNY INTERFEJS ---
def apply_hero_layout():
    # A. Style CSS
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500&display=swap');

        /* UKRYCIE ELEMENTÓW SYSTEMOWYCH */
        [data-testid="stHeader"], [data-testid="stFooter"], [data-testid="stToolbar"] {
            display: none !important;
        }

        /* TŁO APLIKACJI */
        .stApp {
            background-color: #F0D3DE !important;
        }

        /* KONTENER HERO (Strukturalny) */
        [data-testid="stAppViewBlockContainer"] {
            position: fixed !important;
            top: 1cm !important;
            bottom: 1cm !important;
            left: 1cm !important;
            right: 1cm !important;
            
            background: rgba(255, 255, 255, 0.25) !important;
            backdrop-filter: blur(25px) saturate(150%) !important;
            -webkit-backdrop-filter: blur(25px) saturate(150%) !important;
            
            border-radius: 1cm !important;
            border: none !important;
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15) !important;
            
            z-index: 1000 !important;
            
            /* Usunięcie domyślnych paddingów żeby móc swobodnie układać elementy */
            padding: 0 !important;
            max-width: none !important;
        }

        /* --- STYLIZACJA PRZYCISKÓW STREAMLIT JAKO NAWIGACJI --- */
        /* Kontener na przyciski w prawym górnym rogu */
        .nav-container {
            position: absolute;
            top: 40px;
            right: 50px;
            display: flex;
            gap: 20px;
            align-items: center;
            z-index: 1001;
        }

        /* Targetowanie przycisków wewnątrz kontenera nav */
        div[data-testid="stButton"] > button {
            background: transparent !important;
            border: none !important;
            color: #1a1a1a !important;
            font-family: 'Poppins', sans-serif !important;
            font-size: 14px !important;
            font-weight: 500 !important;
            padding: 0 !important;
            box-shadow: none !important;
            position: relative;
        }
        
        div[data-testid="stButton"] > button:focus {
             box-shadow: none !important;
        }

        /* Hover dla lupki (ostatni przycisk) nie potrzebujemy go, dodajemy klasę dla lupy niżej */

        /* --- STREFA ZAWARTOŚCI NA ŚRODKU --- */
        .content-area {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            text-align: center;
            font-family: 'Poppins', sans-serif;
            color: rgba(26, 26, 26, 0.8);
            z-index: 1000;
        }
        
        .content-title {
            font-size: 150px;
            font-weight: 300;
            margin: 0;
            line-height: 1;
            animation: fadeIn 0.6s ease-out;
        }
        
        .content-subtitle {
             font-size: 24px;
             font-weight: 400;
             margin-top: 20px;
             animation: fadeIn 0.8s ease-out;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        </style>
    """, unsafe_allow_html=True)

    # B. Renderowanie Nawigacji (Używamy kolumn Streamlit pozycjonowanych CSS)
    # Zamiast HTML, używamy przycisków Streamlit otoczonych tagiem div z klasą nav-container
    st.markdown('<div class="nav-container">', unsafe_allow_html=True)
    
    # Tworzymy layout kolumn w prawym górnym rogu dla przycisków
    col1, col2, col3, col4, col5, col6 = st.columns([1,1,1,1,1,1])
    
    tabs = ["Home", "About", "Services", "Portfolio", "Contact"]
    
    with col1:
        if st.button("Home"): set_tab("Home")
    with col2:
        if st.button("About"): set_tab("About")
    with col3:
        if st.button("Services"): set_tab("Services")
    with col4:
        if st.button("Portfolio"): set_tab("Portfolio")
    with col5:
        if st.button("Contact"): set_tab("Contact")
    with col6:
         # Atrapa lupy jako emoji dla uproszczenia przycisków
         st.button("🔍")

    st.markdown('</div>', unsafe_allow_html=True)

    # C. Dynamiczne wstrzykiwanie fali pod AKTYWNY element
    active_idx = tabs.index(st.session_state.active_tab)
    # Dodajemy style dla fali używając pseudo-klasy :nth-child dla konkretnej kolumny (plus 1 bo index w nth-child od 1)
    wave_css = f"""
        <style>
         div[data-testid="column"]:nth-child({active_idx + 1}) div[data-testid="stButton"] > button::after {{
            content: '';
            position: absolute;
            bottom: -10px;
            left: -15px;
            right: -15px;
            height: 6px;
            background-image: url("data:image/svg+xml,%3Csvg width='30' height='6' viewBox='0 0 30 6' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M0 3C5 1 10 1 15 3C20 5 25 5 30 3' stroke='%23FF2A5F' stroke-width='1.5' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E");
            background-repeat: repeat-x;
        }}
        </style>
    """
    st.markdown(wave_css, unsafe_allow_html=True)

    # D. Renderowanie zawartości w zależności od stanu
    content_html = f"""
        <div class="content-area">
            <h1 class="content-title">{tabs.index(st.session_state.active_tab) + 1}</h1>
            <p class="content-subtitle">Welcome to the {st.session_state.active_tab} section</p>
        </div>
    """
    st.markdown(content_html, unsafe_allow_html=True)

# Wywołanie interfejsu
apply_hero_layout()
