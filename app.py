import streamlit as st

# --- 1. MINIMALISTYCZNA KONFIGURACJA ---
st.set_page_config(
    page_title="Blank Hero",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. STAN APLIKACJI (Z PARAMETRÓW URL) ---
current_tab = st.query_params.get("tab", "Home")

# --- 3. STATYCZNY INTERFEJS (Nigdy się nie przeładowuje) ---
# Tego stringa HTML/CSS nie modyfikujemy dynamicznie z poziomu Pythona.
# Dzięki temu Streamlit zachowuje ten element w przeglądarce, pozwalając na płynne animacje.
STATIC_HTML = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500&display=swap');

/* Ukrycie elementów systemowych Streamlit */
[data-testid="stHeader"], [data-testid="stFooter"], [data-testid="stToolbar"] {
    display: none !important;
}

.stApp {
    background-color: #F0D3DE !important;
}

/* KONTENER HERO */
#hero-canvas {
    position: fixed;
    top: 1cm;
    bottom: 1cm;
    left: 1cm;
    right: 1cm;
    
    background: rgba(255, 255, 255, 0.25);
    backdrop-filter: blur(25px) saturate(150%);
    -webkit-backdrop-filter: blur(25px) saturate(150%);
    
    border-radius: 1cm;
    border: none;
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
    z-index: 1000;
}

/* --- NAWIGACJA --- */
.hero-nav {
    position: fixed;
    top: calc(1cm + 40px);
    right: calc(1cm + 50px);
    display: flex;
    gap: 60px;
    align-items: center;
    font-family: 'Poppins', sans-serif;
    z-index: 1002; 
}

.hero-nav a {
    color: #1a1a1a !important;
    text-decoration: none;
    font-size: 14px;
    font-weight: 500;
    cursor: pointer;
    position: relative;
    padding-bottom: 5px; /* Przestrzeń pod tekstem na falę */
}

/* --- PŁYWAJĄCY WĘŻYK (MAGICZNA CZĘŚĆ) --- */
.active-wave {
    position: absolute;
    bottom: -10px;
    left: 0;
    height: 6px;
    
    background-image: url("data:image/svg+xml,%3Csvg width='30' height='6' viewBox='0 0 30 6' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M0 3C5 1 10 1 15 3C20 5 25 5 30 3' stroke='%23FF2A5F' stroke-width='1.5' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E");
    background-repeat: repeat-x;
    
    /* Płynna animacja transformacji i szerokości */
    transition: transform 0.4s cubic-bezier(0.25, 1, 0.5, 1), width 0.4s cubic-bezier(0.25, 1, 0.5, 1);
    pointer-events: none;
    width: 0px; /* Startowa szerokość ukryta, JS nada odpowiednią */
    z-index: 1003;
}

/* --- RESZTA STYLÓW --- */
.hero-nav .search-icon {
    margin-left: -20px;
    display: flex;
    align-items: center;
}

.hero-nav .search-icon svg {
    width: 18px;
    height: 18px;
    stroke: #1a1a1a;
    stroke-width: 2;
    transition: stroke 0.2s ease;
}

.hero-nav .search-icon:hover svg {
    stroke: #FF2A5F; 
}

.main .block-container {
    padding: 0 !important;
    position: relative;
    z-index: 1001 !important; 
}

.content-area {
    margin-top: 150px; 
    padding-left: 2.5cm;
    padding-right: 2.5cm;
    font-family: 'Poppins', sans-serif;
}
</style>

<div id="hero-canvas"></div>
<nav class="hero-nav" id="main-nav">
    <div class="active-wave" id="wave"></div>
    
    <a data-tab="Home" href="?tab=Home" target="_self">Home</a>
    <a data-tab="About" href="?tab=About" target="_self">About</a>
    <a data-tab="Services" href="?tab=Services" target="_self">Services</a>
    <a data-tab="Portfolio" href="?tab=Portfolio" target="_self">Portfolio</a>
    <a data-tab="Contact" href="?tab=Contact" target="_self">Contact</a>
    
    <a class="search-icon">
        <svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="11" cy="11" r="8"></circle>
            <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
        </svg>
    </a>
</nav>

<img src="dummy" style="display:none;" onerror="
    if(!window.navInitialized) {
        const wave = document.getElementById('wave');
        const links = document.querySelectorAll('a[data-tab]');
        
        links.forEach(link => {
            link.addEventListener('click', function(e) {
                // Obliczamy natychmiastową pozycję i przesuwamy wężyk w ułamku sekundy
                const linkRect = this.getBoundingClientRect();
                const navRect = this.parentElement.getBoundingClientRect();
                const offset = linkRect.left - navRect.left;
                
                wave.style.width = linkRect.width + 'px';
                wave.style.transform = `translateX(${offset}px)`;
            });
        });
        window.navInitialized = true;
    }
">
"""

# Renderujemy główny interfejs (tylko raz, zapobiega to niszczeniu animacji)
st.markdown(STATIC_HTML, unsafe_allow_html=True)

# --- 4. DYNAMICZNY SYNCHRONIZATOR STANU ---
# Ten kod zapewnia, że wężyk wraca na odpowiednie miejsce po odświeżeniu, 
# użyciu przycisku 'wstecz' w przeglądarce lub podczas ładowania zawartości przez Streamlit.
st.markdown(f"""
<img src="sync_{current_tab}" style="display:none;" onerror="
    setTimeout(() => {{
        const wave = document.getElementById('wave');
        const activeLink = document.querySelector(`a[data-tab='{current_tab}']`);
        if(wave && activeLink) {{
            const linkRect = activeLink.getBoundingClientRect();
            const navRect = activeLink.parentElement.getBoundingClientRect();
            const offset = linkRect.left - navRect.left;
            
            wave.style.width = linkRect.width + 'px';
            wave.style.transform = `translateX(${{offset}}px)`;
        }}
    }}, 50); // Minimalne opóźnienie dla pewności, że czcionki i wymiary są wyrenderowane
">
""", unsafe_allow_html=True)

# --- 5. WYŚWIETLANIE TREŚCI ---
st.markdown("<div class='content-area'>", unsafe_allow_html=True)

if current_tab == "Home":
    st.title("Witaj w Blank Hero")
    st.write("Kliknij dowolną zakładkę w nawigacji. Zauważysz, jak podświetlenie płynnie przesuwa się na wybrane miejsce!")
    
elif current_tab == "About":
    st.title("O mnie")
    st.write("Student pielęgniarstwa (rocznik 2025). Tutaj gromadzę materiały z zajęć, notatki kliniczne i projekty medyczne.")
    
elif current_tab == "Services":
    st.title("Usługi")
    st.write("Miejsce na listę usług lub specjalizacji.")
    
elif current_tab == "Portfolio":
    st.title("Portfolio")
    st.write("Galeria projektów i certyfikatów.")
    
elif current_tab == "Contact":
    st.title("Kontakt")
    st.text_input("Zostaw wiadomość:", placeholder="Napisz do mnie...")
    st.button("Wyślij")

st.markdown("</div>", unsafe_allow_html=True)
