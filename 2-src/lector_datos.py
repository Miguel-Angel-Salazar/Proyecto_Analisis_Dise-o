import os


def cargar_datos(nombre_archivo):

    # ruta base del archivo actual
    ruta_base = os.path.dirname(__file__)

    # construir ruta completa hacia 1-datos
    ruta_archivo = os.path.join(
        ruta_base,
        "..",
        "1-datos",
        nombre_archivo
    )

    materias = []
    salones = []
    horarios = []
    restricciones = []
    preferencias = []

    seccion = ""

    # abrir archivo
    with open(ruta_archivo, "r", encoding="utf-8") as archivo:

        # recorrer línea por línea
        for linea in archivo:

            linea = linea.strip()

            # ignorar líneas vacías
            if linea == "":
                continue

            # ignorar comentarios
            if linea.startswith("#"):
                continue

            # =========================
            # DETECTAR SECCIONES
            # =========================

            if linea == "MATERIAS":
                seccion = "materias"
                continue

            elif linea == "SALONES":
                seccion = "salones"
                continue

            elif linea == "HORARIOS_DISPONIBLES":
                seccion = "horarios"
                continue

            elif linea == "RESTRICCIONES_PROFESORES":
                seccion = "restricciones"
                continue

            elif linea == "PREFERENCIAS_PROFESORES":
                seccion = "preferencias"
                continue

            # =========================
            # LEER MATERIAS
            # =========================

            if seccion == "materias":

                datos = linea.split("|")

                materia = {
                    "nombre": datos[0],
                    "profesor": datos[1],
                    "grupo": datos[2],
                    "alumnos": int(datos[3]),
                    "horas": int(datos[4]),
                    "preferencia": datos[5]
                }

                materias.append(materia)

            # =========================
            # LEER SALONES
            # =========================

            elif seccion == "salones":

                datos = linea.split("|")

                salon = {
                    "nombre": datos[0],
                    "capacidad": int(datos[1])
                }

                salones.append(salon)

            # =========================
            # LEER HORARIOS
            # =========================

            elif seccion == "horarios":

                horarios.append(linea)

            # =========================
            # LEER RESTRICCIONES
            # =========================

            elif seccion == "restricciones":

                restricciones.append(linea)

            # =========================
            # LEER PREFERENCIAS
            # =========================

            elif seccion == "preferencias":

                preferencias.append(linea)

    return (
        materias,
        salones,
        horarios,
        restricciones,
        preferencias
    )