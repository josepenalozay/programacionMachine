def una_funcion(parametro):
    variable = 1
    variable +=1
    print("una funcion: variable=",variable)

def otra_funcion(parametro):
    print("otra funcion: variable=", variable)
    print("otra funcion: variable+1=", variable+1)

def la_funcion(parametro):
    variable+=1

variable = 5

una_funcion(variable)
print("variable =", variable)
otra_funcion(variable)
print("variable =", variable)
la_funcion(variable)