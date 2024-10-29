una_variable = 10
otra_variable = 3

una_variable = otra_variable
otra_variable = una_variable
print("una_variable: ",una_variable)
print("otra_variable: ",otra_variable)

una_variable = 10
otra_variable = 3

(una_variable, otra_variable) = (otra_variable, una_variable)
print("una_variable: ",una_variable)
print("otra_variable: ",otra_variable)


def division_entera(dividendo,divisor):
    cociente = dividendo//divisor
    residuo = dividendo % divisor
    return (cociente, residuo)

print(division_entera(10,3))