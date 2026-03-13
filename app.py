import streamlit as st

# --- 1. KONFIGURACJA STRONY ---
st.set_page_config(
    page_title="AI System Pro", 
    page_icon="✨", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# --- 2. KOMPLETNY INTERFEJS (CSS + HTML) ---
def apply_minimalist_layout():
    style = """
    <style>
    /* UKRYCIE ELEMENTÓW SYSTEMOWYCH */
    [data-testid="stHeader"], [data-testid="stFooter"], [data-testid="stToolbar"] {
        display: none !important;
    }
    .main .block-container { padding: 0 !important; max-width: 100% !important; }

    /* NIESKOŃCZONE TŁO */
    @keyframes panBackground {
        0% { background-position: 0% 0%; }
        50% { background-position: 100% 100%; }
        100% { background-position: 0% 0%; }
    }
    .stApp {
        background: linear-gradient(135deg, #1e1121 0%, #2d1b33 25%, #e8a2a8 50%, #2d1b33 75%, #1e1121 100%) !important;
        background-size: 400% 400% !important;
        animation: panBackground 40s infinite ease-in-out;
    }

    /* KONFIGURACJA ZMIENNYCH */
    :root {
        --sidebar-width: 320px;
        --margin: 1cm;
        --elastic-curve: cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }

    #sidebar-checkbox {
        display: none;
    }

    /* PANEL BOCZNY */
    #custom-sidebar {
        position: fixed;
        top: var(--margin);
        bottom: var(--margin);
        left: calc(-1 * var(--sidebar-width) - 2cm);
        width: var(--sidebar-width);
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(40px) saturate(150%);
        -webkit-backdrop-filter: blur(40px) saturate(150%);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 30px;
        transition: all 0.8s var(--elastic-curve);
        z-index: 1000;
    }

    /* GŁÓWNY KONTENER */
    #main-canvas {
        position: fixed;
        top: var(--margin);
        bottom: var(--margin);
        left: var(--margin);
        right: var(--margin);
        background: rgba(255, 255, 255, 0.07);
        backdrop-filter: blur(45px) saturate(160%);
        -webkit-backdrop-filter: blur(45px) saturate(160%);
        border: 1px solid rgba(255, 255, 255, 0.25);
        border-radius: 35px;
        transition: all 0.8s var(--elastic-curve);
        z-index: 500;
        box-shadow: 0 25px 50px rgba(0, 0, 0, 0.2);
    }

    /* MINIMALISTYCZNA STRZAŁKA (LABEL) */
    .toggle-label {
        position: fixed;
        /* Umiejscowienie wewnątrz marginesu 1cm */
        left: 0.35cm; 
        top: 50%;
        transform: translateY(-50%);
        cursor: pointer;
        z-index: 2000;
        color: rgba(255, 255, 255, 0.6);
        font-size: 40px;
        font-weight: 100; /* Bardzo cienka */
        font-family: serif; /* Dla ładniejszego kształtu '>' */
        transition: all 0.8s var(--elastic-curve);
        user-select: none;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .toggle-label:hover {
        color: white;
        transform: translateY(-50%) scale(1.2);
    }

    /* LOGIKA DYNAMIKI */
    
    #sidebar-checkbox:checked ~ #custom-sidebar {
        left: var(--margin);
    }

    #sidebar-checkbox:checked ~ #main-canvas {
        left: calc(var(--sidebar-width) + var(--margin) + 0.5cm);
    }

    #sidebar-checkbox:checked ~ .toggle-label {
        /* Przesunięcie do marginesu między panelem a kontenerem */
        left: calc(var(--sidebar-width) + var(--margin) + 0.1cm);
        transform: translateY(-50%) rotate(180deg);
        color: rgba(255, 255, 255, 0.8);
    }
    </style>

    <input type="checkbox" id="sidebar-checkbox">
    <label for="sidebar-checkbox" class="toggle-label">›</label>
    
    <div id="custom-sidebar"></div>
    <div id="main-canvas"></div>
    """
    st.markdown(style, unsafe_allow_html=True)

# Wywołanie interfejsu
apply_minimalist_layout()
