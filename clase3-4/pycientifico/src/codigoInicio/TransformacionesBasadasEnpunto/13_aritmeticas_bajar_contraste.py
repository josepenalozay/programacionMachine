# Importamos librerias
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Leemos nuestra imagen
imagen = cv2.imread('../img/cepillo.png')
#imgBGR = cv2.imread('img/monedas.jpg')

# Dividir a la mitad la intensidad del brillo en cada canal
imagen_dividida = imagen // 2

# Mostrar la imagen original y la imagen con la intensidad dividida
cv2.imshow('Imagen Original', imagen)
cv2.imshow('Imagen con Intensidad Dividida', imagen_dividida)
cv2.waitKey(0)
cv2.destroyAllWindows()