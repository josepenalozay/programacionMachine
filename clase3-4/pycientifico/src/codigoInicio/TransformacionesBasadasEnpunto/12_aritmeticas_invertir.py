# Importamos librerias
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Leemos nuestra imagen
imgBGR = cv2.imread('../img/cepillo.png')
#imgBGR = cv2.imread('img/monedas.jpg')

imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)

# Convertimos a EDG
imgGray = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2GRAY)

# Creamos una matriz del tamaño de la IMG
factor = 255
matrizGray = np.ones(imgGray.shape, dtype='uint8') * factor
matrizBGR = np.ones(imgBGR.shape, dtype='uint8') * factor


# Disminuimos el brillo en RGB
oscuraBRG = cv2.subtract(matrizBGR,  imgBGR)
oscuraRGB = cv2.cvtColor(oscuraBRG, cv2.COLOR_BGR2RGB)


# Mostramos la imagen
cv2.imshow('IMAGEN ORIGINAL', imgBGR)

cv2.imshow('IMAGEN OSCURA RGB', oscuraBRG)
cv2.waitKey(0)