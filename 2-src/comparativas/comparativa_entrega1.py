import time
import json
import sys
import os

# permitir importar archivos desde 2-src
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from lector_datos import cargar_datos
from fuerza_bruta import fuerza_bruta
from recursivo import resolver_recursivo


casos = [
    ("caso_prueba_pequeno.txt", 3, "Pequeno"),
    ("caso_prueba_mediano.txt", 8, "Mediano"),
    ("caso_prueba_grande.txt", 15, "Grande")
]


# lista donde se guardarán los resultados
resultados = []


print("=" * 75)
print("RESULTADOS ENTREGA 1 - FUERZA BRUTA VS RECURSIVIDAD")
print("=" * 75)


for caso, cantidad, nombre_caso in casos:

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

    tiempo_fuerza_bruta = (fin - inicio) * 1000  # ms

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

    tiempo_recursivo = (fin - inicio) * 1000  # ms

    # =====================================
    # GUARDAR RESULTADOS
    # =====================================

    resultados.append({
        "caso": nombre_caso,
        "materias": cantidad,
        "fuerza_bruta": tiempo_fuerza_bruta,
        "recursivo": tiempo_recursivo
    })

    # =====================================
    # MOSTRAR RESULTADOS
    # =====================================

    print(f"\nCASO: {nombre_caso}")

    print(f"   Materias totales: {cantidad}")

    print(
        f"   Fuerza Bruta: "
        f"{len(resultado_fuerza_bruta)} asignadas en "
        f"{tiempo_fuerza_bruta:.4f} ms"
    )

    print(
        f"   Recursividad: "
        f"{len(asignaciones_recursivo)} asignadas en "
        f"{tiempo_recursivo:.4f} ms"
    )


# =====================================
# GUARDAR JSON
# =====================================

with open(
    "2-src/comparativas/resultados_entrega1.json",
    "w"
) as archivo:

    json.dump(
        resultados,
        archivo,
        indent=4
    )


print("\nArchivo JSON generado correctamente.")