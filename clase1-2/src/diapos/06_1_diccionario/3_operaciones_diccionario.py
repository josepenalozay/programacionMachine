notas_por_codigo = {"202401": 8.0,
                    "202402": 9.5,
                    "202403": 10.2}

print("202404" in notas_por_codigo)
notas_por_codigo["202404"] = 18.0

print("202404" in notas_por_codigo)
print(notas_por_codigo["202404"])

del(notas_por_codigo["202404"])
print("202404" in notas_por_codigo)
