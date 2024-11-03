def una_funcion(parametro):
    variable = 1
    variable +=1
    print("una 04_funcion: variable=",variable)

def otra_funcion(parametro):
    print("otra 04_funcion: variable=", variable)
    print("otra 04_funcion: variable+1=", variable+1)

def la_funcion(parametro):
    variable+=1

variable = 5

una_funcion(variable)
print("variable =", variable)
otra_funcion(variable)
print("variable =", variable)
la_funcion(variable)