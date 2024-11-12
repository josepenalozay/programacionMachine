import traceback

def main():
    try:
        # Código que puede lanzar una excepción
        resultado = 10 / 0  # Esto lanzará una excepción ZeroDivisionError
    except Exception as e:
        # Manejo de la excepción
        print("Se ha producido un error:", str(e))
        traceback.print_exc()  # Imprime el stack trace de la excepción

if __name__ == "__main__":
    main()
