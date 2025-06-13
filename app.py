# app.py
import streamlit as st
from auth.login import login
from components.navbar import menu
from pages import inicio, simulador, estado_resultado

# Cargar CSS
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Login
login()

# Navegación
opcion = menu()

if opcion == "Inicio":
    inicio.app()
elif opcion == "Simulador":
    simulador.app()
elif opcion == "Estado de Resultado":
    estado_resultado.app()
