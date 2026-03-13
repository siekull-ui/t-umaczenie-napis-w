import streamlit as st

# --- 1. MINIMALISTYCZNA KONFIGURACJA ---
st.set_page_config(
    page_title="Blank Hero - Fast SPA",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. INTERFEJS (CSS + HTML + JS) ---
def apply_fast_hero_layout():
    
    css_styles = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500&display=swap');

    /* Ukrycie elementów systemowych Streamlit */
    [data-testid="stHeader"], [data-testid="stFooter"], [data-testid="stToolbar"] {
        display: none !important;
    }

    .stApp {
        background-color: #F0D3DE !important;
    }

    /* KONTENER HERO */
    #hero-canvas {
        position: fixed;
        top: 1cm; bottom: 1cm; left: 1cm; right: 1cm;
        background: rgba(255, 255, 255, 0.25);
        backdrop-filter: blur(25px) saturate(150%);
        -webkit-backdrop-filter: blur(25px) saturate(150%);
        border-radius: 1cm;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
        z-index: 1000;
        padding: 100px 50px 50px 50px; /* Miejsce na treść poniżej nawigacji */
        overflow-y: auto; /* Scrollowanie, jeśli treść jest długa */
    }

    /* --- NAWIGACJA --- */
    .hero-nav {
        position: absolute;
        top: 40px;
        right: 50px;
        display: flex;
        gap: 60px;
        align-items: center;
        font-family: 'Poppins', sans-serif;
    }

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

    /* --- TREŚĆ ZAKŁADEK --- */
    .tab-content {
        display: none; /* Domyślnie ukrywamy wszystkie sekcje */
        font-family: 'Poppins', sans-serif;
        color: #1a1a1a;
        animation: fadeIn 0.4s ease-in-out;
    }

    /* Klasa dla aktywnej sekcji */
    .tab-content.active-content {
        display: block;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* Usunięcie marginesów domyślnych Streamlit */
    .main .block-container { padding: 0 !important; }
    </style>
    """

    # Struktura HTML z osadzonym skryptem JS
    html_structure = """
    <div id="hero-canvas">
        <nav class="hero-nav">
            <a onclick="switchTab('home', this)" class="active">Home</a>
            <a onclick="switchTab('about', this)">About</a>
            <a onclick="switchTab('services', this)">Services</a>
            <a onclick="switchTab('portfolio', this)">Portfolio</a>
            <a onclick="switchTab('contact', this)">Contact</a>
        </nav>

        <div id="home" class="tab-content active-content">
            <h1>Witaj na stronie głównej 👋</h1>
            <p>To jest błyskawiczna nawigacja bez przeładowywania.</p>
        </div>
        
        <div id="about" class="tab-content">
            <h1>O nas 🚀</h1>
            <p>Tutaj znajduje się treść zakładki About. Pojawia się natychmiast po kliknięciu!</p>
        </div>

        <div id="services" class="tab-content">
            <h1>Usługi 🛠️</h1>
            <p>Nasza oferta...</p>
        </div>

        <div id="portfolio" class="tab-content">
            <h1>Portfolio 🎨</h1>
            <p>Zobacz nasze projekty.</p>
        </div>

        <div id="contact" class="tab-content">
            <h1>Kontakt 📬</h1>
            <p>Napisz do nas wiadomość.</p>
        </div>
    </div>

    <script>
    function switchTab(tabId, element) {
        // 1. Usuń klasę 'active' ze wszystkich linków
        const links = document.querySelectorAll('.hero-nav a');
        links.forEach(link => link.classList.remove('active'));
        
        // 2. Dodaj klasę 'active' do klikniętego linku (uruchamia falę)
        element.classList.add('active');

        // 3. Ukryj wszystkie sekcje z treścią
        const contents = document.querySelectorAll('.tab-content');
        contents.forEach(content => content.classList.remove('active-content'));

        // 4. Pokaż tylko wybraną sekcję
        document.getElementById(tabId).classList.add('active-content');
    }
    </script>
    """
    
    # Wstrzyknięcie całości do Streamlit
    st.components.v1.html(css_styles + html_structure, height=1000, scrolling=False)

# Wywołanie układu
apply_fast_hero_layout()
