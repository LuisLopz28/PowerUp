# pages/simulador.py
import streamlit as st

def app():
    st.title("🧮 Simulador de Facturación")
    precio_unitario = st.number_input("Precio unitario", min_value=0.0, value=100.0)
    cantidad = st.slider("Cantidad vendida", 0, 1000, 50)
    ingresos = precio_unitario * cantidad

    st.metric("Total Facturado", f"${ingresos:,.2f}")
