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


def fuerza_bruta(materias, salones, horarios):

    asignaciones = []

    for materia in materias:

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

                        break

                ya_asignada = False

                for a in asignaciones:

                    if a["materia"] == materia["nombre"]:
                        ya_asignada = True

                if ya_asignada:
                    break

    return asignaciones


casos = [
    "caso_prueba_pequeno.txt",
    "caso_prueba_mediano.txt",
    "caso_prueba_grande.txt",
    ]

for caso in casos:

    print("\n===================================")
    print("CASO:", caso)
    print("===================================\n")

    materias, salones, horarios, restricciones, preferencias = cargar_datos(
        caso
    )

    resultado = fuerza_bruta(
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