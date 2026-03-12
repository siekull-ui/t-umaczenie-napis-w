import streamlit as st
import deepl
import tempfile
import os

# 1. Konfiguracja wyglądu strony
st.set_page_config(page_title="Inteligentny Tłumacz", page_icon="🌍", layout="centered")

st.title("🌍 Tłumacz Plików (TXT, SRT)")
st.write("Wgraj plik, a AI od DeepL przetłumaczy go z zachowaniem **pełnej struktury** (odstępy, entery, kody czasowe w SRT pozostaną nienaruszone)!")

# 2. Konfiguracja DeepL
# W Streamlit Cloud zamień to później na: AUTH_KEY = st.secrets["DEEPL_API_KEY"]
AUTH_KEY = "09d9dd8f-b8c5-45e6-be4f-dab5b623c368:fx"
translator = deepl.Translator(AUTH_KEY)

# 3. Wybór języka docelowego
target_languages = {
    "Polski": "PL", 
    "Angielski (USA)": "EN-US", 
    "Niemiecki": "DE", 
    "Hiszpański": "ES",
    "Francuski": "FR"
}
selected_lang = st.selectbox("Wybierz język docelowy:", list(target_languages.keys()))
target_code = target_languages[selected_lang]

# 4. Moduł wgrywania pliku
uploaded_file = st.file_uploader("Wybierz plik (.txt lub .srt)", type=["txt", "srt"])

if uploaded_file is not None:
    # Pobieramy rozszerzenie pliku, żeby DeepL wiedział, z czym ma do czynienia
    file_ext = uploaded_file.name.split('.')[-1].lower()
    
    st.subheader("📄 Podgląd wgranego pliku:")
    # Pokazujemy tylko podgląd (nie wysyłamy tego tekstu bezpośrednio do tłumacza)
    preview_text = uploaded_file.getvalue().decode("utf-8")
    st.text_area("Początek pliku", preview_text[:400] + "\n...", height=150, disabled=True)
    
    if st.button("🚀 Przetłumacz plik"):
        with st.spinner("Trwa tłumaczenie dokumentu... (DeepL analizuje i chroni strukturę plików SRT/TXT)"):
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

                st.success("Tłumaczenie zakończone! Formaty, czasy i entery zostały zachowane.")
                
                # KROK F: Przycisk do pobrania w dokładnie tym samym formacie
                new_filename = f"PL_{uploaded_file.name}"
                st.download_button(
                    label=f"⬇️ Pobierz gotowy plik (.{file_ext.upper()})",
                    data=translated_bytes,
                    file_name=new_filename,
                    mime="text/plain"
                )
                
            except deepl.DocumentTranslationException as e:
                st.error(f"Błąd podczas analizy struktury pliku: {e}")
            except Exception as e:
                st.error(f"Wystąpił nieoczekiwany błąd: {e}")
