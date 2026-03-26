import streamlit as st

# Konfiguracja strony
st.set_page_config(
    page_title="Portfolio Student Pielęgniarstwa",
    page_icon="👤",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Niestandardowy CSS dla efektu Glassmorphism i wyśrodkowania
# Tutaj dzieje się cała magia stylizacji
st.markdown("""
    <style>
    /* Import czcionki Inter dla nowoczesnego wyglądu */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');

    html, body, [class*="st-"] {
        font-family: 'Inter', sans-serif;
        background-color: #FFFFFF; /* Czyste białe tło */
        color: #000000; /* Czarne napisy */
    }

    /* Ukrycie standardowych elementów interfejsu Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp { background-color: white; } /* Wymuszenie białego tła aplikacji */

    /* Główny kontener - środkowanie wszystkiego */
    .main-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        min-height: 100vh;
        padding: 50px 20px;
    }

    /* Pływające Menu (Navbar) - Glassmorphism */
    .nav-box {
        position: fixed;
        top: 20px;
        background: rgba(255, 255, 255, 0.4); /* Półprzezroczyste białe tło */
        border-radius: 50px;
        padding: 12px 30px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.1); /* Lekki cień */
        backdrop-filter: blur(10px); /* Rozmycie tła - efekt szkła */
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.18);
        display: flex;
        gap: 25px;
        z-index: 1000;
        max-width: 90%;
    }
    .nav-link {
        text-decoration: none;
        color: #000000; /* Czarne linki */
        font-weight: 500;
        font-size: 14px;
        white-space: nowrap;
    }

    /* Sekcja tekstowa */
    .hero-title {
        font-size: 60px;
        font-weight: 800;
        line-height: 1.1;
        margin-top: 100px;
        margin-bottom: 20px;
        color: #000000; /* Czarne napisy */
    }
    .hero-subtitle {
        font-size: 20px;
        color: #333333; /* Ciemnoszare napisy */
        margin-bottom: 50px;
    }

    /* Stylizacja obrazu twarzy w kontenerze Glassmorphism */
    .face-image-container {
        background: rgba(255, 255, 255, 0.3); /* Jeszcze bardziej przezroczyste */
        border-radius: 40px;
        padding: 20px;
        box-shadow: 0 15px 45px rgba(0, 0, 0, 0.15); /* Mocniejszy cień dla głębi */
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        display: inline-block; /* Aby kontener pasował do obrazu */
    }
    .face-img {
        border-radius: 30px; /* Zaokrąglone rogi samego zdjęcia */
        filter: grayscale(100%); /* Zdjęcie czarno-białe */
        display: block;
    }
    </style>

    <div style="display: flex; justify-content: center; width: 100%;">
        <div class="nav-box">
            <a href="#" class="nav-link">Profil</a>
            <a href="#" class="nav-link">Edukacja</a>
            <a href="#" class="nav-link">Praktyki</a>
            <a href="https://pl.linkedin.com/" class="nav-link" target="_blank">LinkedIn</a>
            <a href="#" class="nav-link">Kontakt</a>
        </div>
    </div>

    <div class="main-container">
        <h1 class="hero-title">Twoje Imię to<br>Student Pielęgniarstwa</h1>
        <p class="hero-subtitle">Pasjonat opieki medycznej. Mielec, Polska.</p>
    </div>
""", unsafe_allow_html=True)

# Wyświetlenie zdjęcia twarzy
# Używamy st.image z niestandardowym HTMLem, aby zastosować style Glassmorphism
try:
    # Wczytujemy zdjęcie przez Streamlit, żeby upewnić się, że istnieje
    st.image("jaja.png", width=400)
    
    # Nakładamy style na renderowany element img
    st.markdown("""
        <style>
        div.stImage > img {
            display: block;
            margin-left: auto;
            margin-right: auto;
            border-radius: 30px;
            filter: grayscale(100%);
            box-shadow: 0 15px 45px rgba(0, 0, 0, 0.15);
            background: rgba(255, 255, 255, 0.3);
            padding: 20px;
            border: 1px solid rgba(255, 255, 255, 0.2);
            backdrop-filter: blur(15px);
        }
        /* Kontener obrazu środkuje go w układzie wide */
        div.stImage {
            text-align: center;
        }
        </style>
    """, unsafe_allow_html=True)

except FileNotFoundError:
    st.error("Nie znaleziono pliku jaja.png w repozytorium. Upewnij się, że nazwa jest poprawna.")

# Opcjonalnie: Czysty stopka community
st.markdown("""
    <div style="text-align: center; color: #999; padding: 20px; font-size: 12px; margin-top: auto;">
        Streamlit Community | Mielec, Poland
    </div>
""", unsafe_allow_html=True)
