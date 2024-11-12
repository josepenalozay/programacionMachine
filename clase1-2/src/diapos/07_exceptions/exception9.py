def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError as e:
        print("Error: No se puede dividir por cero.")
    else:
        # Este bloque se ejecuta solo si no hay excepción
        print("La división fue exitosa. El resultado es:", resultado)

# Ejemplo de uso
dividir(10, 2)  # División sin errores, ejecuta el bloque else
dividir(10, 0)  # Genera ZeroDivisionError, no ejecuta el bloque else
