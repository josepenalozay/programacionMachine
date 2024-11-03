def incluir_promedio(nota_practicas):
    notas_promedio = []
    for alumno_notas in nota_practicas:
        alumno = alumno_notas[0]
        notas = alumno_notas[1]
        notas_promedio.append([
            alumno,
            notas,
            calcular_promedio(notas)]
        )
    return notas_promedio


def calcular_promedio(grades):
        return sum(grades) / len(grades)


notas_algo = [[['Paolo', 'Guerrero'], [10, 10, 10]],
              [['Andres', 'Hurtado'], [10, 5, 12]],
              [['Waldir', 'Saenz'], []]]

print(incluir_promedio(notas_algo))
