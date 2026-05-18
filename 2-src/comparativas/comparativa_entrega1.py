import time
import sys
import os

# permitir importar archivos desde 2-Src
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from lector_datos import cargar_datos

from fuerza_bruta import fuerza_bruta
from recursivo import resolver_recursivo


casos = [
    ("caso_prueba_pequeno.txt", 3),
    ("caso_prueba_mediano.txt", 8),
    ("caso_prueba_grande.txt", 15)
]


print("\n====================================")
print("COMPARATIVA ENTREGA 1")
print("====================================")


for caso, cantidad in casos:

    print("\nCaso:", caso)

    materias, salones, horarios, restricciones, preferencias = cargar_datos(
        caso
    )

    # =====================================
    # FUERZA BRUTA
    # =====================================

    inicio = time.time()

    resultado_fuerza_bruta = fuerza_bruta(
        materias,
        salones,
        horarios
    )

    fin = time.time()

    tiempo_fuerza_bruta = fin - inicio

    # =====================================
    # RECURSIVO
    # =====================================

    asignaciones_recursivo = []

    inicio = time.time()

    resolver_recursivo(
        materias,
        salones,
        horarios,
        0,
        asignaciones_recursivo
    )

    fin = time.time()

    tiempo_recursivo = fin - inicio

    # =====================================
    # RESULTADOS
    # =====================================

    print("\nCantidad de materias:", cantidad)

    print("\nFUERZA BRUTA")
    print("Tiempo:", tiempo_fuerza_bruta)
    print("Asignaciones:", len(resultado_fuerza_bruta))

    print("\nRECURSIVO")
    print("Tiempo:", tiempo_recursivo)
    print("Asignaciones:", len(asignaciones_recursivo))

    print("\n------------------------------------")