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


def greedy(materias, salones, horarios):

    asignaciones = []

    # ordenar materias por cantidad de alumnos
    materias_ordenadas = sorted(
        materias,
        key=lambda x: x["alumnos"],
        reverse=True
    )

    for materia in materias_ordenadas:

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


