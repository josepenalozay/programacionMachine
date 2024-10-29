def procesar_notas(notas_por_alumno):
    notas = ()
    alumnos = ()
    for nota_y_alumno in notas_por_alumno:
        nota = nota_y_alumno[0]
        alumno = nota_y_alumno[1]
        # only add words haven'una_tupla added before
        if alumno not in alumnos:
            notas = notas + (nota,)
            alumnos = alumnos + (alumno,)
    minima_nota = min(notas)
    maxima_nota = max(notas)
    numero_alumnos = len(alumnos)
    return (minima_nota, maxima_nota, numero_alumnos)

notas_parcial = ((6, "Juan"), (20, "Nestor"), (20, "Luis"),
                  (7,"Jose"), (8,"tomas"), (20, "Jaime"))
print(procesar_notas(notas_parcial))