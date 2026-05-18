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

with open(
    "2-src/comparativas/resultados_entrega2.json",
    "r"
) as archivo:

    datos_entrega2 = json.load(archivo)


materias = []
tiempos_greedy = []
tiempos_backtracking = []


for dato in datos_entrega2:

    materias.append(dato["materias"])

    tiempos_greedy.append(dato["greedy"])

    tiempos_backtracking.append(dato["backtracking"])


# GRAFICA GREEDY VS BACKTRACKING


plt.figure()

plt.plot(
    materias,
    tiempos_greedy,
    marker="o",
    label="Greedy"
)

plt.plot(
    materias,
    tiempos_backtracking,
    marker="o",
    label="Backtracking"
)

plt.xlabel("Cantidad de materias")
plt.ylabel("Tiempo de ejecucion (ms)")

plt.title("Comparativa Greedy vs Backtracking")

plt.legend()

plt.grid(True)

plt.savefig(
    "4-graficas/greedy_vs_backtracking.png"
)

plt.show()