# Demo para leer imagenes para imagenes a color 
#   - El orden normal es RGB
#   - Pero opencv usa el orden BGR
# https://www.pyimagesearch.com/2014/11/03/display-matplotlib-rgb-image/

#-----------------------------#
# 1. IMPORTAMOS LIBRERIAS
#-----------------------------#
import cv2    # Opencv
import sys    #
import matplotlib.pyplot as plt
plt.close('all') # Cierra figuras

#-----------------------------#
# 2. LEEMOS LA IMAGEN
#-----------------------------#
#  2.1. LEEMOS LA IMAGEN

img = cv2.imread('../img/imagenRGB.png',
                 cv2.IMREAD_COLOR)

#img = cv2.imread('lena.png',
#                 cv2.IMREAD_COLOR)
# Chequeamos si ha cargado la imagen
if img is None:
    print('La imagen no existe. Revise el path')
    sys.exit()  # Finaliza python
#  2.2. MOSTRAMOS PROPIEDADES
print("---")
print("Propiedades de la imagen")
print("  tipo de variable:", type(img))
print("  tipo de pixel:", img.dtype)
print("  tamaño:", img.shape)  # (rows,cols)
#  2.3. MOSTRAMOS LA IMAGEN
plt.figure()
#plt.imshow(img) # Esto no plotea bien por el formato 
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))


#-----------------------------#
# 3. ANALIZAMOS CADA CANAL
#-----------------------------#
#  3.1. PARTIMOS LA IMAGEN EN CADA CANAL
b,g,r = cv2.split(img)
#  3.2. MOSTRAMOS CADA CANAL
#   -> Canal Blue 
plt.figure()
plt.title('canal B')
plt.imshow(b, cmap='gray')
#   -> Canal Green 
plt.figure()
plt.title('canal G')
plt.imshow(g, cmap='gray')
#   -> Canal Red 
#plt.figure()
#plt.title('canal R')
#plt.imshow(r, cmap='gray')
plt.show()

#cv2.imshow("b",b)
#cv2.imshow("g",g)
#cv2.imshow("r",r)
#cv2.waitKey(0)

print("Hola")
print("Hola")
