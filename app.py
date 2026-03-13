# --- 1. MINIMALISTYCZNA KONFIGURACJA ---

st.set_page_config(

    page_title="Blank Hero",

    layout="wide",

    initial_sidebar_state="collapsed"

)



# --- 2. KONSTRUKCJA INTERFEJSU (CSS + HTML) ---

def apply_hero_layout():

    st.markdown("""

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



        /* KONTENER HERO */

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

            /* Usunięto transition dla koloru, jeśli nie ma efektu hover na tekście */

        }



        /* FALA - przygotowana tylko pod aktywne kliknięcie */

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



        /* TYLKO AKTYWNA ZAKŁADKA MA FALĘ (usunięto a:hover::after) */

        .hero-nav a.active::after {

            opacity: 1;

        }



        /* Ikonka lupki */

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



        /* Lupka nadal reaguje na najechane - opcjonalne, dla UX */

        .hero-nav .search-icon:hover svg {

            stroke: #FF2A5F; 

        }



        /* Usunięcie marginesów domyślnych Streamlit */

        .main .block-container {

            padding: 0 !important;

        }

        </style>



        <div id="hero-canvas">

            <nav class="hero-nav">

                <a class="active">Home</a>

                <a>About</a>

                <a>Services</a>

                <a>Portfolio</a>

                <a>Contact</a>

                <a class="search-icon">

                    <svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round">

                        <circle cx="11" cy="11" r="8"></circle>

                        <line x1="21" y1="21" x2="16.65" y2="16.65"></line>

                    </svg>

                </a>

            </nav>

        </div>

    """, unsafe_allow_html=True)



# Wywołanie układu

apply_hero_layout()
