import json
import matplotlib.pyplot as plt


# =========================================
# LEER RESULTADOS ENTREGA 1
# =========================================

with open(
    "2-src/comparativas/resultados_entrega1.json",
    "r"
) as archivo:

    datos_entrega1 = json.load(archivo)


materias = []
tiempos_fuerza_bruta = []
tiempos_recursivo = []


for dato in datos_entrega1:

    materias.append(dato["materias"])

    tiempos_fuerza_bruta.append(dato["fuerza_bruta"])

    tiempos_recursivo.append(dato["recursivo"])


# =========================================
# GRAFICA FUERZA BRUTA VS RECURSIVO
# =========================================

plt.figure()

plt.plot(
    materias,
    tiempos_fuerza_bruta,
    marker="o",
    label="Fuerza Bruta"
)

plt.plot(
    materias,
    tiempos_recursivo,
    marker="o",
    label="Recursivo"
)

plt.xlabel("Cantidad de materias")
plt.ylabel("Tiempo de ejecucion (ms)")

plt.title("Comparativa Fuerza Bruta vs Recursivo")

plt.legend()

plt.grid(True)

plt.savefig(
    "4-graficas/fuerza_bruta_vs_recursivo.png"
)

plt.show()