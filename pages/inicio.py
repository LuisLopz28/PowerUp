# pages/inicio.py
import streamlit as st

def app():
    st.title("🚀 PowerUp - Soluciones Digitales")
    st.markdown("""
    <h3>Misión</h3>
    <p>Impulsamos decisiones inteligentes a través de soluciones digitales como tableros Power BI, análisis de datos y más.</p>

    <h3>Servicios</h3>
    <ul>
        <li>📊 Desarrollo de dashboards</li>
        <li>📈 Análisis de datos</li>
        <li>🧮 Simuladores Python</li>
        <li>📑 Estados Financieros Inteligentes</li>
    </ul>
    """, unsafe_allow_html=True)
