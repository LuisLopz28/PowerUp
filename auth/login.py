# auth/login.py
import streamlit as st

USERS = {
    "admin": "admin123",
    "luis": "powerup2025"
}

def login():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        st.title("🔒 Iniciar sesión")
        user = st.text_input("Usuario")
        password = st.text_input("Contraseña", type="password")
        if st.button("Ingresar"):
            if USERS.get(user) == password:
                st.session_state.logged_in = True
                st.experimental_rerun()
            else:
                st.error("Credenciales inválidas")
        st.stop()
