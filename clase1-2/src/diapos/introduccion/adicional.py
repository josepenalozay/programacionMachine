# Leer el precio en soles
precio_soles = float(input("Ingrese el precio en soles: "))

# Leer la tasa de conversion
tasa_conversion = float(input("Ingrese la tasa: "))

# Convertir factor dolares
precio_dolares = precio_soles / tasa_conversion

# Mostrar el resultado
print(f"El precio en dólares es: ", str(precio_dolares))