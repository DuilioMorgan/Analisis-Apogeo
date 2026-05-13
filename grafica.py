import matplotlib.pyplot as plt
import lectura

tiempo, empuje_N = lectura.obtener_datos_curva()

def graficar_empuje(t, e):
    plt.figure(figsize=(10,5))
    plt.plot(tiempo, empuje_N, color="#8C66D7", linewidth = 2, label = "Curva de Empuje")
    plt.title("Análisis de Empuje Estático - Prometeo III")
    plt.xlabel("Tiempo (ms)")
    plt.ylabel("Fuerza (N)")
    plt.grid(True)
    plt.legend()
    plt.show()

graficar_empuje(tiempo, empuje_N)