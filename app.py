import streamlit as st

# --- 1. KONFIGURACJA STRONY ---
st.set_page_config(
    page_title=" ", 
    page_icon="✨", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# --- 2. GŁÓWNY STYL CSS (TŁO + GUMOWY KONTENER) ---
def apply_elastic_layout():
    style = """
    <style>
    /* Ukrycie elementów systemowych Streamlit */
    [data-testid="stHeader"], 
    [data-testid="stFooter"], 
    [data-testid="stToolbar"] {
        display: none !important;
    }

    /* Reset głównego kontenera */
    .main .block-container {
        padding: 0 !important;
        max-width: 100% !important;
    }

    /* Nieskończone, animowane tło */
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

    /* --- SPRĘŻYSTY KONTENER GLASSMORPHISM --- */
    .elastic-glass-canvas {
        /* Pozycjonowanie 1cm od każdej krawędzi */
        position: fixed;
        top: 1cm;
        left: 1cm;
        right: 1cm;
        bottom: 1cm;
        
        /* Wygląd: Glassmorphism (90% przepuszczalności) */
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(45px) saturate(160%);
        -webkit-backdrop-filter: blur(45px) saturate(160%);
        
        /* Obramowanie i cień */
        border: 1px solid rgba(255, 255, 255, 0.25);
        border-radius: 35px;
        box-shadow: 0 25px 50px rgba(0, 0, 0, 0.2);
        
        /* EFEKT GUMY (SPRĘŻYSTOŚĆ) */
        /* Ten bezier sprawia, że ruch jest "żywy" i lekko odbija */
        transition: all 0.6s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        
        z-index: 100;
        overflow: hidden;
    }

    /* Dodatkowa interakcja przy najechaniu (poczucie elastyczności) */
    .elastic-glass-canvas:hover {
        transform: scale(1.005); /* Minimalne powiększenie */
        background: rgba(255, 255, 255, 0.12);
        border-color: rgba(255, 255, 255, 0.4);
    }

    /* Subtelne rozświetlenie góry dla lepszego detalu 3D */
    .elastic-glass-canvas::after {
        content: "";
        position: absolute;
        top: 0; left: 0; right: 0; height: 100px;
        background: linear-gradient(to bottom, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0) 100%);
        pointer-events: none;
    }
    </style>
    
    <div class="elastic-glass-canvas">
        </div>
    """
    st.markdown(style, unsafe_allow_html=True)

# Wywołanie interfejsu
apply_elastic_layout()
