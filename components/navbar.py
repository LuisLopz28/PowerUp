# components/navbar.py
import streamlit as st

def menu():
    return st.sidebar.radio("📂 Navegación", [
        "Inicio",
        "Simulador",
        "Estado de Resultado"
    ])
