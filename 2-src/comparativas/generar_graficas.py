import matplotlib.pyplot as plt


# tamaños de entrada
materias = [3, 8, 15]

# tiempos fuerza bruta
tiempos_fuerza_bruta = [
    7.3909759521484375e-06,
    2.09808349609375e-05,
    0.0002028942108154297
]

# tiempos recursivo
tiempos_recursivo = [
    5.4836273193359375e-06,
    1.71661376953125e-05,
    0.0001533031463623047
]


# =========================================
# GRAFICA COMPARATIVA
# =========================================

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
plt.ylabel("Tiempo de ejecucion (segundos)")

plt.title("Comparativa Fuerza Bruta vs Recursivo")

plt.legend()

plt.grid(True)

# guardar imagen
plt.savefig(
    "4-graficas/fuerza_bruta_vs_recursivo.png"
)

# mostrar grafica
plt.show()