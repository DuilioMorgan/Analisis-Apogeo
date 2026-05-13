import pandas as pd

def obtener_datos_curva():
    datos = pd.read_csv("DATOS.CSV", sep=None, engine='python', header=0)
    
    datos.columns = datos.columns.str.strip()

    datos["Tiempo(ms)"] = pd.to_numeric(
        datos["Tiempo(ms)"].astype(str).str.replace(',', '.').str.strip(),
        errors='coerce'
    )
    datos["Fuerza(kg)"] = pd.to_numeric(
        datos["Fuerza(kg)"].astype(str).str.replace(',', '.').str.strip(),
        errors='coerce'
    )

    datos = datos.dropna(subset=["Tiempo(ms)", "Fuerza(kg)"])

    tiempo_ms = datos["Tiempo(ms)"].values
    empuje_kg = datos["Fuerza(kg)"].values
    empuje_N = empuje_kg * 9.81

    return tiempo_ms, empuje_N