import streamlit as st

# --- 1. CONFIG ---
st.set_page_config(
    page_title="Blank Hero",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. CSS: HERO GLASS CONTAINER ---
st.markdown("""
    <style>
    /* Ukrycie elementów systemowych */
    [data-testid="stHeader"], [data-testid="stFooter"], [data-testid="stToolbar"] {
        display: none !important;
    }

    /* Różowe tło bazowe */
    .stApp {
        background-color: #F0D3DE !important;
    }

    /* Stylizacja głównego obszaru jako satynowy kontener Hero */
    [data-testid="stAppViewBlockContainer"] {
        /* Kolor i przezroczystość */
        background: rgba(255, 255, 255, 0.9) !important;
        
        /* Glassmorphism / Satyna */
        backdrop-filter: blur(30px) !important;
        -webkit-backdrop-filter: blur(30px) !important;
        
        /* Marginesy i zaokrąglenie */
        margin: 1cm !important;
        border-radius: 1cm !important;
        
        /* Dopasowanie do ekranu */
        min-height: calc(100vh - 2cm) !important;
        width: calc(100% - 2cm) !important;
        
        /* Obramowanie dla widoczności krawędzi (efekt szkła) */
        border: 1px solid rgba(255, 255, 255, 0.6) !important;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.05) !important;
        
        /* Reset paddingów Streamlit */
        padding: 0 !important;
    }

    /* Usunięcie ograniczenia szerokości narzucanego przez Streamlit */
    .main .block-container {
        max-width: 100% !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. INICJACJA KONTENERA ---
# Dodajemy pusty kontener, aby wymusić renderowanie stylów
with st.container():
    st.write("")
