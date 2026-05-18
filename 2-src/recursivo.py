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


def resolver_recursivo(
    materias,
    salones,
    horarios,
    indice,
    asignaciones
):

    if indice >= len(materias):
        return

    materia = materias[indice]

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

                    resolver_recursivo(
                        materias,
                        salones,
                        horarios,
                        indice + 1,
                        asignaciones
                    )

                    return


# ==========================================
# PRUEBAS
# ==========================================

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

        asignaciones = []

        resolver_recursivo(
            materias,
            salones,
            horarios,
            0,
            asignaciones
        )

        print("HORARIO GENERADO\n")

        for r in asignaciones:

            print("Materia:", r["materia"])
            print("Profesor:", r["profesor"])
            print("Grupo:", r["grupo"])
            print("Salon:", r["salon"])
            print("Horario:", r["horario"])

            print("-----------------------")