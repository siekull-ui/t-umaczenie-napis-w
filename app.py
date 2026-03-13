import streamlit as st
import deepl
import tempfile
import os

# 1. Konfiguracja wyglądu strony (Jasny motyw w ustawieniach)
st.set_page_config(page_title="Inteligentny Tłumacz", page_icon="🌍", layout="centered", initial_sidebar_state="collapsed")

# 2. Konfiguracja DeepL
# W Streamlit Cloud zamień to później na: AUTH_KEY = st.secrets["DEEPL_API_KEY"]
AUTH_KEY = "09d9dd8f-b8c5-45e6-be4f-dab5b623c368:fx"
translator = deepl.Translator(AUTH_KEY)

# 3. Definiowanie kolorów i stylu CSS
accent_color_primary = "#0D6EFD"  # Niebieski
accent_color_secondary = "#6610f2" # Fioletowy
text_color = "#333"

css = f"""
<style>
/* Reset i główny gradient tła */
body {{
    margin: 0;
    padding: 0;
    background: linear-gradient(135deg, #e0f7fa, #d1c4e9);
    color: {text_color};
}}

/* Ukrycie domyślnego nagłówka i stopki Streamlit */
[data-testid="stHeader"], [data-testid="stFooter"] {{
    display: none;
}}

/* Główny kontener na środku */
.block-container {{
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    padding: 0;
}}

/* Kontener z efektem Glassmorphism */
.glass-container {{
    backdrop-filter: blur(10px);
    background: rgba(255, 255, 255, 0.4);
    border-radius: 20px;
    border: 1px solid rgba(255, 255, 255, 0.2);
    padding: 30px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
    width: 100%;
    max-width: 600px;
    text-align: center;
}}

/* Tytuł */
.stTitle {{
    font-weight: 700;
    margin-bottom: 10px;
}}

/* Opis */
.glass-container p {{
    margin-bottom: 30px;
}}

/* Stylizacja elementów Streamlit wewnątrz kontenera */
/* Selectbox */
.stSelectbox div[data-baseweb="select"] {{
    border-radius: 10px;
    border: 1px solid rgba(255, 255, 255, 0.3);
    background: rgba(255, 255, 255, 0.5);
}}

/* File Uploader */
.stFileUploader div[data-testid="stFileUploadDropzone"] {{
    border-radius: 15px;
    border: 2px dashed rgba(255, 255, 255, 0.5);
    background: rgba(255, 255, 255, 0.2);
    transition: background 0.3s ease;
}}
.stFileUploader div[data-testid="stFileUploadDropzone"]:hover {{
    background: rgba(255, 255, 255, 0.4);
}}

/* Przyciski */
.stButton button {{
    background: linear-gradient(135deg, {accent_color_primary}, {accent_color_secondary});
    color: white;
    border: none;
    border-radius: 10px;
    padding: 10px 20px;
    font-weight: 600;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}}
.stButton button:hover {{
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
}}
.stButton button:active {{
    transform: translateY(1px);
}}

/* Nagłówek podglądu */
.glass-container h3 {{
    margin-top: 30px;
}}

/* Pole podglądu tekstu */
.stTextArea textarea {{
    border-radius: 10px;
    border: 1px solid rgba(255, 255, 255, 0.3);
    background: rgba(255, 255, 255, 0.5);
}}

/* Komunikaty sukcesu i błędu */
.stAlert div {{
    border-radius: 10px;
}}

/* Stylizacja standardowego spinnera Streamlit wewnątrz karty */
.stSpinner div {{
    border-color: {accent_color_primary} {accent_color_primary} {accent_color_primary} transparent;
}}
</style>
"""

# 4. Wstrzyknięcie CSS
st.markdown(css, unsafe_allow_html=True)

# 5. Tworzenie kontenera z efektem Glassmorphism
with st.container():
    st.markdown('<div class="glass-container">', unsafe_allow_html=True)

    st.title("Tłumacz Plików (TXT, SRT)")
    st.write("Wgraj plik, a AI od DeepL przetłumaczy go z zachowaniem pełnej struktury (odstępy, entery, kody czasowe w SRT pozostaną nienaruszone).")

    # 6. Wybór języka docelowego
    target_languages = {
        "Polski": "PL", 
        "Angielski (USA)": "EN-US", 
        "Niemiecki": "DE", 
        "Hiszpański": "ES",
        "Francuski": "FR"
    }
    selected_lang = st.selectbox("Wybierz język docelowy:", list(target_languages.keys()))
    target_code = target_languages[selected_lang]

    # 7. Moduł wgrywania pliku
    uploaded_file = st.file_uploader("Wybierz plik (.txt lub .srt)", type=["txt", "srt"])

    if uploaded_file is not None:
        # Pobieramy rozszerzenie pliku, żeby DeepL wiedział, z czym ma do czynienia
        file_ext = uploaded_file.name.split('.')[-1].lower()
        
        st.subheader("Podgląd wgranego pliku")
        # Pokazujemy tylko podgląd (nie wysyłamy tego tekstu bezpośrednio do tłumacza)
        try:
            preview_text = uploaded_file.getvalue().decode("utf-8")
            st.text_area("Początek pliku", preview_text[:400] + "\n...", height=150, disabled=True)
        except UnicodeDecodeError:
            st.error("Wystąpił błąd przy dekodowaniu pliku. Upewnij się, że plik jest w formacie UTF-8.")
            st.markdown('</div>', unsafe_allow_html=True)
            st.stop()
        
        # 8. Tłumaczenie po kliknięciu przycisku
        if st.button("Przetłumacz plik"):
            # *Używamy standardowego spinnera Streamlit wewnątrz karty glassmorphism*
            # *Dodanie specyficznej, złożonej animacji cząsteczek z iPhone'a jest niemożliwe*
            # *przy użyciu czystego Streamlit w rozsądny sposób.*
            with st.spinner("Trwa tłumaczenie dokumentu..."):
                try:
                    # KROK A: Tworzymy tymczasowy plik wejściowy na serwerze
                    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{file_ext}") as temp_in:
                        temp_in.write(uploaded_file.getvalue())
                        temp_in_path = temp_in.name
                    
                    # KROK B: Tworzymy ścieżkę dla pliku wyjściowego
                    temp_out_path = temp_in_path.replace(f".{file_ext}", f"_out.{file_ext}")

                    # KROK C: Właściwe tłumaczenie DOKUMENTU, a nie surowego tekstu!
                    translator.translate_document_from_filepath(
                        temp_in_path,
                        temp_out_path,
                        target_lang=target_code
                    )

                    # KROK D: Odczytujemy gotowy, nienaruszony strukturalnie plik
                    with open(temp_out_path, "rb") as f:
                        translated_bytes = f.read()

                    # KROK E: Usuwamy pliki tymczasowe z serwera, żeby nie zaśmiecać dysku
                    os.remove(temp_in_path)
                    os.remove(temp_out_path)

                    st.success("Tłumaczenie zakończone. Formaty, czasy i entery zostały zachowane.")
                    
                    # KROK F: Przycisk do pobrania w dokładnie tym samym formacie
                    new_filename = f"PL_{uploaded_file.name}"
                    st.download_button(
                        label=f"Pobierz gotowy plik (.{file_ext.upper()})",
                        data=translated_bytes,
                        file_name=new_filename,
                        mime="text/plain"
                    )
                    
                except deepl.DocumentTranslationException as e:
                    st.error(f"Błąd podczas analizy struktury pliku: {e}")
                except Exception as e:
                    st.error(f"Wystąpił nieoczekiwany błąd: {e}")

    # Zamknięcie kontenera glass-container
    st.markdown('</div>', unsafe_allow_html=True)
