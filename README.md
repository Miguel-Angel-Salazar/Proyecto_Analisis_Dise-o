# Planificador de Horarios Universitarios

Proyecto de analisis y diseno de algoritmos para asignar materias a salones y horarios de manera optima, utilizando fuerza bruta, recursividad, greedy, backtracking y divide y venceras.

## Descripcion

Este proyecto resuelve el problema de planificacion de horarios universitarios mediante diferentes tecnicas algoritmicas. El sistema asigna materias (con profesor, grupo, alumnos y horas requeridas) a salones disponibles (con capacidad limitada) en horarios especificos, optimizando tres objetivos simultaneamente.

## Los 3 Subproblemas

El planificador resuelve los siguientes subproblemas:

### Subproblema 1: Evitar conflictos de horario
Garantizar que no existan superposiciones imposibles:
- **Conflicto de profesor**: Un profesor no puede dar dos clases al mismo tiempo
- **Conflicto de salon**: Un salon no puede albergar dos materias simultaneamente
- **Conflicto de grupo**: Un grupo no puede tener dos clases al mismo tiempo
- **Restricciones de disponibilidad**: Respetar los horarios bloqueados de cada profesor

### Subproblema 2: Maximizar el uso de salones
Optimizar la utilizacion de los recursos fisicos:
- **Minimizar salones ociosos**: Concentrar las clases en el menor numero de salones posible
- **Uso eficiente de capacidad**: Asignar materias a salones con capacidad adecuada (ni muy grande ni muy pequeno)
- **Balance de carga**: Distribuir las clases de manera uniforme cuando sea posible

### Subproblema 3: Respetar preferencias de horario
Satisfacer las preferencias de los profesores cuando sea posible:
- **Preferencias prioritarias**: Cada profesor puede indicar horarios preferidos con prioridad (alta, media, baja)
- **Puntaje de satisfaccion**: El sistema calcula un puntaje basado en cuantas preferencias se cumplen
- **Horarios deseados por materia**: Las materias pueden tener ventanas horarias preferidas

## Objetivo

Comparar distintas tecnicas algoritmicas para resolver un mismo problema de optimizacion multi-objetivo, evaluando su eficiencia, complejidad y calidad de solucion en los 3 subproblemas.


## Entradas del sistema

### Materias
| Campo | Descripcion | Relevancia para subproblemas |
|-------|-------------|------------------------------|
| Nombre | Identificador de la materia | - |
| Profesor | Profesor asignado | SP1: Evitar conflictos de profesor |
| Grupo | Grupo de estudiantes | SP1: Evitar conflictos de grupo |
| Alumnos | Cantidad de estudiantes | SP2: Seleccionar salon con capacidad adecuada |
| Horas requeridas | Duracion de la clase | SP2: Optimizar bloques de horario |
| Preferencia horaria | Ventana horaria deseada | SP3: Respetar preferencias |

### Salones
| Campo | Descripcion | Relevancia para subproblemas |
|-------|-------------|------------------------------|
| Nombre | Identificador del salon | SP1: Evitar conflictos de salon |
| Capacidad | Maximo de estudiantes | SP2: Uso eficiente de recursos |

### Horarios disponibles
Dia, hora de inicio y hora de fin para cada franja horaria.

### Restricciones de profesores
Profesor, dia y franja horaria en la que **no** esta disponible (SP1).

### Preferencias de profesores
Profesor, dia, franja horaria y prioridad (alta/media/baja) de su preferencia (SP3).

## Estructura del proyecto

```
planificador-horarios-universidad/
|
|___ 1-Datos/                       # Casos de prueba
|   |___ 1-caso_pequeno.txt            # 3 materias, 2 salones, 2 grupos
|   |___ 2-caso_mediano.txt            # 8 materias, 4 salones, 4 grupos
|   |___ 3-caso_grande.txt             # 15 materias, 6 salones, 6 grupos
|   |___ 4-caso_100.txt                # Template para 100 materias
|   |___ 5-caso_1000.txt               # Template para 1000 materias
|
|___ 2-Src/                         # Codigo fuente
|   |___ algoritmo_fuerza_bruta.py    
|   |___ algoritmo_recursivo.py         
|   |___ algoritmo_greedy.py           
|   |___ algoritmo_backtracking.py     
|   |___ algoritmo_divide_venceras.py  
|   |___ comparativa.py            # Comparativa de todos los algoritmos
|   |___ lector_datos.py            
|
|___ 3-Docs/                        # Documentacion
|   |___ entrega1.pdf
|   |___ entrega2.pdf
|   |___ entrega3_final.pdf                
|
|___ 4-Presentacion/                # Presentacion final
|   |___ presentacion_final.pdf        # Diapositivas (placeholder)
|
|___ .gitignore
|___ README.md
```

## Integrantes del equipo

- MIguel Ángel Guarnizo Salazar
- Juan Sebastián Villa Rodas
- Tomás Buriticá Jaramillo


