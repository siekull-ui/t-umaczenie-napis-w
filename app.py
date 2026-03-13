import streamlit as st

# --- 1. KONFIGURACJA STRONY ---
st.set_page_config(
    page_title=" ", 
    page_icon="✨", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# --- 2. LOGIKA INTERFEJSU (CSS + JS) ---
def apply_pro_layout():
    style = """
    <style>
    /* UKRYCIE ELEMENTÓW SYSTEMOWYCH */
    [data-testid="stHeader"], [data-testid="stFooter"], [data-testid="stToolbar"] {
        display: none !important;
    }
    .main .block-container { padding: 0 !important; max-width: 100% !important; }

    /* TŁO INFINITY */
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

    /* ZMIENNE DLA DYNAMIKI */
    :root {
        --sidebar-width: 300px;
        --margin: 1cm;
        --rubber-transition: all 0.8s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }

    /* PANEL BOCZNY (SIDEBAR) */
    #custom-sidebar {
        position: fixed;
        top: var(--margin);
        bottom: var(--margin);
        left: calc(-1 * var(--sidebar-width) - 2cm); /* Ukryty poza ekranem */
        width: var(--sidebar-width);
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(40px) saturate(150%);
        -webkit-backdrop-filter: blur(40px) saturate(150%);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 30px;
        transition: var(--rubber-transition);
        z-index: 1000;
        box-shadow: 20px 0 50px rgba(0,0,0,0.2);
    }

    /* KONTENER GŁÓWNY */
    #main-canvas {
        position: fixed;
        top: var(--margin);
        bottom: var(--margin);
        left: var(--margin);
        right: var(--margin);
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(45px) saturate(160%);
        -webkit-backdrop-filter: blur(45px) saturate(160%);
        border: 1px solid rgba(255, 255, 255, 0.25);
        border-radius: 35px;
        transition: var(--rubber-transition);
        z-index: 500;
        box-shadow: 0 25px 50px rgba(0, 0, 0, 0.2);
    }

    /* STAN AKTYWNY (PO KLIKNIĘCIU) */
    body.sidebar-open #custom-sidebar {
        left: var(--margin);
    }
    body.sidebar-open #main-canvas {
        left: calc(var(--sidebar-width) + var(--margin) + 0.5cm); /* "Ściśnięcie" kontenera */
    }

    /* PULSUJĄCA STRZAŁKA */
    @keyframes pulse {
        0% { transform: scale(1); opacity: 0.6; box-shadow: 0 0 0 0 rgba(255,255,255,0.4); }
        70% { transform: scale(1.2); opacity: 1; box-shadow: 0 0 20px 10px rgba(255,255,255,0); }
        100% { transform: scale(1); opacity: 0.6; }
    }

    #toggle-btn {
        position: fixed;
        left: 15px;
        top: 50%;
        transform: translateY(-50%);
        width: 40px;
        height: 40px;
        background: rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(10px);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        z-index: 2000;
        border: 1px solid rgba(255, 255, 255, 0.4);
        animation: pulse 2s infinite;
        transition: var(--rubber-transition);
        color: white;
        font-size: 20px;
        user-select: none;
    }

    body.sidebar-open #toggle-btn {
        left: calc(var(--sidebar-width) + var(--margin) + 10px);
        transform: translateY(-50%) rotate(180deg);
    }
    </style>

    <div id="toggle-btn" onclick="toggleSidebar()">❯</div>
    <div id="custom-sidebar"></div>
    <div id="main-canvas"></div>

    <script>
    function toggleSidebar() {
        document.body.classList.toggle('sidebar-open');
    }
    </script>
    """
    st.markdown(style, unsafe_allow_html=True)

# Wywołanie interfejsu
apply_pro_layout()
