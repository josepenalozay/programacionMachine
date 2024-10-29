impuestos_por_mes = [100.0, 200.0, 100.0]

total_impuestos = 0.0

for indice in range(len(impuestos_por_mes)):
    total_impuestos+=impuestos_por_mes[indice]

print("total_impuestos: ", total_impuestos)

total_impuestos = 0.0
for impuesto_mensual in impuestos_por_mes:
    total_impuestos += impuesto_mensual

print("total impuestos: ", total_impuestos)

