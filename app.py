import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components  # DODANY IMPORT

# --- KONFIGURACJA STRONY ---
st.set_page_config(page_title="Korepetycje Biologia", page_icon="🧬", layout="wide", initial_sidebar_state="collapsed")

# --- STYLE CSS (GLASSMORPHISM) ---
css = """
<style>
/* Ukrycie domyślnego UI Streamlita */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.block-container {padding-top: 2rem; padding-bottom: 2rem;}

/* Głębokie tło podbijające efekt szkła */
.stApp {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    color: #ffffff;
}

/* Magia Glassmorphismu dla niestandardowych elementów HTML */
.glass-card {
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 16px;
    padding: 2.5rem;
    margin-bottom: 1.5rem;
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
    color: white;
    transition: transform 0.3s ease;
}

.glass-card:hover {
    transform: translateY(-5px);
    background: rgba(255, 255, 255, 0.08);
}

/* Typografia i detale */
h1, h2, h3, p, li {
    font-family: 'Inter', 'Montserrat', sans-serif;
    color: white !important;
}

/* Stylizacja natywnych przycisków Streamlit */
div.stButton > button {
    background: rgba(255, 255, 255, 0.1) !important;
    border: 1px solid rgba(255, 255, 255, 0.3) !important;
    border-radius: 8px !important;
    color: white !important;
    transition: all 0.3s ease !important;
    padding: 0.5rem 2rem !important;
    font-weight: bold !important;
}

div.stButton > button:hover {
    background: rgba(255, 255, 255, 0.2) !important;
    transform: translateY(-2px) !important;
    border-color: #ffffff !important;
    box-shadow: 0 4px 15px rgba(255, 255, 255, 0.1) !important;
}
</style>
"""
st.markdown(css, unsafe_allow_html=True)

# --- NAWIGACJA (ZAMROŻONY PASEK) ---
selected = option_menu(
    menu_title=None,
    options=["Start", "O mnie", "Oferta", "Zapisy"],
    icons=["house", "person", "book", "calendar-check"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {
            "padding": "0!important", 
            "background-color": "rgba(255, 255, 255, 0.05)", 
            "backdrop-filter": "blur(10px)", 
            "border": "1px solid rgba(255, 255, 255, 0.1)", 
            "border-radius": "10px",
            "max-width": "800px",
            "margin": "0 auto"
        },
        "icon": {"color": "white", "font-size": "18px"},
        "nav-link": {
            "color": "#e0e0e0", 
            "font-size": "16px", 
            "text-align": "center", 
            "margin":"0px", 
            "--hover-color": "rgba(255, 255, 255, 0.1)"
        },
        "nav-link-selected": {
            "background-color": "rgba(255, 255, 255, 0.15)", 
            "color": "white", 
            "font-weight": "bold", 
            "border-bottom": "2px solid #ffffff"
        },
    }
)

st.markdown("<br><br>", unsafe_allow_html=True)

# --- WIDOKI (ZAKŁADKI) ---

if selected == "Start":
    col1, col2, col3 = st.columns([1, 4, 1])
    with col2:
        st.markdown("""
        <div style="text-align: center; padding: 4rem 0;">
            <h1 style="font-size: 4rem; font-weight: 800; margin-bottom: 1rem; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">
                Zrozum biologię.<br>Zdaj egzaminy. Osiągnij cel.
            </h1>
            <p style="font-size: 1.5rem; color: #e0e0e0; margin-bottom: 2rem;">
                Nowoczesne korepetycje łączące teorię z medyczną praktyką.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('<div style="display: flex; justify-content: center;">', unsafe_allow_html=True)
        if st.button("Rozpocznij naukę", use_container_width=False):
            st.success("Przejdź do zakładki 'Zapisy', aby wybrać termin!")
        st.markdown('</div>', unsafe_allow_html=True)

elif selected == "O mnie":
    col1, col2, col3 = st.columns([1, 6, 1])
    with col2:
        st.markdown("""
        <div class="glass-card">
            <h2 style="text-align: center; margin-bottom: 2rem;">🧬 Twoje zdrowie i wiedza w dobrych rękach</h2>
            <div style="display: flex; flex-wrap: wrap; gap: 2rem; align-items: center;">
                <div style="flex: 2; min-width: 300px;">
                    <p style="font-size: 1.1rem; line-height: 1.6;">
                        Uważam, że biologia to instrukcja obsługi nas samych. Suche fakty z podręcznika często bywają trudne do zapamiętania, dopóki nie zobaczymy ich w życiowym kontekście.
                    </p>
                    <p style="font-size: 1.1rem; line-height: 1.6;">
                        Będąc na pielęgniarstwie, mam absolutnie świeże spojrzenie na to, jak szkolna teoria łączy się z prawdziwą wiedzą medyczną. Wiedzę z anatomii, fizjologii czy biochemii zdobywam i testuję na co dzień w praktyce.
                    </p>
                    <ul style="font-size: 1.1rem; line-height: 1.6;">
                        <li>Przekładam trudne mechanizmy biologiczne na obrazowe, medyczne przykłady z życia wzięte.</li>
                        <li>Pokazuję przyczynowość i skutki – uczymy się zrozumienia procesów, a nie "wykuwania" na pamięć.</li>
                        <li>Pomagam przełamać stres przed maturą, bazując na własnym, niedawnym doświadczeniu egzaminacyjnym.</li>
                    </ul>
                </div>
                <div style="flex: 1; min-width: 250px; text-align: center;">
                    <img src="https://images.unsplash.com/photo-1532938911079-1b06ac7ceec7?auto=format&fit=crop&q=80&w=400" style="width: 100%; border-radius: 12px; border: 2px solid rgba(255,255,255,0.2); box-shadow: 0 4px 15px rgba(0,0,0,0.4);">
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

elif selected == "Oferta":
    st.markdown("<h2 style='text-align: center; margin-bottom: 2rem;'>📚 Wybierz poziom dla siebie</h2>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="glass-card" style="text-align: center;">
            <h3>Szkoła Podstawowa</h3>
            <h1 style="color: #4facfe;">60 zł<span style="font-size: 1rem; color: #ccc;"> / 60 min</span></h1>
            <hr style="border-color: rgba(255,255,255,0.1);">
            <p style="text-align: left;">🔹 Nadrabianie zaległości</p>
            <p style="text-align: left;">🔹 Przygotowanie do sprawdzianów</p>
            <p style="text-align: left;">🔹 Egzamin ósmoklasisty</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class="glass-card" style="text-align: center; border: 1px solid rgba(79, 172, 254, 0.5);">
            <h3>Liceum / Podstawa</h3>
            <h1 style="color: #4facfe;">80 zł<span style="font-size: 1rem; color: #ccc;"> / 60 min</span></h1>
            <hr style="border-color: rgba(255,255,255,0.1);">
            <p style="text-align: left;">🔹 Bieżąca pomoc w nauce</p>
            <p style="text-align: left;">🔹 Zrozumienie trudnych pojęć</p>
            <p style="text-align: left;">🔹 Praca z arkuszami</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown("""
        <div class="glass-card" style="text-align: center;">
            <h3>Matura Rozszerzona</h3>
            <h1 style="color: #4facfe;">100 zł<span style="font-size: 1rem; color: #ccc;"> / 90 min</span></h1>
            <hr style="border-color: rgba(255,255,255,0.1);">
            <p style="text-align: left;">🔹 Analiza zadań maturalnych</p>
            <p style="text-align: left;">🔹 Klucz odpowiedzi CKE</p>
            <p style="text-align: left;">🔹 Powtórki z anatomii i genetyki</p>
        </div>
        """, unsafe_allow_html=True)

elif selected == "Zapisy":
    col1, col2, col3 = st.columns([1, 6, 1])
    with col2:
        st.markdown("""
        <div class="glass-card" style="text-align: center;">
            <h2>📅 Umów się na zajęcia</h2>
            <p>Wybierz dogodny dla siebie termin z kalendarza poniżej. Pierwsze, 30-minutowe zajęcia zapoznawcze są darmowe!</p>
            <hr style="border-color: rgba(255,255,255,0.1); margin: 2rem 0;">
        </div>
        """, unsafe_allow_html=True)
        
        calendly_url = "https://calendly.com/twoj-link-calendly"
        components.iframe(calendly_url, height=600, scrolling=True) # POPRAWIONE WYWOŁANIE

        st.markdown("""
        <div style="text-align: center; margin-top: 2rem; color: #aaa;">
            <p>Masz pytania? Napisz do mnie: <b>kontakt@twojadomena.pl</b></p>
        </div>
        """, unsafe_allow_html=True)
