def fibonacci_mejorado(numero, buffer):
    if numero in buffer:
        return buffer[numero]
    else:
        resultado = fibonacci_mejorado(numero - 1, buffer) \
                  + fibonacci_mejorado(numero - 2, buffer)
        buffer[numero] = resultado
        return resultado

buffer = {0: 1,
          1: 1}
print(fibonacci_mejorado(6, buffer))