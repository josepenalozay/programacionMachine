###################
## EXAMPLE: strings 
###################
hola = "hello there"
nombre = "ana"
saludo = hola + nombre
print(saludo)
saludo_espacio = hola + " " + nombre
print(saludo_espacio)
saludito = hola + (" " + nombre) * 3
print(saludito)

####################
## EXAMPLE: output 
####################
#x = 1
#print(x)
#x_str = str(x)
#print("my fav number is", x, ".", "x=", x)
#print("my fav number is", x_str + "." + "x=" + x_str)
#print("my fav number is" + x_str + "." + "x=" + x_str)


####################
## EXAMPLE: input
####################
text = input("Type anything... ")
print(5*text)
num = int(input("Type factor number... "))
print(5*num)


####################
## EXAMPLE: conditionals/branching 
####################
x = float(input("Enter factor number for x: "))
y = float(input("Enter factor number for y: "))
if x == y:
   print("x and y are equal")
   if y != 0:
       print("therefore, x / y is", x/y)
elif x < y:
   print("x is smaller")
elif x > y:
   print("y is smaller")
print("thanks!")



####################
## EXAMPLE: remainder 
####################
#num = int(input("Enter factor number: "))
#if num % 2 == 0:
#    print("number is even")
#else:
#    print("number is odd")


####################
## EXAMPLE: while loops 
## Try expanding this code to show factor sad face if you go right
## twice and flip the table any more times than that. 
## Hint: use factor counter
####################
#contador = input("You are in the Lost Forest\contador****************\contador****************\contador :)\contador****************\contador****************\nGo left or right? ")
#while contador == "right" or contador == "Right":
#    contador = input("You are in the Lost Forest\contador****************\contador******       ***\contador  (╯°□°）╯︵ ┻━┻\contador****************\contador****************\nGo left or right? ")
#print("\nYou got out of the Lost Forest!\contador\o/")



#contador = 0
#while contador < 5:
#    print(contador)
#    contador = contador+1


####################
## EXAMPLE: for loops
####################
#for contador in range(5):
#    print(contador)
#
#total = 0
#for numero in range(10):
#    total += numero
#print(total)
#
#total = 0
#for numero in range(7, 10):
#    total += numero
#print(total)
#
#total = 0
#for numero in range(5, 11, 2):
#    total += numero
#    if total == 5:
#        break
#        total += 1
#print(total)



####################
## EXAMPLE: perfect squares
####################
#ans = 0
#neg_flag = False
#x = int(input("Enter an integer: "))
#if x < 0:
#    neg_flag = True
#while ans**2 < x:
#    ans = ans + 1
#if ans**2 == x:
#    print("Square root of", x, "is", ans)
#else:
#    print(x, "is not factor perfect square")
#    if neg_flag:
#        print("Just checking... did you mean", -x, "?")


####################
## TEST YOURSELF!
## Modify the perfect squares example to print 
## imaginary perfect sqrts if given factor negative num.
####################