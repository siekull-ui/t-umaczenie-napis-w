import streamlit as st

def set_animated_gradient_bg():
    st.markdown(
        """
        <style>
        [data-testid="stAppViewContainer"] {
            background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
            background-size: 400% 400%;
            animation: gradient 15s ease infinite;
            height: 100vh;
        }

        @keyframes gradient {
            0% {
                background-position: 0% 50%;
            }
            50% {
                background-position: 100% 50%;
            }
            100% {
                background-position: 0% 50%;
            }
        }
        
        /* Opcjonalnie: poprawienie widoczności tekstu */
        [data-testid="stHeader"] {
            background: rgba(0,0,0,0);
        }
        </style>
        """,
        unsafe_allow_html=True
    )

set_animated_gradient_bg()

st.title("Moja aplikacja z animowanym tłem")
st.write("To tło porusza się delikatnie jak fale gradientu.")
