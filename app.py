import streamlit as st
import deepl

# 1. Konfiguracja wyglądu strony
st.set_page_config(page_title="Inteligentny Tłumacz", page_icon="🌍", layout="centered")

st.title("🌍 Tłumacz Plików (TXT, SRT)")
st.write("Wgraj swój plik, a AI od DeepL przetłumaczy go z zachowaniem pełnego kontekstu!")

# 2. Konfiguracja DeepL
# WAŻNE: W gotowej aplikacji na Hubie ten klucz ukryjemy w tzw. "Secrets", 
# ale do testów lokalnych możemy wpisać go tutaj.
AUTH_KEY = "09d9dd8f-b8c5-45e6-be4f-dab5b623c368:fx"
translator = deepl.Translator(AUTH_KEY)

# 3. Wybór języka docelowego
# Słownik ułatwiający wybór - przyjazna nazwa dla Ciebie, kod dla DeepL
target_languages = {
    "Polski": "PL", 
    "Angielski (USA)": "EN-US", 
    "Niemiecki": "DE", 
    "Hiszpański": "ES",
    "Francuski": "FR"
}
selected_lang = st.selectbox("Wybierz język, na który chcesz przetłumaczyć:", list(target_languages.keys()))
target_code = target_languages[selected_lang]

# 4. Moduł wgrywania pliku
uploaded_file = st.file_uploader("Wybierz plik (.txt lub .srt)", type=["txt", "srt"])

if uploaded_file is not None:
    # Odczytanie zawartości pliku
    text_data = uploaded_file.read().decode("utf-8")
    
    # Pokazanie podglądu, żebyś wiedział, że plik wczytał się poprawnie (pokazuje pierwsze 300 znaków)
    st.subheader("📄 Podgląd oryginału:")
    st.text_area("Oryginalny tekst", text_data[:300] + "...", height=150, disabled=True)
    
    # Przycisk uruchamiający tłumaczenie
    if st.button("🚀 Przetłumacz plik"):
        with st.spinner("Trwa tłumaczenie... (przy długich plikach może to zająć kilkanaście sekund)"):
            try:
                # Wysłanie tekstu do DeepL
                # preserve_formatting=True stara się zachować strukturę linii, co jest kluczowe dla plików SRT
                result = translator.translate_text(text_data, target_lang=target_code, preserve_formatting=True)
                translated_text = result.text
                
                st.success("Tłumaczenie zakończone sukcesem!")
                
                st.subheader("✅ Podgląd tłumaczenia:")
                st.text_area("Przetłumaczony tekst", translated_text[:300] + "...", height=150, disabled=True)
                
                # Przycisk do pobrania przetłumaczonego pliku na dysk
                new_filename = f"Przetlumaczone_{uploaded_file.name}"
                st.download_button(
                    label="⬇️ Pobierz gotowy plik",
                    data=translated_text,
                    file_name=new_filename,
                    mime="text/plain"
                )
            except deepl.DeepLException as e:
                st.error(f"Wystąpił błąd z serwerem DeepL: {e}")
