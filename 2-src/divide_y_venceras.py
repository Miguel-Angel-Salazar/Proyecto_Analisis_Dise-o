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
    resultado = solucion_izquierda + solucion_derecha

    return resultado


# =====================================
# PRUEBAS
# =====================================

if __name__ == "__main__":

    casos = [
        "caso_prueba_pequeno.txt",
        "caso_prueba_mediano.txt",
        "caso_prueba_grande.txt"
    ]

    for caso in casos:

        print("\n===================================")
        print("CASO:", caso)
        print("===================================\n")

        materias, salones, horarios, restricciones, preferencias = cargar_datos(
            caso
        )

        resultado = divide_y_venceras(
            materias,
            salones,
            horarios
        )

        print("HORARIO GENERADO\n")

        for r in resultado:

            print("Materia:", r["materia"])
            print("Profesor:", r["profesor"])
            print("Grupo:", r["grupo"])
            print("Salon:", r["salon"])
            print("Horario:", r["horario"])

            print("-----------------------")