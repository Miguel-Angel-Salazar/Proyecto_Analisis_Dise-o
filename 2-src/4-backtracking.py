
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

def backtracking(materias, salones, horarios, indice, asignaciones):

    if indice >= len(materias):
        return True