import streamlit as st
from login import check_login

st.set_page_config(page_title="PowerUp App", layout="wide")

# Estilos
with open("static/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Login
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    username = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")
    if st.button("Iniciar sesión"):
        if check_login(username, password):
            st.session_state.logged_in = True
            st.experimental_rerun()
        else:
            st.error("Credenciales inválidas")
else:
    st.sidebar.success("Sesión iniciada")
    st.title("Bienvenido a PowerUp 🎯")
    st.write("Selecciona una sección desde el menú izquierdo.")