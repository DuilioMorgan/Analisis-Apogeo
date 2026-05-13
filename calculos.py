import numpy as np
import lectura

tiempo, empuje = lectura.obtener_datos_curva()
tiempo_quemado = tiempo[-1] - tiempo[0]
masa_propelente = float(input("Masa del propelente en kg: "))

empuje_maximo = empuje.max()

impulso_total = np.trapezoid(empuje, tiempo)

empuje_medio = impulso_total/tiempo_quemado

impulso_especifico = impulso_total/(masa_propelente * 9.80665)

print("\nRESULTADOS DE LA PRUEBA ESTÁTICA")
print(f"Tiempo de Quemado del Motor {tiempo_quemado:.2f} ms")
print(f"Impulso Total (It): {impulso_total:.2f} N*s")
print(f"Empuje Máximo: {empuje_maximo:.2f} N")
print(f"Empuje Medio: {empuje_medio:.2f} N")
print(f"Impulso Especifico (Is): {impulso_especifico:.2f}")
