import streamlit as st
import deepl
import tempfile
import os
import base64

# --- FUNKCJA DO WCZYTANIA TŁA ---
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    try:
        bin_str = get_base64_of_bin_file(png_file)
        # Nakładamy obraz na sam spód (.stApp)
        page_bg_img = f'''
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{bin_str}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        '''
        st.markdown(page_bg_img, unsafe_allow_html=True)
    except FileNotFoundError:
        st.error("Nie znaleziono pliku background.jpg - dorzuć go do folderu ze skryptem!")

# 1. Konfiguracja strony (ustawiamy na 'wide', żeby kontener mógł się rozlać, ale tekst wyśrodkujemy)
st.set_page_config(page_title="AI Document Translator", page_icon="🌍", layout="wide")

# Wczytanie grafiki tła
set_background('background.jpg')

# 2. Konfiguracja DeepL
AUTH_KEY = "09d9dd8f-b8c5-45e6-be4f-dab5b623c368:fx"
translator = deepl.Translator(AUTH_KEY)

# 3. CSS - Pełnoekranowy Glassmorphism
css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');

* {
    font-family: 'Inter', sans-serif;
    color: #ffffff !important; /* Wymuszamy biały tekst na całości, żeby pasował do szkła */
}

/* Ukrycie śmieci od Streamlita */
[data-testid="stHeader"], [data-testid="stFooter"] {
    display: none;
}

/* TO JEST KLUCZ: Nakładka na CAŁY EKRAN z efektem potężnego rozmycia */
[data-testid="stAppViewContainer"] {
    background: rgba(20, 20, 30, 0.4); /* Półprzezroczysty ciemny fiolet/granat */
    backdrop-filter: blur(50px); /* Ekstremalny blur - tło staje się tylko poświatą */
    -webkit-backdrop-filter: blur(50px);
}

/* Środkowanie zawartości, żeby tekst nie latał po rogach ekranu */
.block-container {
    max-width: 750px !important;
    padding-top: 10vh !important;
    padding-bottom: 10vh !important;
}

/* Nowoczesny Tytuł */
h1 {
    font-weight: 800 !important;
    font-size: 3rem !important;
    text-align: center;
    background: linear-gradient(135deg, #fff, #a78bfa);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.5rem !important;
}

/* Subtytuł pod h1 */
.stMarkdown p {
    text-align: center;
    font-size: 1.1rem;
    opacity: 0.8;
    margin-bottom: 2rem !important;
}

/* Pola wyboru i uploader */
.stSelectbox div[data-baseweb="select"] {
    background: rgba(255, 255, 255, 0.1) !important;
    border: 1px solid rgba(255, 255, 255, 0.2) !important;
    border-radius: 12px !important;
}

.stFileUploader section {
    background: rgba(255, 255, 255, 0.05) !important;
    border: 2px dashed rgba(255, 255, 255, 0.3) !important;
    border-radius: 16px !important;
    padding: 30px !important;
    transition: all 0.3s ease;
}

.stFileUploader section:hover {
    background: rgba(255, 255, 255, 0.1) !important;
    border-color: #8b5cf6 !important;
}

/* Przyciski */
.stButton button {
    width: 100%;
    background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%) !important;
    border: none !important;
    padding: 14px 24px !important;
    border-radius: 12px !important;
    font-weight: 700 !important;
    font-size: 1.1rem !important;
    letter-spacing: 1px;
    box-shadow: 0 10px 30px -10px rgba(168, 85, 247, 0.6);
    transition: all 0.2s ease-in-out !important;
}

.stButton button:hover {
    transform: translateY(-3px);
    box-shadow: 0 15px 35px -10px rgba(168, 85, 247, 0.8);
}

/* Pole tekstowe podglądu */
.stTextArea textarea {
    background: rgba(0, 0, 0, 0.3) !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    border-radius: 12px !important;
}

/* Powiadomienia */
.stAlert {
    background: rgba(16, 185, 129, 0.2) !important;
    border: 1px solid rgba(16, 185, 129, 0.4) !important;
    backdrop-filter: blur(10px);
    border-radius: 12px !important;
}
</style>
"""

st.markdown(css, unsafe_allow_html=True)

# 4. Interfejs (bez dodatkowego diva, bo cała strona to teraz szkło)
st.title("Tłumacz AI PRO")
st.write("Wgraj plik TXT lub SRT. Pełna struktura zostanie zachowana.")

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
        st.error("Problem z kodowaniem pliku. Upewnij się, że to UTF-8.")

    if st.button("🚀 URUCHOM TŁUMACZENIE"):
        with st.spinner("DeepL analizuje i tłumaczy dokument..."):
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

                st.success("Tłumaczenie gotowe! Formatowanie zachowane.")
                
                new_filename = f"{target_code}_{uploaded_file.name}"
                st.download_button(
                    label="💾 POBIERZ PRZETŁUMACZONY PLIK",
                    data=translated_bytes,
                    file_name=new_filename,
                    mime="text/plain"
                )
                
            except Exception as e:
                st.error(f"Błąd krytyczny: {e}")
