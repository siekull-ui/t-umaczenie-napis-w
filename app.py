import streamlit as st

# Konfiguracja strony
st.set_page_config(page_title="Portfolio", page_icon="👤", layout="wide")

# Niestandardowy CSS, aby dopasować wygląd do zdjęcia
st.markdown("""
    <style>
    /* Import czcionki */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;800&display=swap');

    html, body, [class*="st-"] {
        font-family: 'Inter', sans-serif;
    }

    /* Ukrycie standardowych elementów Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Pływające Menu (Navbar) */
    .nav-container {
        display: flex;
        justify-content: center;
        padding: 20px 0;
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        background-color: rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(10px);
        z-index: 999;
    }
    .nav-box {
        background: white;
        padding: 10px 30px;
        border-radius: 50px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        display: flex;
        gap: 20px;
    }
    .nav-link {
        text-decoration: none;
        color: #000;
        font-weight: 500;
        font-size: 14px;
    }

    /* Główna sekcja tekstowa */
    .hero-container {
        text-align: center;
        margin-top: 150px;
        margin-bottom: 50px;
    }
    .hero-title {
        font-size: 64px;
        font-weight: 800;
        line-height: 1.1;
        margin-bottom: 20px;
        color: #000;
    }
    .hero-subtitle {
        font-size: 20px;
        color: #666;
        margin-bottom: 40px;
    }

    /* Stylizacja obrazu twarzy */
    .face-img {
        display: block;
        margin-left: auto;
        margin-right: auto;
        filter: grayscale(100%);
        transition: 0.3s;
    }
    .face-img:hover {
        filter: grayscale(0%);
    }
    </style>

    <div class="nav-container">
        <div class="nav-box">
            <a href="#" class="nav-link">O mnie</a>
            <a href="#" class="nav-link">Wyróżnione</a>
            <a href="#" class="nav-link">Praca</a>
            <a href="#" class="nav-link">LinkedIn</a>
            <a href="#" class="nav-link">Kontakt</a>
        </div>
    </div>

    <div class="hero-container">
        <h1 class="hero-title">Twoje Imię<br>to Student Pielęgniarstwa</h1>
        <p class="hero-subtitle">Pasjonat opieki medycznej. Mielec, Polska.</p>
    </div>
""", unsafe_allow_html=True)

# Wyświetlenie Twojego zdjęcia z repozytorium
# Streamlit automatycznie szuka pliku w tym samym folderze co app.py
try:
    st.image("jaja.png", width=500, use_container_width=False)
    # Dodatkowa stylizacja obrazu przez CSS (centrowanie pod tekstem)
    st.markdown("""
        <style>
        img {
            display: block;
            margin-left: auto;
            margin-right: auto;
            filter: grayscale(100%);
        }
        </style>
    """, unsafe_allow_html=True)
except FileNotFoundError:
    st.error("Nie znaleziono pliku jaja.png w repozytorium. Upewnij się, że nazwa jest poprawna.")
