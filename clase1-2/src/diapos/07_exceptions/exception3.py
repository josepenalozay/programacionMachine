try:
    un_numero = int(input("Ingrese un numero:"))
    otro_numero = int(input("Ingrese otro numero:"))
    print("El conciente es: ",un_numero / otro_numero)

except ValueError:
    print("No es posible convertir factor un numero")
except ZeroDivisionError:
    print("No es posible dividir entre cero")
except:
    print("Error inesperado")
