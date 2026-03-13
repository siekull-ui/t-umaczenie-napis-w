import streamlit as st
import base64

# --- 1. FUNKCJE DOTYCZĄCE TŁA ---
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    try:
        bin_str = get_base64_of_bin_file(png_file)
        page_bg_img = f'''
        <style>
        @keyframes panBackground {{
            0% {{ background-position: 0% 0%; background-size: 110%; }}
            50% {{ background-position: 100% 100%; background-size: 130%; }}
            100% {{ background-position: 0% 0%; background-size: 110%; }}
        }}
        
        .stApp {{
            background-image: url("data:image/png;base64,{bin_str}");
            background-repeat: no-repeat;
            background-attachment: fixed;
            animation: panBackground 60s infinite alternate ease-in-out;
        }}

        /* Efekt szklanej tafli na całą aplikację */
        [data-testid="stAppViewContainer"] {{
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(25px);
            -webkit-backdrop-filter: blur(25px);
        }}
        </style>
        '''
        st.markdown(page_bg_img, unsafe_allow_html=True)
    except FileNotFoundError:
        st.error("Nie znaleziono pliku 'background.jpg'.")

# --- 2. KONFIGURACJA STRONY ---
st.set_page_config(page_title="AI App Template", page_icon="✨", layout="wide")
set_background('background.jpg')

# --- 3. STYLIZACJA INTERFEJSU (CSS) ---
css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');

* {
    font-family: 'Inter', sans-serif;
}

/* Ukrycie standardowych elementów Streamlit */
[data-testid="stHeader"], [data-testid="stFooter"] {
    display: none;
}

.block-container {
    max-width: 800px !important;
    padding-top: 10vh !important;
}

h1 {
    font-weight: 800 !important;
    font-size: 3.5rem !important;
    text-align: center;
    background: linear-gradient(135deg, #3b82f6, #8b5cf6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 1rem !important;
}

.sub-text {
    text-align: center;
    font-size: 1.15rem;
    color: #475569;
    margin-bottom: 3rem;
}
</style>
"""
st.markdown(css, unsafe_allow_html=True)

# --- 4. MIEJSCE NA TWOJE NOWE FUNKCJE ---
st.markdown("<h1>System AI</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-text'>Gotowy do implementacji nowych funkcjonalności.</p>", unsafe_allow_html=True)
