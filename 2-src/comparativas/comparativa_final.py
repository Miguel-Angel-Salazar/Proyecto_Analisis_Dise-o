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
from divide_y_venceras import divide_y_venceras


casos = [
    ("caso_prueba_pequeno.txt", 3, "Pequeno"),
    ("caso_prueba_mediano.txt", 8, "Mediano"),
    ("caso_prueba_grande.txt", 15, "Grande")
]


# lista para guardar resultados
resultados = []


print("=" * 75)
print("RESULTADOS ENTREGA FINAL - DIVIDE Y VENCERAS")
print("=" * 75)


for caso, cantidad, nombre_caso in casos:

    materias, salones, horarios, restricciones, preferencias = cargar_datos(
        caso
    )

    # =====================================
    # DIVIDE Y VENCERAS
    # =====================================

    inicio = time.time()

    resultado_divide_venceras = divide_y_venceras(
        materias,
        salones,
        horarios
    )

    fin = time.time()

    tiempo_divide_venceras = (fin - inicio) * 1000  # ms

    # =====================================
    # GUARDAR RESULTADOS
    # =====================================

    resultados.append({
        "caso": nombre_caso,
        "materias": cantidad,
        "divide_venceras": tiempo_divide_venceras
    })

    # =====================================
    # MOSTRAR RESULTADOS
    # =====================================

    print(f"\nCASO: {nombre_caso}")

    print(f"   Materias totales: {cantidad}")

    print(
        f"   Divide y Venceras: "
        f"{len(resultado_divide_venceras)} asignadas en "
        f"{tiempo_divide_venceras:.4f} ms"
    )


# =====================================
# GUARDAR JSON
# =====================================

with open(
    "2-src/comparativas/resultados_final.json",
    "w"
) as archivo:

    json.dump(
        resultados,
        archivo,
        indent=4
    )


print("\nArchivo JSON generado correctamente.")