import streamlit as st

# --- 1. MINIMALISTYCZNA KONFIGURACJA ---
st.set_page_config(
    page_title="Blank Hero",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. LOGIKA ZAKŁADEK (STAN APLIKACJI) ---
# Pobieramy aktualną zakładkę z parametrów URL (domyślnie "Home")
current_tab = st.query_params.get("tab", "Home")

# Funkcja pomocnicza do dynamicznego nadawania klasy "active"
def get_active_class(tab_name):
    return 'class="active"' if current_tab == tab_name else ""

# --- 3. KONSTRUKCJA INTERFEJSU (CSS + HTML) ---
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

    /* KONTENER HERO (Samo szklane tło) */
    #hero-canvas {
        position: fixed;
        top: 1cm;
        bottom: 1cm;
        left: 1cm;
        right: 1cm;
        
        background: rgba(255, 255, 255, 0.25);
        backdrop-filter: blur(25px) saturate(150%);
        -webkit-backdrop-filter: blur(25px) saturate(150%);
        
        border-radius: 1cm;
        border: none;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
        
        z-index: 1000;
    }

    /* --- NAWIGACJA --- */
    .hero-nav {
        position: fixed;
        top: calc(1cm + 40px); /* Dopasowane do kontenera hero */
        right: calc(1cm + 50px);
        display: flex;
        gap: 60px;
        align-items: center;
        font-family: 'Poppins', sans-serif;
        z-index: 1002; /* Musi być na samym wierzchu, by było klikalne */
    }

    .hero-nav a {
        color: #1a1a1a !important;
        text-decoration: none;
        font-size: 14px;
        font-weight: 500;
        cursor: pointer;
        position: relative;
    }

    .hero-nav a::after {
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

    .hero-nav a.active::after {
        opacity: 1;
    }

    .hero-nav .search-icon {
        margin-left: -20px;
        display: flex;
        align-items: center;
    }

    .hero-nav .search-icon svg {
        width: 18px;
        height: 18px;
        stroke: #1a1a1a;
        stroke-width: 2;
        transition: stroke 0.2s ease;
    }

    .hero-nav a.search-icon::after {
        display: none; 
    }

    .hero-nav .search-icon:hover svg {
        stroke: #FF2A5F; 
    }

    /* Zapewnienie, że natywne elementy Streamlit będą nad szkłem */
    .main .block-container {
        padding: 0 !important;
        position: relative;
        z-index: 1001 !important; 
    }
    
    /* Bezpieczny obszar na tekst pod nawigacją */
    .content-area {
        margin-top: 150px; 
        padding-left: 2.5cm;
        padding-right: 2.5cm;
        font-family: 'Poppins', sans-serif;
    }
    </style>
    """

    # Linki mają teraz href i target="_self", co wywołuje błyskawiczne odświeżenie wewnątrz Streamlit
    html_structure = f"""
    <div id="hero-canvas"></div>
    <nav class="hero-nav">
        <a href="?tab=Home" target="_self" {get_active_class("Home")}>Home</a>
        <a href="?tab=About" target="_self" {get_active_class("About")}>About</a>
        <a href="?tab=Services" target="_self" {get_active_class("Services")}>Services</a>
        <a href="?tab=Portfolio" target="_self" {get_active_class("Portfolio")}>Portfolio</a>
        <a href="?tab=Contact" target="_self" {get_active_class("Contact")}>Contact</a>
        <a class="search-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round">
                <circle cx="11" cy="11" r="8"></circle>
                <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
            </svg>
        </a>
    </nav>
    """

    st.markdown(css_styles + html_structure, unsafe_allow_html=True)

# Uruchamiamy stylizację
apply_hero_layout()


# --- 4. WYŚWIETLANIE TREŚCI W ZALEŻNOŚCI OD ZAKŁADKI ---
# Otwieramy dedykowany kontener, żeby tekst ładnie układał się pod nawigacją
st.markdown("<div class='content-area'>", unsafe_allow_html=True)

if current_tab == "Home":
    st.title("Witaj w Blank Hero")
    st.write("Wybierz zakładkę z menu powyżej, aby nawigować po stronie.")
    
elif current_tab == "About":
    st.title("O mnie")
    st.write("Student pielęgniarstwa (rocznik 2025). Tutaj gromadzę materiały z zajęć, notatki kliniczne i projekty medyczne.")
    
elif current_tab == "Services":
    st.title("Usługi")
    st.write("Miejsce na listę usług lub specjalizacji.")
    
elif current_tab == "Portfolio":
    st.title("Portfolio")
    st.write("Galeria projektów i certyfikatów.")
    
elif current_tab == "Contact":
    st.title("Kontakt")
    st.text_input("Zostaw wiadomość:", placeholder="Napisz do mnie...")
    st.button("Wyślij")

st.markdown("</div>", unsafe_allow_html=True)
