import streamlit as st
import base64
import os

# 1. Konfiguracja strony
st.set_page_config(page_title="Dawid | Portfolio", layout="wide")

# 2. Funkcja do bezpiecznego wczytywania obrazka (omija błędy PIL)
def get_image_base64(path):
    if os.path.exists(path):
        try:
            with open(path, "rb") as f:
                data = f.read()
                return base64.b64encode(data).decode()
        except Exception:
            return None
    return None

img_data = get_image_base64("jaja.png")

# 3. CSS - Stylizacja: Białe tło, Glassmorphism, Zaokrąglenia
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');

    /* Reset i tło strony */
    .stApp {{
        background-color: #FFFFFF;
        font-family: 'Inter', sans-serif;
    }}

    /* Ukrycie dekoracji Streamlit */
    header, footer, #MainMenu {{visibility: hidden;}}

    /* Pasek nawigacji - Glassmorphism */
    .nav-container {{
        position: fixed;
        top: 20px;
        width: 100%;
        display: flex;
        justify-content: center;
        z-index: 1000;
    }}
    .nav-bar {{
        background: rgba(255, 255, 255, 0.6);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(0, 0, 0, 0.05);
        border-radius: 100px;
        padding: 10px 25px;
        display: flex;
        gap: 20px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.03);
    }}
    .nav-bar a {{
        text-decoration: none;
        color: #000;
        font-weight: 500;
        font-size: 14px;
        transition: 0.3s;
    }}
    .nav-bar a:hover {{ opacity: 0.6; }}

    /* GŁÓWNY KONTENER (Biała karta) */
    .hero-card {{
        background: #FFFFFF;
        max-width: 900px;
        margin: 100px auto 0 auto;
        border-radius: 50px;
        border: 1px solid #F0F0F0;
        box-shadow: 0 30px 60px rgba(0,0,0,0.05);
        overflow: hidden; /* To sprawi, że zdjęcie na dole będzie przycięte do zaokrągleń karty */
        display: flex;
        flex-direction: column;
        align-items: center;
        position: relative;
    }}

    .hero-text {{
        color: #000000;
        font-size: clamp(32px, 5vw, 64px);
        font-weight: 900;
        text-align: center;
        margin-top: 60px;
        margin-bottom: 40px;
        letter-spacing: -2px;
    }}

    /* Kontener na twarz - przyklejony do dołu */
    .face-container {{
        width: 100%;
        display: flex;
        justify-content: center;
        align-items: flex-end; /* Zdjęcie dotyka dołu */
        margin-top: auto;
    }}

    .face-img {{
        width: 450px; /* Rozmiar Twojej twarzy */
        display: block;
        filter: grayscale(100%);
        transition: filter 0.5s ease;
        margin-bottom: -5px; /* Lekkie przesunięcie, by idealnie siadło na ramce */
    }}
    
    .hero-card:hover .face-img {{
        filter: grayscale(0%);
    }}

    </style>

    <div class="nav-container">
        <div class="nav-bar">
            <a href="#">O mnie</a>
            <a href="#">Projekty</a>
            <a href="#">Kontakt</a>
        </div>
    </div>

    <div class="hero-card">
        <h1 class="hero-text">Cześć, jestem Dawid!</h1>
        <div class="face-container">
            {"<img src='data:image/png;base64," + img_data + "' class='face-img'>" if img_data else "<div style='padding:100px; color:red;'>Błąd pliku jaja.png. Wrzuć go ponownie na GitHub!</div>"}
        </div>
    </div>

    <p style="text-align: center; color: #888; margin-top: 30px; font-weight: 500;">
        Student Pielęgniarstwa • Pasjonat Medycyny
    </p>
""", unsafe_allow_html=True)
