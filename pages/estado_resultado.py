# pages/estado_resultado.py
import streamlit as st
import pandas as pd

def app():
    st.title("📑 Transformar Estado de Resultado")

    archivo = st.file_uploader("Carga tu archivo Excel", type=["xlsx"])
    if archivo:
        df = pd.read_excel(archivo)
        st.write("📄 Datos cargados:")
        st.dataframe(df.head())

        # Simulación de transformación
        if 'Ingreso' in df.columns and 'Gasto' in df.columns:
            df['Utilidad'] = df['Ingreso'] - df['Gasto']
            st.success("Transformación exitosa")
            st.dataframe(df)
