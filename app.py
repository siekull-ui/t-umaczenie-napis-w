import streamlit as st

# --- 1. KONFIGURACJA STRONY ---
st.set_page_config(
    page_title="AI System Pro", 
    page_icon="✨", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# --- 2. INTERFEJS CV (PRZEWIJALNY) ---
def apply_scrollable_prestige_layout():
    style = """
    <style>
    /* UKRYCIE ELEMENTÓW SYSTEMOWYCH */
    [data-testid="stHeader"], [data-testid="stFooter"], [data-testid="stToolbar"] {
        display: none !important;
    }
    
    /* Pozwalamy na scrollowanie głównego kontenera Streamlit */
    .main .block-container { 
        padding: 0 !important; 
        max-width: 100% !important; 
    }

    /* NIESKOŃCZONE TŁO - FIXED, żeby zawsze było pod spodem */
    @keyframes panBackground {
        0% { background-position: 0% 0%; }
        50% { background-position: 100% 100%; }
        100% { background-position: 0% 0%; }
    }
    .stApp {
        background: linear-gradient(135deg, #1e1121 0%, #2d1b33 25%, #e8a2a8 50%, #2d1b33 75%, #1e1121 100%) !important;
        background-size: 400% 400% !important;
        animation: panBackground 40s infinite ease-in-out;
        background-attachment: fixed !important; /* Tło stoi w miejscu podczas scrolla */
        overflow-y: auto !important;
    }

    /* KONFIGURACJA ZMIENNYCH */
    :root {
        --sidebar-width: 320px;
        --margin: 1cm;
        --elastic-curve: cubic-bezier(0.175, 0.885, 0.32, 1.275);
        --container-height: calc(100vh - 2 * var(--margin));
    }

    #sidebar-checkbox {
        display: none;
    }

    /* --- PANEL BOCZNY (ABSOLUTE) --- */
    #custom-sidebar {
        position: absolute; /* Zmienione na absolute, by odjeżdżało w górę */
        top: var(--margin);
        height: var(--container-height);
        left: calc(-1 * var(--sidebar-width) - 2cm);
        width: var(--sidebar-width);
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(40px) saturate(150%);
        -webkit-backdrop-filter: blur(40px) saturate(150%);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 30px;
        transition: left 0.8s var(--elastic-curve);
        z-index: 1000;
    }

    /* --- GŁÓWNY KONTENER (ABSOLUTE) --- */
    #main-canvas {
        position: absolute; /* Zmienione na absolute */
        top: var(--margin);
        height: var(--container-height);
        left: var(--margin);
        right: var(--margin);
        background: rgba(255, 255, 255, 0.07);
        backdrop-filter: blur(45px) saturate(160%);
        -webkit-backdrop-filter: blur(45px) saturate(160%);
        border: 1px solid rgba(255, 255, 255, 0.25);
        border-radius: 35px;
        transition: left 0.8s var(--elastic-curve);
        z-index: 500;
        box-shadow: 0 25px 50px rgba(0, 0, 0, 0.2);
    }

    /* --- STACJONARNA STRZAŁKA --- */
    .toggle-label {
        position: absolute; /* Odjeżdża razem z kontenerem */
        left: 0.35cm;
        top: calc(50vh);
        transform: translateY(-50%);
        cursor: pointer;
        z-index: 2500;
        color: rgba(255, 255, 255, 0.4);
        font-size: 42px;
        font-weight: 100;
        font-family: serif;
        user-select: none;
        transition: transform 0.6s var(--elastic-curve), color 0.3s ease;
    }

    /* --- LOGIKA DYNAMIKI --- */
    #sidebar-checkbox:checked ~ #custom-sidebar {
        left: var(--margin);
    }
    #sidebar-checkbox:checked ~ #main-canvas {
        left: calc(var(--sidebar-width) + var(--margin) + 0.5cm);
    }
    #sidebar-checkbox:checked ~ .toggle-label {
        transform: translateY(-50%) rotate(180deg);
    }

    /* --- SPACER DLA EFEKTU SCROLLA --- */
    .scroll-spacer {
        height: 250vh; /* Zapewnia dużo miejsca na dole do scrollowania */
        width: 100%;
        pointer-events: none; /* Żeby nie blokował interakcji */
    }
    </style>

    <input type="checkbox" id="sidebar-checkbox">
    <label for="sidebar-checkbox" class="toggle-label">›</label>
    
    <div id="custom-sidebar"></div>
    <div id="main-canvas"></div>
    
    <div class="scroll-spacer"></div>
    """
    st.markdown(style, unsafe_allow_html=True)

# Wywołanie interfejsu
apply_scrollable_prestige_layout()
