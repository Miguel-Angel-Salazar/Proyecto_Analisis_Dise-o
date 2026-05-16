
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
#
# m = numero de materias
# s = numero de salones
# h = numero de horarios


