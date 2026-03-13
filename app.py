import streamlit as st
import deepl
import tempfile
import os
import base64

# --- FUNKCJA DO WCZYTANIA I ANIMACJI TŁA ---
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    try:
        bin_str = get_base64_of_bin_file(png_file)
        # Dodajemy animację 'panBackground', która płynnie przesuwa powiększone tło
        page_bg_img = f'''
        <style>
        @keyframes panBackground {{
            0% {{ background-position: 0% 0%; background-size: 110%; }}
            50% {{ background-position: 100% 100%; background-size: 120%; }}
            100% {{ background-position: 0% 0%; background-size: 110%; }}
        }}
        
        .stApp {{
            background-image: url("data:image/png;base64,{bin_str}");
            background-repeat: no-repeat;
            background-attachment: fixed;
            /* Uruchomienie animacji: 60 sekund, w kółko, płynnie */
            animation: panBackground 60s infinite alternate ease-in-out;
        }}
        </style>
        '''
        st.markdown(page_bg_img, unsafe_allow_html=True)
    except FileNotFoundError:
        st.error("Gdzie jest background.jpg?! Wrzuć plik do folderu.")

# 1. Konfiguracja strony
st.set_page_config(page_title="AI Document Translator", page_icon="✨", layout="wide")

# Wczytanie grafiki i odpalenie animacji ruchu
set_background('background.jpg')

# 2. Konfiguracja DeepL
AUTH_KEY = "09d9dd8f-b8c5-45e6-be4f-dab5b623c368:fx"
translator = deepl.Translator(AUTH_KEY)

# 3. CSS - Jasny Glassmorphism, 3D Cienie i Ruch
css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');

/* Reset globalny fontu i koloru (ciemny grafit dla czytelności na szkle) */
* {
    font-family: 'Inter', sans-serif;
    color: #1e293b !important; 
}

[data-testid="stHeader"], [data-testid="stFooter"] {
    display: none;
}

/* GŁÓWNA NAKŁADKA - Jasne, czyste szkło zamiast ciemnego */
[data-testid="stAppViewContainer"] {
    background: rgba(255, 255, 255, 0.15); /* Bardzo delikatna biel */
    backdrop-filter: blur(35px); /* Rozmycie tła */
    -webkit-backdrop-filter: blur(35px);
}

.block-container {
    max-width: 800px !important;
    padding-top: 8vh !important;
    padding-bottom: 8vh !important;
}

/* Nowoczesny Tytuł z gradientem dopasowanym do jasnego motywu */
h1 {
    font-weight: 800 !important;
    font-size: 3.5rem !important;
    text-align: center;
    background: linear-gradient(135deg, #3b82f6, #8b5cf6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.2rem !important;
    text-shadow: 0 10px 30px rgba(99, 102, 241, 0.2); /* Lekka poświata */
}

.stMarkdown p {
    text-align: center;
    font-size: 1.15rem;
    color: #475569 !important; /* Zgaszony granat dla podtytułu */
    font-weight: 400;
    margin-bottom: 2.5rem !important;
}

/* --- KONTENERY INTERFEJSU (Głębia i brak czerni) --- */

/* Selectbox */
.stSelectbox div[data-baseweb="select"] {
    background: rgba(255, 255, 255, 0.4) !important;
    border: 1px solid rgba(255, 255, 255, 0.6) !important;
    border-radius: 16px !important;
    box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.1) !important; /* Efekt głębi */
    transition: all 0.3s ease;
}
.stSelectbox div[data-baseweb="select"]:hover {
    background: rgba(255, 255, 255, 0.6) !important;
    box-shadow: 0 12px 40px 0 rgba(31, 38, 135, 0.15) !important;
}

/* Uploader plików */
.stFileUploader section {
    background: rgba(255, 255, 255, 0.3) !important;
    border: 2px dashed rgba(99, 102, 241, 0.4) !important;
    border-radius: 20px !important;
    padding: 35px !important;
    box-shadow: inset 0 0 20px rgba(255, 255, 255, 0.5), 0 10px 30px rgba(0, 0, 0, 0.05) !important; /* Głębia do wewnątrz i na zewnątrz */
    transition: all 0.3s ease;
}
.stFileUploader section:hover {
    background: rgba(255, 255, 255, 0.5) !important;
    border-color: #6366f1 !important;
    transform: translateY(-2px);
    box-shadow: inset 0 0 20px rgba(255, 255, 255, 0.6), 0 15px 40px rgba(0, 0, 0, 0.1) !important;
}

/* Przycisk akcji */
.stButton button {
    width: 100%;
    background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%) !important;
    color: white !important; /* Tu wymuszamy biel, żeby napis na przycisku był widoczny */
    border: none !important;
    padding: 16px 24px !important;
    border-radius: 16px !important;
    font-weight: 700 !important;
    font-size: 1.15rem !important;
    letter-spacing: 1px;
    box-shadow: 0 10px 25px -5px rgba(168, 85, 247, 0.5), inset 0 2px 5px rgba(255, 255, 255, 0.3) !important;
    transition: all 0.2s ease-in-out !important;
}
.stButton button:hover {
    transform: translateY(-4px);
    box-shadow: 0 20px 35px -10px rgba(168, 85, 247, 0.7), inset 0 2px 5px rgba(255, 255, 255, 0.4) !important;
}

/* Podgląd tekstu */
.stTextArea textarea {
    background: rgba(255, 255, 255, 0.4) !important;
    border: 1px solid rgba(255, 255, 255, 0.7) !important;
    border-radius: 16px !important;
    box-shadow: inset 0 4px 10px rgba(0, 0, 0, 0.03) !important;
    color: #334155 !important;
}

/* Powiadomienia (Alerts) */
.stAlert {
    background: rgba(255, 255, 255, 0.6) !important;
    border: 1px solid rgba(255, 255, 255, 0.8) !important;
    border-left: 5px solid #10b981 !important; /* Zielony pasek boczny dla sukcesu */
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05) !important;
    border-radius: 16px !important;
}

/* Powiadomienie błędu (nadpisanie paska) */
.stAlert:has(.st-emotion-cache-1kqow14) { /* Klasa błędu Streamlit */
    border-left-color: #ef4444 !important;
}
</style>
"""

st.markdown(css, unsafe_allow_html=True)

# 4. Interfejs aplikacji
st.title("Tłumacz AI PRO")
st.write("Wgraj dokument (TXT, SRT). Struktura pozostanie nienaruszona.")

target_languages = {
    "Polski": "PL", 
    "Angielski (USA)": "EN-US", 
    "Niemiecki": "DE", 
    "Hiszpański": "ES",
    "Francuski": "FR"
}

selected_lang = st.selectbox("Wybierz język docelowy:", list(target_languages.keys()))
target_code = target_languages[selected_lang]

uploaded_file = st.file_uploader("Przeciągnij i upuść plik tutaj", type=["txt", "srt"])

if uploaded_file is not None:
    file_ext = uploaded_file.name.split('.')[-1].lower()
    
    try:
        preview_text = uploaded_file.getvalue().decode("utf-8")
        st.text_area("Podgląd struktury pliku", preview_text[:300] + "...\n[...]", height=130, disabled=True)
    except Exception:
        st.error("Problem z kodowaniem pliku. Upewnij się, że to format UTF-8.")

    if st.button("🚀 URUCHOM TŁUMACZENIE"):
        with st.spinner("Sztuczna inteligencja pracuje nad dokumentem..."):
            try:
                with tempfile.NamedTemporaryFile(delete=False, suffix=f".{file_ext}") as temp_in:
                    temp_in.write(uploaded_file.getvalue())
                    temp_in_path = temp_in.name
                
                temp_out_path = temp_in_path.replace(f".{file_ext}", f"_out.{file_ext}")

                translator.translate_document_from_filepath(
                    temp_in_path,
                    temp_out_path,
                    target_lang=target_code
                )

                with open(temp_out_path, "rb") as f:
                    translated_bytes = f.read()

                os.remove(temp_in_path)
                os.remove(temp_out_path)

                st.success("Wszystko poszło gładko! Plik przetłumaczony, formatowanie nienaruszone.")
                
                new_filename = f"{target_code}_{uploaded_file.name}"
                st.download_button(
                    label="💾 POBIERZ GOTOWY PLIK",
                    data=translated_bytes,
                    file_name=new_filename,
                    mime="text/plain"
                )
                
            except Exception as e:
                st.error(f"Błąd krytyczny: {e}")
