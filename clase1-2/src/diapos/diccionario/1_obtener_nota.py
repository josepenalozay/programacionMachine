def obtener_nota(codigo, lista_codigos, lista_nota):
    indice = lista_codigos.index(codigo)
    nota = lista_nota[indice]

    return (codigo, nota)
codigos = ["202401","202402","202403"]
notas = [8.0, 9.5, 10.2]

print(obtener_nota("202402", codigos, notas))