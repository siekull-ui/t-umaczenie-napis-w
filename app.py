import streamlit as st
import base64
import os

# 1. Konfiguracja na pełną szerokość
st.set_page_config(page_title="Dawid | Portfolio", layout="wide", initial_sidebar_state="collapsed")

def get_image_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return None

img_data = get_image_base64("jaja.png")

# 2. Stylizacja: Full-width, Deep Black, Glassmorphism
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');

    /* Globalne ustawienia */
    .stApp {{
        background-color: #ffffff;
        font-family: 'Inter', sans-serif;
    }}

    header, footer, #MainMenu {{visibility: hidden;}}

    /* Nawigacja - Bardziej "szklana" */
    .nav-container {{
        position: fixed;
        top: 30px;
        width: 100%;
        display: flex;
        justify-content: center;
        z-index: 1000;
    }}
    .nav-bar {{
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(20px) saturate(180%);
        -webkit-backdrop-filter: blur(20px) saturate(180%);
        border: 1px solid rgba(0, 0, 0, 0.08);
        border-radius: 100px;
        padding: 12px 40px;
        display: flex;
        gap: 30px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.03);
    }}
    .nav-bar a {{
        text-decoration: none;
        color: #000000 !important;
        font-weight: 600;
        font-size: 15px;
        letter-spacing: -0.3px;
    }}

    /* GŁÓWNY KONTENER - Teraz szeroki i dopracowany */
    .hero-section {{
        display: flex;
        justify-content: center;
        padding: 0 20px;
        margin-top: 120px;
    }}

    .hero-card {{
        background: #ffffff;
        width: 100%;
        max-width: 1200px; /* Rozciągnięty kontener */
        height: 700px; /* Stała wysokość dla balansu */
        border-radius: 60px;
        border: 1px solid #f0f0f0;
        box-shadow: 0 40px 100px rgba(0,0,0,0.07);
        display: flex;
        flex-direction: column;
        align-items: center;
        overflow: hidden;
        position: relative;
        transition: transform 0.4s ease;
    }}

    /* Tekst - Duży, czarny, konkretny */
    .hero-text {{
        color: #000000 !important;
        font-size: clamp(40px, 8vw, 90px);
        font-weight: 900;
        text-align: center;
        margin-top: 80px;
        line-height: 0.95;
        letter-spacing: -4px;
        z-index: 2;
    }}

    .hero-sub {{
        color: #000000;
        font-size: 20px;
        font-weight: 400;
        margin-top: 20px;
        opacity: 0.6;
        z-index: 2;
    }}

    /* Zdjęcie twarzy - Idealnie na dolnej ramce */
    .face-wrapper {{
        position: absolute;
        bottom: 0;
        width: 100%;
        display: flex;
        justify-content: center;
        align-items: flex-end;
    }}

    .face-img {{
        width: 500px; /* Rozmiar dopasowany do szerokiej karty */
        height: auto;
        display: block;
        filter: grayscale(100%);
        transition: all 0.6s cubic-bezier(0.16, 1, 0.3, 1);
        transform: translateY(10px); /* Delikatne wpuszczenie w dół */
    }}
    
    .hero-card:hover .face-img {{
        filter: grayscale(0%);
        transform: translateY(0) scale(1.02);
    }}

    /* Dodatkowy element dekoracyjny - lekkie zaokrąglone obramowanie wewnątrz */
    .hero-card::after {{
        content: "";
        position: absolute;
        inset: 0;
        border-radius: 60px;
        border: 1px solid rgba(0,0,0,0.03);
        pointer-events: none;
    }}
    </style>

    <div class="nav-container">
        <div class="nav-bar">
            <a href="#">Home</a>
            <a href="#">O mnie</a>
            <a href="#">Edukacja</a>
            <a href="#">Kontakt</a>
        </div>
    </div>

    <section class="hero-section">
        <div class="hero-card">
            <h1 class="hero-text">Cześć, jestem Dawid!</h1>
            <p class="hero-sub">Student Pielęgniarstwa • Mielec, Polska</p>
            
            <div class="face-wrapper">
                {"<img src='data:image/png;base64," + img_data + "' class='face-img'>" if img_data else "<div style='padding-bottom:100px; color:#ccc;'>Wgraj jaja.png, żeby zobaczyć magię</div>"}
            </div>
        </div>
    </section>

    <div style="height: 100px;"></div> """, unsafe_allow_html=True)
