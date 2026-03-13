import streamlit as st

# --- 1. KONFIGURACJA STRONY ---
st.set_page_config(
    page_title=" ", 
    page_icon="✨", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# --- 2. GŁÓWNY STYL CSS ---
def apply_styles():
    style = """
    <style>
    /* Ukrycie elementów systemowych */
    [data-testid="stHeader"], 
    [data-testid="stFooter"], 
    [data-testid="stToolbar"] {
        display: none !important;
    }

    /* Reset kontenera głównego Streamlit */
    .main .block-container {
        padding: 0 !important;
        max-width: 100% !important;
    }

    /* Animacja tła (Twoje nieskończone tło) */
    @keyframes panBackground {
        0% { background-position: 0% 0%; }
        50% { background-position: 100% 100%; }
        100% { background-position: 0% 0%; }
    }

    .stApp {
        background: linear-gradient(
            135deg,
            #1e1121 0%,
            #2d1b33 25%,
            #e8a2a8 50%,
            #2d1b33 75%,
            #1e1121 100%
        ) !important;
        background-size: 400% 400% !important;
        animation: panBackground 40s infinite ease-in-out;
    }

    /* --- GUMOWY KONTENER GLASSMORPHISM --- */
    .glass-canvas {
        position: fixed;
        top: 1cm;
        left: 1cm;
        right: 1cm;
        bottom: 1cm;
        
        /* Glassmorphism setup */
        background: rgba(255, 255, 255, 0.07); /* Przepuszczalność ~90% */
        backdrop-filter: blur(40px) saturate(150%);
        -webkit-backdrop-filter: blur(40px) saturate(150%);
        
        /* Detale wykończenia */
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 30px;
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.3);
        
        /* Efekt "gumy" - płynne przejście przy zmianie rozmiaru okna */
        transition: all 0.6s cubic-bezier(0.25, 1, 0.5, 1);
        
        z-index: 100;
        overflow: hidden;
    }

    /* Subtelne rozświetlenie krawędzi (detal) */
    .glass-canvas::before {
        content: "";
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        border-radius: 30px;
        background: linear-gradient(135deg, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0) 100%);
        pointer-events: none;
    }
    </style>
    
    <div class="glass-canvas">
        </div>
    """
    st.markdown(style, unsafe_allow_html=True)

# Wywołanie stylu
apply_styles()
