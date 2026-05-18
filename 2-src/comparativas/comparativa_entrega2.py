import time
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
    ("caso_prueba_pequeno.txt", 3),
    ("caso_prueba_mediano.txt", 8),
    ("caso_prueba_grande.txt", 15)
]


print("\n====================================")
print("COMPARATIVA ENTREGA 2")
print("====================================")

for caso, cantidad in casos:

    print("\nCaso:", caso)

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

    tiempo_greedy = fin - inicio

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

    tiempo_backtracking = fin - inicio

    # =====================================
    # RESULTADOS
    # =====================================

    print("\nCantidad de materias:", cantidad)

    print("\nGREEDY")
    print("Tiempo:", tiempo_greedy)
    print("Asignaciones:", len(resultado_greedy))

    print("\nBACKTRACKING")
    print("Tiempo:", tiempo_backtracking)
    print("Asignaciones:", len(asignaciones_backtracking))

    print("\n------------------------------------")