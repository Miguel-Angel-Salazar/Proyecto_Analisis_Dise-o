import time
import sys
import os

# permitir importar archivos desde 2-src
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(_file_), "..")
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