import traceback

def main():
    try:
        metodo_que_lanza_excepcion()
    except Exception as e:
        print("Se ha capturado una excepción en main:", str(e))
        traceback.print_exc()  # Imprime el stack trace de la excepción

def metodo_que_lanza_excepcion():
    try:
        # Código que puede lanzar una excepción
        resultado = 10 / 0  # Esto lanzará una excepción ZeroDivisionError
    except Exception as e:
        print("Error capturado en metodo_que_lanza_excepcion:", str(e))
        traceback.print_exc()  # Imprime el stack trace de la excepción
        raise  # Relanza la excepción para que sea manejada más arriba

if __name__ == "__main__":
    main()
