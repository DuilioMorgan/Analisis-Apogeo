import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class MotorPrometeo:
    def __init__(self, archivo, masa_propelente):
        # Streamlit manda el archivo directamente, así que lo recibimos aquí
        self.archivo = archivo
        self.masa_propelente = masa_propelente
        self.tiempo_s = None
        self.empuje_N = None
        self.resultados = {}
        
        # Leemos y limpiamos automáticamente
        self._leer_datos()
        
    def _leer_datos(self):
        datos = pd.read_csv(self.archivo, sep=None, engine='python', header=0)
        datos.columns = datos.columns.str.strip()

        datos["Tiempo(ms)"] = pd.to_numeric(
            datos["Tiempo(ms)"].astype(str).str.replace(',', '.').str.strip(), errors='coerce'
        )
        datos["Fuerza(kg)"] = pd.to_numeric(
            datos["Fuerza(kg)"].astype(str).str.replace(',', '.').str.strip(), errors='coerce'
        )
        datos = datos.dropna(subset=["Tiempo(ms)", "Fuerza(kg)"])

        # Conversión a segundos y Newtons
        self.tiempo_s = datos["Tiempo(ms)"].values / 1000.0
        self.empuje_N = datos["Fuerza(kg)"].values * 9.81

    def calcular_rendimiento(self):
        t_quemado = self.tiempo_s[-1] - self.tiempo_s[0]
        empuje_max = self.empuje_N.max()
        impulso_tot = np.trapezoid(self.empuje_N, self.tiempo_s)
        empuje_med = impulso_tot / t_quemado
        impulso_esp = impulso_tot / (self.masa_propelente * 9.80665)

        self.resultados = {
            "tb": t_quemado,
            "Fmax": empuje_max,
            "It": impulso_tot,
            "Favg": empuje_med,
            "Isp": impulso_esp
        }
        return self.resultados

    def generar_grafica(self):
        # En Streamlit no usamos plt.show(), sino que construimos la figura y la devolvemos
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(self.tiempo_s, self.empuje_N, color="#8C66D7", linewidth=2, label="Curva Prometeo III")
        ax.set_title("Análisis de Empuje Estático - Prometeo III", fontweight='bold')
        ax.set_xlabel("Tiempo (Segundos)")
        ax.set_ylabel("Fuerza (Newtons)")
        ax.grid(True, linestyle='--', alpha=0.7)
        ax.legend()
        fig.tight_layout()
        return fig