from lector_datos import cargar_datos


# función para revisar si hay conflictos
def hay_conflicto(asignaciones, profesor, grupo, salon, horario):

    for a in asignaciones:

        # mismo salón y mismo horario
        if a["salon"] == salon and a["horario"] == horario:
            return True

        # mismo profesor y mismo horario
        if a["profesor"] == profesor and a["horario"] == horario:
            return True

        # mismo grupo y mismo horario
        if a["grupo"] == grupo and a["horario"] == horario:
            return True

    return False


# algoritmo de fuerza bruta
def fuerza_bruta(materias, salones, horarios):

    asignaciones = []

    # recorrer materias
    for materia in materias:

        # probar todos los salones
        for salon in salones:

            # validar capacidad
            if salon["capacidad"] >= materia["alumnos"]:

                # probar todos los horarios
                for horario in horarios:

                    conflicto = hay_conflicto(
                        asignaciones,
                        materia["profesor"],
                        materia["grupo"],
                        salon["nombre"],
                        horario
                    )

                    # si no hay conflicto se asigna
                    if conflicto == False:

                        nueva = {
                            "materia": materia["nombre"],
                            "profesor": materia["profesor"],
                            "grupo": materia["grupo"],
                            "salon": salon["nombre"],
                            "horario": horario
                        }

                        asignaciones.append(nueva)

                        # salir del horario
                        break

                # si ya se asignó, salir del salón
                ya_asignada = False

                for a in asignaciones:

                    if a["materia"] == materia["nombre"]:
                        ya_asignada = True

                if ya_asignada:
                    break

    return asignaciones


# ============================
# PROGRAMA PRINCIPAL
# ============================

materias, salones, horarios, restricciones, preferencias = cargar_datos(
    "caso_prueba_pequeno.txt"
)

resultado = fuerza_bruta(
    materias,
    salones,
    horarios
)

print("\nHORARIO GENERADO\n")

for r in resultado:

    print("Materia:", r["materia"])
    print("Profesor:", r["profesor"])
    print("Grupo:", r["grupo"])
    print("Salon:", r["salon"])
    print("Horario:", r["horario"])

    print("-----------------------")