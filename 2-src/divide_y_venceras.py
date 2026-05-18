from lector_datos import cargar_datos


def hay_conflicto(asignaciones, profesor, grupo, salon, horario):

    for a in asignaciones:

        if a["salon"] == salon and a["horario"] == horario:
            return True

        if a["profesor"] == profesor and a["horario"] == horario:
            return True

        if a["grupo"] == grupo and a["horario"] == horario:
            return True

    return False


def asignar_materias(materias, salones, horarios):

    asignaciones = []

    for materia in materias:

        asignada = False

        for salon in salones:

            if salon["capacidad"] >= materia["alumnos"]:

                for horario in horarios:

                    conflicto = hay_conflicto(
                        asignaciones,
                        materia["profesor"],
                        materia["grupo"],
                        salon["nombre"],
                        horario
                    )

                    if conflicto == False:

                        nueva = {
                            "materia": materia["nombre"],
                            "profesor": materia["profesor"],
                            "grupo": materia["grupo"],
                            "salon": salon["nombre"],
                            "horario": horario
                        }

                        asignaciones.append(nueva)

                        asignada = True

                        break

            if asignada:
                break

    return asignaciones


def divide_y_venceras(materias, salones, horarios):

    # caso base
    if len(materias) <= 2:

        return asignar_materias(
            materias,
            salones,
            horarios
        )

    # dividir
    mitad = len(materias) // 2

    izquierda = materias[:mitad]
    derecha = materias[mitad:]

    # vencer
    solucion_izquierda = divide_y_venceras(
        izquierda,
        salones,
        horarios
    )

    solucion_derecha = divide_y_venceras(
        derecha,
        salones,
        horarios
    )

    # combinar
    resultado = solucion_izquierda.copy()

    for materia in solucion_derecha:

        conflicto = hay_conflicto(
            resultado,
            materia["profesor"],
            materia["grupo"],
            materia["salon"],
            materia["horario"]
        )

        if conflicto == False:

            resultado.append(materia)

    return resultado


