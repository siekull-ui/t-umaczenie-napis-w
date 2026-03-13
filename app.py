import streamlit as st

# --- 1. KONFIGURACJA STRONY ---
st.set_page_config(
    page_title="AI System Pro", 
    page_icon="✨", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# --- 2. KOMPLETNY INTERFEJS (CSS + JS + HTML) ---
def apply_elastic_sidebar_layout():
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
        /* TWOJA KRZYWA SPRĘŻYSTOŚCI */
        --elastic-curve: cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }

    /* PANEL BOCZNY (SIDEBAR) */
    #custom-sidebar {
        position: fixed;
        top: var(--margin);
        bottom: var(--margin);
        left: calc(-1 * var(--sidebar-width) - 2cm); /* Ukryty poza lewą krawędzią */
        width: var(--sidebar-width);
        background: rgba(255, 255, 255, 0.08); /* 92% przezroczystości */
        backdrop-filter: blur(40px) saturate(150%);
        -webkit-backdrop-filter: blur(40px) saturate(150%);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 30px;
        transition: all 0.8s var(--elastic-curve);
        z-index: 1000;
        box-shadow: 15px 0 40px rgba(0,0,0,0.2);
    }

    /* GŁÓWNY KONTENER (CANVAS) */
    #main-canvas {
        position: fixed;
        top: var(--margin);
        bottom: var(--margin);
        left: var(--margin);
        right: var(--margin);
        background: rgba(255, 255, 255, 0.07); /* ~93% przezroczystości */
        backdrop-filter: blur(45px) saturate(160%);
        -webkit-backdrop-filter: blur(45px) saturate(160%);
        border: 1px solid rgba(255, 255, 255, 0.25);
        border-radius: 35px;
        transition: all 0.8s var(--elastic-curve);
        z-index: 500;
        box-shadow: 0 25px 50px rgba(0, 0, 0, 0.2);
    }

    /* --- LOGIKA ŚCISKANIA (SQUEEZE) --- */
    body.sidebar-active #custom-sidebar {
        left: var(--margin);
    }

    body.sidebar-active #main-canvas {
        /* Ściska kontener: lewa krawędź przesuwa się, by zrobić miejsce dla panelu + odstęp */
        left: calc(var(--sidebar-width) + var(--margin) + 0.5cm);
    }

    /* PULSUJĄCY PRZYCISK / STRZAŁKA */
    @keyframes pulse-ring {
        0% { transform: scale(1); box-shadow: 0 0 0 0 rgba(255, 255, 255, 0.4); }
        70% { transform: scale(1.1); box-shadow: 0 0 0 15px rgba(255, 255, 255, 0); }
        100% { transform: scale(1); box-shadow: 0 0 0 0 rgba(255, 255, 255, 0); }
    }

    #sidebar-toggle {
        position: fixed;
        left: 20px;
        top: 50%;
        transform: translateY(-50%);
        width: 45px;
        height: 45px;
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.4);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        z-index: 2000;
        color: white;
        font-size: 22px;
        animation: pulse-ring 2s infinite ease-in-out;
        transition: all 0.6s var(--elastic-curve);
        user-select: none;
    }

    /* Obrót strzałki i przesunięcie przycisku przy otwarciu */
    body.sidebar-active #sidebar-toggle {
        left: calc(var(--sidebar-width) + var(--margin) + 15px);
        transform: translateY(-50%) rotate(180deg);
        background: rgba(255, 255, 255, 0.3);
    }

    #sidebar-toggle:hover {
        background: rgba(255, 255, 255, 0.4);
        transform: translateY(-50%) scale(1.2);
    }
    </style>

    <div id="sidebar-toggle" onclick="document.body.classList.toggle('sidebar-active')">❯</div>
    <div id="custom-sidebar"></div>
    <div id="main-canvas"></div>
    """
    st.markdown(style, unsafe_allow_html=True)

# Wywołanie układu
apply_elastic_sidebar_layout()
