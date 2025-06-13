# auth/login.py
import streamlit as st
from database.db import verificar_usuario

def login():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        st.title("🔐 Iniciar sesión")
        username = st.text_input("Usuario")
        password = st.text_input("Contraseña", type="password")

        if st.button("Ingresar"):
            if verificar_usuario(username, password):
                st.session_state.logged_in = True
                st.success("¡Bienvenido!")
                st.experimental_rerun()
            else:
                st.error("Usuario o contraseña inválidos")
        st.stop()
