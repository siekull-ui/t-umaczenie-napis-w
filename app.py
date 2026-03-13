import streamlit as st

# --- 1. KONFIGURACJA STRONY ---
st.set_page_config(
    page_title="Satin Glass UI",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. STYLIZACJA CSS (GLASSMORPHISM) ---
st.markdown("""
    <style>
    /* Ukrycie elementów systemowych */
    [data-testid="stHeader"], [data-testid="stFooter"], [data-testid="stToolbar"] {
        display: none !important;
    }

    /* Tło całej aplikacji */
    .stApp {
        background-color: #F0D3DE !important;
        overflow: hidden; /* Zapobiega pojawianiu się pasków przewijania strony głównej */
    }

    /* Główny kontener - Efekt Glassmorphism */
    .main .block-container {
        /* Kolor jasny, 90% przezroczystości (0.9) */
        background: rgba(255, 255, 255, 0.9) !important;
        
        /* Efekt satynowy/blur */
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        
        /* Geometria: marginesy 1cm i dopasowanie do ekranu */
        margin: 1cm !important;
        padding: 2rem !important; /* Wewnętrzny odstęp dla treści */
        border-radius: 1cm !important;
        
        /* Dynamiczne dopasowanie wysokości i szerokości */
        height: calc(100vh - 2cm) !important;
        min-height: calc(100vh - 2cm) !important;
        max-width: calc(100% - 2cm) !important;
        
        /* Delikatne obramowanie i cień dla podbicia efektu glass */
        border: 1px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.05);
        
        /* Centrowanie zawartości w pionie/poziomie (opcjonalnie) */
        display: flex;
        flex-direction: column;
    }

    /* Resetowanie domyślnych marginesów Streamlit dla elementów wewnątrz */
    [data-testid="stVerticalBlock"] {
        gap: 1rem;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. TREŚĆ ---
st.title("Satynowy Interfejs")
st.write("Ten kontener idealnie przylega do krawędzi z zachowaniem 1-centymetrowego odstępu.")
st.info("Efekt 'Matte' jest najlepiej widoczny, gdy pod kontenerem znajdują się jakieś kształty lub gdy zmienisz kolor tła na gradient.")
