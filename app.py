import streamlit as st

# --- 1. MINIMALISTYCZNA KONFIGURACJA ---
st.set_page_config(
    page_title="Blank Hero",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. KONSTRUKCJA INTERFEJSU (CSS HACKS) ---
def apply_hero_layout():
    css_styles = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500&display=swap');

    /* Ukrycie elementów systemowych Streamlit */
    [data-testid="stHeader"], [data-testid="stFooter"], [data-testid="stToolbar"] {
        display: none !important;
    }

    /* Tło aplikacji */
    .stApp {
        background-color: #F0D3DE !important;
    }

    /* KONTENER HERO - Przerabiamy domyślny obszar roboczy Streamlita na "szkło" */
    .main .block-container {
        margin: 1cm auto !important;
        max-width: calc(100vw - 2cm) !important;
        height: calc(100vh - 2cm) !important;
        padding: 120px 50px 50px 50px !important; /* Margines na górze, by zrobić miejsce na nawigację */
        
        background: rgba(255, 255, 255, 0.25);
        backdrop-filter: blur(25px) saturate(150%);
        -webkit-backdrop-filter: blur(25px) saturate(150%);
        
        border-radius: 1cm;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
        overflow-y: auto;
    }

    /* --- NAWIGACJA (HACKOWANIE st.radio) --- */
    
    /* Pozycjonowanie całego paska radio w prawym górnym rogu */
    div[data-testid="stRadio"] {
        position: absolute;
        top: 40px;
        right: 120px; /* Zostawiamy miejsce na lupkę */
        z-index: 1001;
    }
    
    /* Układ flexbox - identyczny z Twoim .hero-nav */
    div[data-testid="stRadio"] > div[role="radiogroup"] {
        display: flex;
        flex-direction: row;
        gap: 60px;
        align-items: center;
        background: transparent;
    }

    /* Ukrycie systemowych kółek (radio buttons) */
    div[data-testid="stRadio"] label > div:first-child {
        display: none !important;
    }

    /* Wygląd pojedynczego linku (etykiety) */
    div[data-testid="stRadio"] label {
        color: #1a1a1a !important;
        font-family: 'Poppins', sans-serif !important;
        cursor: pointer;
        position: relative;
        padding: 0;
        background: transparent !important;
    }

    div[data-testid="stRadio"] label p {
        font-size: 14px !important;
        font-weight: 500 !important;
        margin: 0;
    }

    /* FALA - dodana pod każdą etykietę, domyślnie niewidoczna */
    div[data-testid="stRadio"] label::after {
        content: '';
        position: absolute;
        bottom: -10px;
        left: -15px;
        right: -15px;
        height: 6px;
        background-image: url("data:image/svg+xml,%3Csvg width='30' height='6' viewBox='0 0 30 6' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M0 3C5 1 10 1 15 3C20 5 25 5 30 3' stroke='%23FF2A5F' stroke-width='1.5' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E");
        background-repeat: repeat-x;
        opacity: 0;
        transition: opacity 0.3s ease;
    }

    /* AKTYWNA FALA - [data-checked="true"] to natywny atrybut Streamlita dla wybranej opcji */
    div[data-testid="stRadio"] label[data-checked="true"]::after {
        opacity: 1;
    }

    /* --- IKONA LUPKI (Dodana jako HTML obok nawigacji) --- */
    .search-icon-wrapper {
        position: absolute;
        top: 40px;
        right: 60px;
        z-index: 1001;
        display: flex;
        align-items: center;
        cursor: pointer;
    }

    .search-icon-wrapper svg {
        width: 18px;
        height: 18px;
        stroke: #1a1a1a;
        stroke-width: 2;
        transition: stroke 0.2s ease;
    }

    .search-icon-wrapper:hover svg {
        stroke: #FF2A5F; 
    }
    </style>

    <div class="search-icon-wrapper">
        <svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="11" cy="11" r="8"></circle>
            <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
        </svg>
    </div>
    """
    st.markdown(css_styles, unsafe_allow_html=True)

# Wywołanie styli
apply_hero_layout()

# --- 3. LOGIKA NAWIGACJI ---
tabs = ["Home", "About", "Services", "Portfolio", "Contact"]

# Ukrywamy nagłówek (label_visibility="collapsed") i robimy układ poziomy. 
# Dzięki CSS powyżej, ten widżet st staje się Twoim menu!
selected_tab = st.radio("Nawigacja", tabs, horizontal=True, label_visibility="collapsed")

# --- 4. ZAWWARTOŚĆ ZAKŁADEK ---
st.markdown(f"<h1 style='font-family: Poppins; color: #1a1a1a;'>Zakładka: {selected_tab}</h1>", unsafe_allow_html=True)

if selected_tab == "Home":
    st.write("Witaj na stronie głównej! Przeklikaj zakładki na górze.")
    st.write("Zauważ, że przejścia są natychmiastowe i **nie wywołują migania (przeładowywania) całej przeglądarki**.")
    
elif selected_tab == "About":
    st.write("Tutaj wyświetla się zawartość 'About'.")
    st.info("Ponieważ używamy domyślnego kontenera Streamlita, możemy tu normalnie wrzucać widżety.")
    
elif selected_tab == "Services":
    st.write("Twoje usługi.")
    st.slider("Wybierz poziom zadowolenia z tego rozwiązania", 1, 10, 10)
    
elif selected_tab == "Portfolio":
    st.write("Portfolio projektów.")
    
elif selected_tab == "Contact":
    st.write("Skontaktuj się ze mną.")
    st.text_input("Twój email:")
    st.button("Wyślij")
