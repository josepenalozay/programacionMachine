total = 0
for numero in range(5, 11, 2):
   print("numero: ", numero)
   total += numero
   if total == 5:
      break
      total += 1
print("total: ",total)