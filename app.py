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
        st.warning("Nie znaleziono pliku background.jpg - używam standardowego gradientu.")
        st.markdown("<style>.stApp { background: linear-gradient(135deg, #0f172a, #1e293b); }</style>", unsafe_allow_html=True)

# 1. Konfiguracja strony
st.set_page_config(page_title="AI Document Translator", page_icon="🌐", layout="centered")

# Wczytanie grafiki tła
set_background('background.jpg')

# 2. Konfiguracja DeepL
AUTH_KEY = "09d9dd8f-b8c5-45e6-be4f-dab5b623c368:fx"
translator = deepl.Translator(AUTH_KEY)

# 3. Nowoczesny CSS (Inter Font & Glassmorphism)
css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');

/* Globalne style */
* {
    font-family: 'Inter', sans-serif;
}

[data-testid="stHeader"], [data-testid="stFooter"] {
    display: none;
}

/* Kontener Glassmorphism */
.glass-container {
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border-radius: 24px;
    border: 1px solid rgba(255, 255, 255, 0.15);
    padding: 40px;
    box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
    margin-top: 20px;
    color: white;
}

h1 {
    font-weight: 700 !important;
    letter-spacing: -1px;
    background: linear-gradient(to right, #ffffff, #94a3b8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Stylizacja inputów i boxów */
.stSelectbox div[data-baseweb="select"] {
    background: rgba(255, 255, 255, 0.1) !important;
    border: 1px solid rgba(255, 255, 255, 0.2) !important;
    border-radius: 12px !important;
    color: white !important;
}

.stFileUploader section {
    background: rgba(255, 255, 255, 0.03) !important;
    border: 2px dashed rgba(255, 255, 255, 0.2) !important;
    border-radius: 16px !important;
    padding: 20px !important;
}

/* Przycisk w stylu nowoczesnym */
.stButton button {
    width: 100%;
    background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%) !important;
    color: white !important;
    border: none !important;
    padding: 12px 24px !important;
    border-radius: 12px !important;
    font-weight: 600 !important;
    text-transform: uppercase;
    letter-spacing: 1px;
    transition: all 0.3s ease !important;
    box-shadow: 0 10px 20px -5px rgba(59, 130, 246, 0.5);
}

.stButton button:hover {
    transform: translateY(-2px);
    box-shadow: 0 15px 25px -5px rgba(59, 130, 246, 0.6);
    opacity: 0.9;
}

/* Text area */
.stTextArea textarea {
    background: rgba(0, 0, 0, 0.2) !important;
    color: #cbd5e1 !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    border-radius: 12px !important;
}

/* Alert sukcesu */
.stAlert {
    background: rgba(16, 185, 129, 0.2) !important;
    color: #ecfdf5 !important;
    border: 1px solid rgba(16, 185, 129, 0.3) !important;
    border-radius: 12px !important;
}
</style>
"""

st.markdown(css, unsafe_allow_html=True)

# 4. Budowa interfejsu
with st.container():
    st.markdown('<div class="glass-container">', unsafe_allow_html=True)
    
    st.title("AI Document Translator")
    st.markdown("<p style='opacity: 0.8; font-size: 0.9rem;'>Premium translation service powered by DeepL</p>", unsafe_allow_html=True)

    # Wybór języka
    target_languages = {
        "Polski": "PL", 
        "Angielski (USA)": "EN-US", 
        "Niemiecki": "DE", 
        "Hiszpański": "ES",
        "Francuski": "FR"
    }
    
    col1, col2 = st.columns([1, 1])
    with col1:
        selected_lang = st.selectbox("Język docelowy", list(target_languages.keys()))
    
    target_code = target_languages[selected_lang]

    # Uploader
    uploaded_file = st.file_uploader("Wrzuć dokument (TXT, SRT)", type=["txt", "srt"])

    if uploaded_file is not None:
        file_ext = uploaded_file.name.split('.')[-1].lower()
        
        try:
            preview_text = uploaded_file.getvalue().decode("utf-8")
            st.text_area("Podgląd treści", preview_text[:250] + "...", height=120, disabled=True)
        except Exception:
            st.error("Błąd kodowania pliku.")

        if st.button("Rozpocznij tłumaczenie"):
            with st.spinner("Przetwarzanie przez neurony DeepL..."):
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

                    st.success("Gotowe! Plik jest gotowy do pobrania.")
                    
                    new_filename = f"Translated_{uploaded_file.name}"
                    st.download_button(
                        label="POBIERZ PLIK",
                        data=translated_bytes,
                        file_name=new_filename,
                        mime="text/plain"
                    )
                    
                except Exception as e:
                    st.error(f"Coś poszło nie tak: {e}")

    st.markdown('</div>', unsafe_allow_html=True)
