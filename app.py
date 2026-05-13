import streamlit as st
from logica_motor import MotorPrometeo

import streamlit as st

st.set_page_config(page_title="Análisis Apogeo", page_icon="🚀", layout="centered")

st.image("LogoApogeo.jpeg", use_container_width=True)

st.title("Software de Análisis - Apogeo")
st.markdown("Analisis de datos en crudo para obtener rendimiento de motor")

st.divider()

st.markdown("""
    <style>
    div.stButton > button {
        background-color: #8C66D7 !important;
        color: white !important;
        border: none !important;
        font-weight: bold !important;
    }
    div.stButton > button:hover {
        background-color: #714ebd !important;
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

st.divider()

archivo_csv = st.file_uploader("1. Sube tu archivo DATOS.CSV", type=["csv"])
masa = st.number_input("2. Masa del Propelente (kg):", min_value=0.001, value=0.150, step=0.010, format="%.3f")

if st.button("Calcular Rendimiento", type="primary"):
    if archivo_csv is not None:
        try:
            motor = MotorPrometeo(archivo=archivo_csv, masa_propelente=masa)
            res = motor.calcular_rendimiento()

            st.success("Datos procesados de manera correcta")

            st.subheader("Resultados de la Prueba Estática")
            
            col1, col2, col3 = st.columns(3)
            col1.metric("Tiempo de Quemado", f"{res['tb']:.3f} s")
            col2.metric("Impulso Total (It)", f"{res['It']:.2f} N·s")
            col3.metric("Empuje Máximo", f"{res['Fmax']:.2f} N")

            col4, col5 = st.columns(2)
            col4.metric("Empuje Medio (Favg)", f"{res['Favg']:.2f} N")
            col5.metric("Impulso Específico (Isp)", f"{res['Isp']:.2f} s")

            st.divider()

            st.subheader("Curva de Empuje")
            figura = motor.generar_grafica()
            st.pyplot(figura)

        except Exception as e:
            st.error(f"Ocurrió un error matemático o de lectura: {e}")
    else:
        st.warning("¡Olvidaste subir el archivo CSV!")
