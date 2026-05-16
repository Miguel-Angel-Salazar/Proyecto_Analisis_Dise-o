
# ANALISIS DE COMPLEJIDAD - ALGORITMO FUERZA BRUTA


# Complejidad temporal:
#
# El algoritmo realiza:
#
# 1. Recorrido de todas las materias
#
#       O(m)
#
# 2. Para cada materia se recorren los salones
#
#       O(s)
#
# 3. Para cada salon se recorren todos los horarios
#
#       O(h)
#
# 4. Para cada combinacion se revisan conflictos
#
#       O(m)
#
# ya que la lista de asignaciones puede crecer hasta
# aproximadamente el numero de materias.
#
# Entonces:
#
# O(m) × O(s) × O(h) × O(m)
#
# Resultado:
#
# O(m²sh)
#
#
# donde:

# m = numero de materias
# s = numero de salones
# h = numero de horarios


# Complejidad espacial:
#
# El algoritmo almacena una lista de asignaciones:
#
# asignaciones = []
#
# En el peor caso:
#
# len(asignaciones) = m
#
# por lo tanto:
#
# O(m)
#


import os
import time
import inspect
import importlib.util
import matplotlib.pyplot as plt


def cargar_modulo_desde_archivo(ruta_archivo, nombre_modulo):
    spec = importlib.util.spec_from_file_location(nombre_modulo, ruta_archivo)
    if spec is None or spec.loader is None:
        raise ImportError(f"No se pudo cargar el módulo desde {ruta_archivo}")
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def obtener_funcion_algoritmo(modulo, nombre_funcion=None):
    if nombre_funcion is not None and hasattr(modulo, nombre_funcion):
        return getattr(modulo, nombre_funcion)
    posibles = [
        "fuerza_bruta",
        "recursivo",
        "greedy",
        "backtracking",
        "divide_y_venceras",
        "resolver",
        "algoritmo"
    ]
    for nombre in posibles:
        if hasattr(modulo, nombre):
            return getattr(modulo, nombre)
    raise AttributeError(f"No se encontró una función de algoritmo conocida en {modulo.__file__}")


def ejecutar_algoritmo(funcion, materias, salones, horarios, restricciones, preferencias):
    firma = inspect.signature(funcion)
    parametros = len(firma.parameters)

    if parametros == 3:
        return funcion(materias, salones, horarios)
    if parametros == 5:
        return funcion(materias, salones, horarios, restricciones, preferencias)
    if parametros == 4:
        return funcion(materias, salones, horarios, restricciones)
    if parametros == 2:
        return funcion(materias, salones)

    raise TypeError(
        f"Firma de función inesperada ({parametros} parámetros) para {funcion.__name__}"
    )


# =======================================
# Configuración de archivos de datos
# =======================================

CASOS = [
    ("caso_prueba_pequeno.txt", 3),
    ("caso_prueba_mediano.txt", 8),
    ("caso_prueba_grande.txt", 15),
    ("caso_100.txt", 100),
    ("caso_1000.txt", 1000)
]


# =======================================
# Directorios
# =======================================

BASE_DIR = os.path.dirname(__file__)
DATOS_DIR = os.path.normpath(os.path.join(BASE_DIR, "..", "1-datos"))
ALG_DIR = BASE_DIR


# =======================================
# Cargar datos
# =======================================

lector_path = os.path.join(ALG_DIR, "lector_datos.py")
lector_mod = cargar_modulo_desde_archivo(lector_path, "lector_datos")
cargar_datos = lector_mod.cargar_datos


# =======================================
# Algoritmos disponibles
# =======================================

algoritmos = [
    ("1-fuerza_bruta.py", "fuerza_bruta")
]


def medir_algoritmos():
    resultados = []

    for nombre_archivo_algoritmo, nombre_funcion in algoritmos:
        ruta_modulo = os.path.join(ALG_DIR, nombre_archivo_algoritmo)

        try:
            modulo = cargar_modulo_desde_archivo(ruta_modulo, nombre_archivo_algoritmo.replace(".py", ""))
            funcion = obtener_funcion_algoritmo(modulo, nombre_funcion)
        except Exception as e:
            print(f"No se pudo cargar {nombre_archivo_algoritmo}: {e}")
            continue

        tiempos = []
        tamanos = []

        print(f"\nMEDICIÓN - {nombre_archivo_algoritmo}\n")

        for archivo, cantidad in CASOS:
            ruta_datos = os.path.join(DATOS_DIR, archivo)
            try:
                materias, salones, horarios, restricciones, preferencias = cargar_datos(archivo)
                inicio = time.time()
                ejecutar_algoritmo(funcion, materias, salones, horarios, restricciones, preferencias)
                fin = time.time()
                tiempo_total = fin - inicio
                tiempos.append(tiempo_total)
                tamanos.append(cantidad)
                print("Caso:", archivo)
                print("Materias:", cantidad)
                print("Tiempo:", round(tiempo_total, 6), "segundos")
                print("--------------------------")
            except Exception as e:
                print("Error:", archivo)
                print(e)

        resultados.append((nombre_archivo_algoritmo, tamanos, tiempos))

    return resultados


# =======================================
# Generar gráfico
# =======================================

if __name__ == "__main__":
    resultados = medir_algoritmos()

    if not resultados:
        print("No hay algoritmos válidos para medir.")
    else:
        for nombre_alg, tamanos, tiempos in resultados:
            plt.plot(tamanos, tiempos, label=nombre_alg)

        plt.xlabel("Tamaño de entrada (materias)")
        plt.ylabel("Tiempo (segundos)")
        plt.title("Tiempo vs Tamaño de entrada - Algoritmos disponibles")
        plt.legend()
        plt.grid()
        plt.show()