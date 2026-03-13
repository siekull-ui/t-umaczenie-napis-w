import streamlit as st

# --- 1. KONFIGURACJA STRONY ---
st.set_page_config(
    page_title=" ", 
    page_icon="✨", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# --- 2. CZYSTY KOD CSS (TYLKO TŁO I UKRYCIE ELEMENTÓW) ---
def apply_clean_layout():
    style = """
    <style>
    /* Ukrycie wszystkich domyślnych elementów Streamlit */
    [data-testid="stHeader"], 
    [data-testid="stFooter"], 
    [data-testid="stToolbar"],
    [data-testid="stSidebar"] {
        display: none !important;
    }

    /* Reset marginesów i paddingów */
    .main .block-container {
        padding: 0 !important;
        max-width: 100% !important;
    }

    /* Animacja tła */
    @keyframes panBackground {
        0% { background-position: 0% 0%; }
        50% { background-position: 100% 100%; }
        100% { background-position: 0% 0%; }
    }
    
    /* Główne tło - nieskończone i responsywne */
    .stApp {
        background: linear-gradient(
            135deg,
            #1e1121 0%,      /* Bardzo ciemny fiolet */
            #2d1b33 25%,     /* Głęboki fiolet */
            #e8a2a8 50%,     /* Twój charakterystyczny róż/łososiowy */
            #2d1b33 75%,
            #1e1121 100%
        ) !important;
        
        background-size: 400% 400% !important; /* Powiększenie dla płynności animacji */
        background-attachment: fixed !important;
        animation: panBackground 40s infinite ease-in-out;
    }

    /* Efekt szklanej powłoki na całości */
    [data-testid="stAppViewContainer"] {
        background: rgba(255, 255, 255, 0.03) !important;
        backdrop-filter: blur(15px) !important;
        -webkit-backdrop-filter: blur(15px) !important;
    }
    </style>
    """
    st.markdown(style, unsafe_allow_html=True)

# Wywołanie czystego układu
apply_clean_layout()

# --- 3. BRAK TREŚCI ---
# Ekran pozostaje pusty.
