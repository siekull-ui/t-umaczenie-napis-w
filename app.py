import streamlit as st
import base64
import os

# Konfiguracja
st.set_page_config(page_title="Dawid - Portfolio", layout="wide")

# Funkcja do zamiany obrazka na format czytelny dla HTML (zapobiega błędom PIL)
def get_image_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return None

img_base64 = get_image_base64("jaja.png")

# CSS dla layoutu
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');

    html, body, [class*="st-"] {{
        font-family: 'Inter', sans-serif;
        background-color: #F0F2F5; /* Lekko szare tło strony, by biały kontener się wyróżniał */
    }}

    /* Ukrycie elementów Streamlit */
    #MainMenu, footer, header {{visibility: hidden;}}

    /* GŁÓWNY KONTENER - Dostosowuje się do szerokości, białe tło, glassmorphism */
    .hero-wrapper {{
        width: 100%;
        background: white;
        border-radius: 40px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.05);
        margin-top: 50px;
        display: flex;
        flex-direction: column;
        align-items: center;
        overflow: hidden; /* Obcina obrazek na dole, jeśli trzeba */
        border: 1px solid rgba(0,0,0,0.05);
        position: relative;
    }}

    /* Tekst nad głową */
    .hero-text {{
        font-size: 52px;
        font-weight: 900;
        color: black;
        margin-top: 60px;
        margin-bottom: 20px;
        text-align: center;
        letter-spacing: -2px;
    }}

    /* Kontener na zdjęcie, który przykleja je do dołu */
    .image-container {{
        display: flex;
        justify-content: center;
        align-items: flex-end; /* Przyklejenie do dolnej krawędzi */
        width: 100%;
        height: auto;
    }}

    .face-img {{
        width: 400px; /* Stała szerokość twarzy */
        display: block;
        margin: 0 auto;
        filter: grayscale(100%);
        /* Brak marginesu na dole, żeby dotykało ramki */
        margin-bottom: 0px; 
    }}

    /* Szklane menu */
    .nav-bar {{
        display: flex;
        justify-content: center;
        gap: 30px;
        padding: 15px 40px;
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(15px);
        border-radius: 100px;
        position: fixed;
        top: 20px;
        left: 50%;
        transform: translateX(-50%);
        z-index: 999;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
        border: 1px solid rgba(255,255,255,0.3);
    }}
    
    .nav-bar a {{
        text-decoration: none;
        color: black;
        font-weight: 600;
        font-size: 14px;
    }}
    </style>

    <div class="nav-bar">
        <a href="#">Start</a>
        <a href="#">O mnie</a>
        <a href="#">Kontakt</a>
    </div>

    <div class="hero-wrapper">
        <h1 class="hero-text">Cześć, jestem Dawid!</h1>
        <div class="image-container">
            {"<img src='data:image/png;base64," + img_base64 + "' class='face-img'>" if img_base64 else "<p style='padding: 50px;'>Wgraj jaja.png do repozytorium!</p>"}
        </div>
    </div>

    <div style="text-align: center; margin-top: 40px; color: #888; font-size: 18px; font-weight: 500;">
        Student Pielęgniarstwa • Pasjonat Medycyny
    </div>
""", unsafe_allow_html=True)
