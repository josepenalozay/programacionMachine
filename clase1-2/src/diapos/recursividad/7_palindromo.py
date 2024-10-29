def es_palindromo(frase):
    
    def pre_procesar(frase):
        frase = frase.lower()
        resultado = ''
        for letra in frase:
            if letra in 'abcdefghijklmnopqrstuvwxyz':
                resultado = resultado + letra
        return resultado

    def evaluar(frase):
        if len(frase) <= 1:
            return True
        else:
            return frase[0] == frase[-1] and evaluar(frase[1:-1])

    return evaluar(pre_procesar(frase))

print(es_palindromo("Yo hago yoga hoy."))