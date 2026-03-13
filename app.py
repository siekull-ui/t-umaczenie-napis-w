import streamlit as st

# --- 1. MINIMALISTYCZNA KONFIGURACJA ---
st.set_page_config(
    page_title="Blank Hero - Perfect Styling",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. KONSTRUKCJA INTERFEJSU (Trik CSS) ---
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

    /* KONTENER HERO - Wraca do oryginalnych wymiarów */
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
        overflow-y: auto;
        padding: 100px 50px; /* Margines wewnętrzny dla treści */
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

    /* Zmiana 'a' na 'label', żeby współpracowały z radio buttonami */
    .hero-nav label {
        color: #1a1a1a;
        text-decoration: none;
        font-size: 14px;
        font-weight: 500;
        cursor: pointer;
        position: relative;
        transition: color 0.3s ease;
    }

    .hero-nav label:hover {
        color: #FF2A5F;
    }

    /* FALA - Domyślnie ukryta */
    .hero-nav label::after {
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

    /* Ikonka lupki */
    .search-icon {
        margin-left: -20px;
        display: flex;
        align-items: center;
        cursor: pointer;
    }
    .search-icon svg {
        width: 18px;
        height: 18px;
        stroke: #1a1a1a;
        stroke-width: 2;
        transition: stroke 0.2s ease;
    }
    .search-icon:hover svg { stroke: #FF2A5F; }
    .search-icon::after { display: none !important; }

    /* UKRYWAMY RADIO BUTTONY */
    input[name="hero-tabs"] {
        display: none;
    }

    /* POKAZYWANIE FALI DLA AKTYWNEJ ZAKŁADKI (Magia CSS) */
    #tab-home:checked ~ .hero-nav label[for="tab-home"]::after,
    #tab-about:checked ~ .hero-nav label[for="tab-about"]::after,
    #tab-services:checked ~ .hero-nav label[for="tab-services"]::after,
    #tab-portfolio:checked ~ .hero-nav label[for="tab-portfolio"]::after,
    #tab-contact:checked ~ .hero-nav label[for="tab-contact"]::after {
        opacity: 1;
    }

    /* --- KONTENERY Z TREŚCIĄ --- */
    .tab-content {
        display: none;
        font-family: 'Poppins', sans-serif;
        color: #1a1a1a;
        animation: fadeIn 0.4s ease-in-out;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* POKAZYWANIE TREŚCI ZALEŻNIE OD WYBRANEGO RADIO BUTTONA */
    #tab-home:checked ~ #content-home,
    #tab-about:checked ~ #content-about,
    #tab-services:checked ~ #content-services,
    #tab-portfolio:checked ~ #content-portfolio,
    #tab-contact:checked ~ #content-contact {
        display: block;
    }

    .main .block-container { padding: 0 !important; }
    </style>
    """

    # Struktura HTML wykorzystująca radio-buttony i etykiety
    html_structure = """
    <div id="hero-canvas">
        <input type="radio" id="tab-home" name="hero-tabs" checked>
        <input type="radio" id="tab-about" name="hero-tabs">
        <input type="radio" id="tab-services" name="hero-tabs">
        <input type="radio" id="tab-portfolio" name="hero-tabs">
        <input type="radio" id="tab-contact" name="hero-tabs">

        <nav class="hero-nav">
            <label for="tab-home">Home</label>
            <label for="tab-about">About</label>
            <label for="tab-services">Services</label>
            <label for="tab-portfolio">Portfolio</label>
            <label for="tab-contact">Contact</label>
            
            <div class="search-icon">
                <svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round">
                    <circle cx="11" cy="11" r="8"></circle>
                    <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                </svg>
            </div>
        </nav>

        <div id="content-home" class="tab-content">
            <h1>Cześć! 👋</h1>
            <p>To jest Home. Design uratowany, a strona ani drgnie przy przełączaniu.</p>
        </div>
        
        <div id="content-about" class="tab-content">
            <h1>O mnie</h1>
            <p>Tutaj wrzucisz informacje o sobie.</p>
        </div>

        <div id="content-services" class="tab-content">
            <h1>Usługi</h1>
            <p>Co oferujesz światu.</p>
        </div>

        <div id="content-portfolio" class="tab-content">
            <h1>Portfolio</h1>
            <p>Twoje najlepsze projekty.</p>
        </div>

        <div id="content-contact" class="tab-content">
            <h1>Kontakt</h1>
            <p>Zadzwoń do mnie.</p>
        </div>
    </div>
    """
    
    # Wracamy do st.markdown, co chroni cały układ
    st.markdown(css_styles + html_structure, unsafe_allow_html=True)

# Wywołanie układu
apply_hero_layout()
