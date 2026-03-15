import streamlit as st

# --- 1. KONFIGURACJA ---
st.set_page_config(
    page_title="Blank Hero",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. STYLE CSS (Wstrzyknięte raz) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500&display=swap');

    /* Ukrycie śmieci */
    [data-testid="stHeader"], [data-testid="stFooter"], [data-testid="stToolbar"] {
        display: none !important;
    }

    .stApp {
        background-color: #F0D3DE !important;
    }

    /* Główny kontener (Canvas) */
    .hero-container {
        position: fixed;
        top: 1cm; bottom: 1cm; left: 1cm; right: 1cm;
        background: rgba(255, 255, 255, 0.25);
        backdrop-filter: blur(25px) saturate(150%);
        border-radius: 1cm;
        padding: 40px;
        z-index: 0;
        overflow-y: auto;
    }

    /* Stylizacja przycisków Streamlit, aby wyglądały jak Twoje linki */
    div.stButton > button {
        background: none !important;
        border: none !important;
        color: #1a1a1a !important;
        font-family: 'Poppins', sans-serif !important;
        font-size: 14px !important;
        font-weight: 500 !important;
        padding: 0 !important;
        transition: all 0.3s ease;
    }

    /* Efekt fali dla "aktywnego" stanu (symulowany przez st.session_state) */
    .active-tab {
        border-bottom: 3px solid #FF2A5F !important;
        padding-bottom: 5px !important;
    }
    
    /* Pozycjonowanie nawigacji wewnątrz kontenera */
    .nav-wrapper {
        position: absolute;
        top: 40px;
        right: 50px;
        display: flex;
        gap: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. LOGIKA NAWIGACJI ---
if 'active_tab' not in st.session_state:
    st.session_state.active_tab = "Home"

def set_tab(name):
    st.session_state.active_tab = name

# --- 4. RENDEROWANIE INTERFEJSU ---

# Otwieramy główny kontener wizualny
st.markdown('<div class="hero-container">', unsafe_allow_html=True)

# Tworzymy nawigację używając kolumn Streamlit
cols = st.columns([5, 1, 1, 1, 1, 1, 0.5]) # Proporcje dla menu

tabs = ["Home", "About", "Services", "Portfolio", "Contact"]

with st.container():
    # Pusta kolumna 0 dla zrobienia miejsca po lewej
    for i, tab in enumerate(tabs):
        with cols[i+1]:
            # Sprawdzamy czy to ta zakładka jest aktywna
            is_active = "active-tab" if st.session_state.active_tab == tab else ""
            if st.button(tab, key=tab, on_click=set_tab, args=(tab,)):
                pass # on_click załatwia sprawę
            
            # Wstrzykujemy małą linię (falę) pod aktywnym przyciskiem
            if st.session_state.active_tab == tab:
                st.markdown(f'<div style="height:2px; background:#FF2A5F; width:20px; margin-top:-10px;"></div>', unsafe_allow_html=True)

# --- 5. TREŚĆ ZAKŁADEK ---
st.markdown("---") # Separator wizualny (opcjonalnie)

if st.session_state.active_tab == "Home":
    st.title("Witaj w Home")
    st.write("To jest zawartość dynamiczna bez przeładowania strony.")

elif st.session_state.active_tab == "About":
    st.title("O nas")
    st.write("Jesteśmy zespołem pasjonatów designu.")

elif st.session_state.active_tab == "Services":
    st.title("Nasze Usługi")
    st.info("Oferujemy projektowanie UI/UX i development.")

# Zamykamy kontener wizualny
st.markdown('</div>', unsafe_allow_html=True)
