import time
import json
import sys
import os


sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from lector_datos import cargar_datos

from greedy import greedy
from backtracking import backtracking


casos = [
    ("caso_prueba_pequeno.txt", 3, "Pequeno"),
    ("caso_prueba_mediano.txt", 8, "Mediano"),
    ("caso_prueba_grande.txt", 15, "Grande")
]


# lista para guardar resultados
resultados = []


print("=" * 75)
print("RESULTADOS ENTREGA 2 - GREEDY VS BACKTRACKING")
print("=" * 75)


for caso, cantidad, nombre_caso in casos:

    materias, salones, horarios, restricciones, preferencias = cargar_datos(
        caso
    )

    # =====================================
    # GREEDY
    # =====================================

    inicio = time.time()

    resultado_greedy = greedy(
        materias,
        salones,
        horarios
    )

    fin = time.time()

    tiempo_greedy = (fin - inicio) * 1000  # ms

    # =====================================
    # BACKTRACKING
    # =====================================

    asignaciones_backtracking = []

    inicio = time.time()

    backtracking(
        materias,
        salones,
        horarios,
        0,
        asignaciones_backtracking
    )

    fin = time.time()

    tiempo_backtracking = (fin - inicio) * 1000  # ms

    # =====================================
    # GUARDAR RESULTADOS
    # =====================================

    resultados.append({
        "caso": nombre_caso,
        "materias": cantidad,
        "greedy": tiempo_greedy,
        "backtracking": tiempo_backtracking
    })

    # =====================================
    # MOSTRAR RESULTADOS
    # =====================================

    print(f"\nCASO: {nombre_caso}")

    print(f"   Materias totales: {cantidad}")

    print(
        f"   Greedy:          "
        f"{len(resultado_greedy)} asignadas en "
        f"{tiempo_greedy:.4f} ms"
    )

    print(
        f"   Backtracking:    "
        f"{len(asignaciones_backtracking)} asignadas en "
        f"{tiempo_backtracking:.4f} ms"
    )


# =====================================
# GUARDAR JSON
# =====================================

with open(
    "2-src/comparativas/resultados_entrega2.json",
    "w"
) as archivo:

    json.dump(
        resultados,
        archivo,
        indent=4
    )


print("\nArchivo JSON generado correctamente.")