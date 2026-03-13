import streamlit as st

# --- 1. FUNKCJA DO ZASTOSOWANIA NIESKOŃCZONEGO TŁA CSS ---
def set_infinite_background():
    custom_css = '''
    <style>
    /* Animacja tła */
    @keyframes panBackground {
        0% { background-position: center top; }
        50% { background-position: center bottom; }
        100% { background-position: center top; }
    }
    
    /* Zastosowanie tła na całą aplikację */
    .stApp {
        /* Gradient liniowy na osi pionowej, odwzorowujący Twoje tło */
        background-image: linear-gradient(
            to bottom,
            rgba(30, 17, 33, 1) 0%,      /* Ciemny fiolet na górze */
            rgba(232, 162, 168, 1) 50%,   /* Jasny róż pośrodku */
            rgba(30, 17, 33, 1) 100%     /* Ciemny fiolet na dole */
        ) !important;
        
        background-size: cover !important;      /* Tło pokrywa cały ekran */
        background-position: center !important;  /* Środek tła na środku ekranu */
        background-repeat: no-repeat !important; /* Brak powielania */
        background-attachment: fixed !important;  /* Tło nieruchome względem przewijania */
        
        /* Zastosowanie animacji */
        animation: panBackground 30s infinite alternate ease-in-out;
    }

    /* Zachowanie efektu szklanej tafli */
    [data-testid="stAppViewContainer"] {
        background: rgba(255, 255, 255, 0.1) !important;
        backdrop-filter: blur(25px) !important;
        -webkit-backdrop-filter: blur(25px) !important;
    }
    </style>
    '''
    st.markdown(custom_css, unsafe_allow_html=True)

# --- 2. KONFIGURACJA STRONY ---
# Ustawiamy konfigurację strony na początku
st.set_page_config(page_title="System AI PRO", page_icon="✨", layout="wide")

# Stosujemy nieskończone tło
set_infinite_background()

# --- 3. STYLIZACJA INTERFEJSU (CSS) ---
# Tutaj możesz wkleić pozostały kod CSS dotyczący nagłówków, przycisków itp.
# Upewnij się, że używasz selektorów Streamlit i !important w razie potrzeby.

# Przykład:
css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');

* {
    font-family: 'Inter', sans-serif;
}

[data-testid="stHeader"], [data-testid="stFooter"] {
    display: none;
}

.block-container {
    max-width: 800px !important;
    padding-top: 10vh !important;
}

h1 {
    font-weight: 800 !important;
    font-size: 3.5rem !important;
    text-align: center;
    background: linear-gradient(135deg, #3b82f6, #8b5cf6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 1rem !important;
}

.sub-text {
    text-align: center;
    font-size: 1.15rem;
    color: #475569;
    margin-bottom: 3rem;
}
</style>
"""
st.markdown(css, unsafe_allow_html=True)

# --- 4. TREŚĆ TWOJEJ APLIKACJI ---
st.markdown("<h1>System AI</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-text'>Gotowy do implementacji nowych funkcjonalności.</p>", unsafe_allow_html=True)
