import streamlit as st

# --- 1. KONFIGURACJA ---
st.set_page_config(
    page_title="Blank Hero Navigation",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Pobieramy aktualną zakładkę z URL (domyślnie 'Home')
query_params = st.query_params
active_tab = query_params.get("tab", "Home")

# --- 2. STYLIZACJA I STRUKTURA ---
def apply_hero_layout(current_tab):
    # Generujemy dynamicznie klasy 'active' dla linków
    def is_active(name):
        return "active" if current_tab == name else ""

    css_styles = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500&display=swap');

    [data-testid="stHeader"], [data-testid="stFooter"], [data-testid="stToolbar"] {
        display: none !important;
    }

    .stApp {
        background-color: #F0D3DE !important;
    }

    #hero-canvas {
        position: fixed;
        top: 1cm; bottom: 1cm; left: 1cm; right: 1cm;
        background: rgba(255, 255, 255, 0.25);
        backdrop-filter: blur(25px) saturate(150%);
        -webkit-backdrop-filter: blur(25px) saturate(150%);
        border-radius: 1cm;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
        z-index: 1000;
        padding: 80px 50px; /* Miejsce na treść poniżej navi */
        overflow: hidden;
    }

    .hero-nav {
        position: absolute;
        top: 40px;
        right: 50px;
        display: flex;
        gap: 60px;
        align-items: center;
        font-family: 'Poppins', sans-serif;
    }

    /* Linki jako nawigacja - używamy tagu 'a', ale z parametrem query */
    .hero-nav a {
        color: #1a1a1a !important;
        text-decoration: none;
        font-size: 14px;
        font-weight: 500;
        cursor: pointer;
        position: relative;
        transition: color 0.3s ease;
    }

    .hero-nav a:hover {
        color: #FF2A5F !important;
    }

    /* FALA */
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

    /* Treść zakładki */
    .content-area {
        font-family: 'Poppins', sans-serif;
        color: #1a1a1a;
        margin-top: 60px;
        animation: fadeIn 0.5s ease;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .main .block-container { padding: 0 !important; }
    </style>
    """

    # HTML z linkami aktualizującymi URL (?tab=Nazwa)
    html_structure = f"""
    <div id="hero-canvas">
        <nav class="hero-nav">
            <a href="/?tab=Home" target="_self" class="{is_active('Home')}">Home</a>
            <a href="/?tab=About" target="_self" class="{is_active('About')}">About</a>
            <a href="/?tab=Services" target="_self" class="{is_active('Services')}">Services</a>
            <a href="/?tab=Portfolio" target="_self" class="{is_active('Portfolio')}">Portfolio</a>
            <a href="/?tab=Contact" target="_self" class="{is_active('Contact')}">Contact</a>
        </nav>
        <div class="content-area">
            <h1>{current_tab}</h1>
            <p>To jest zawartość zakładki: <strong>{current_tab}</strong></p>
        </div>
    </div>
    """
    
    st.markdown(css_styles + html_structure, unsafe_allow_html=True)

# --- 3. WYŚWIETLANIE ---
apply_hero_layout(active_tab)

# Opcjonalnie: Możesz tu dodać standardowe widgety Streamlit, 
# ale będą one "pod" Twoim overlayem, chyba że dostosujesz z-index.
