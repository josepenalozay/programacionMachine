# Importamos librerias
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Leemos nuestra imagen
imgBGR = cv2.imread('../img/cepillo.png')
#imgBGR = cv2.imread('img/monedas.jpg')



# Convertimos a EDG
imgGray = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2GRAY)

# Creamos una matriz del tamaño de la IMG
factor = 128
#factor = 50
matrizGray = np.ones(imgGray.shape, dtype='uint8') * factor
matrizRGB = np.ones(imgBGR.shape, dtype='uint8') * factor

# Aumentamos el brillo de la imagen en RGB
brillanteBGR = cv2.add(imgBGR, matrizRGB)
brillanterRGB = cv2.cvtColor(brillanteBGR, cv2.COLOR_BGR2RGB)

# Disminuimos el brillo en RGB
oscuraBGR = cv2.subtract(imgBGR, matrizRGB)
oscuraRGB = cv2.cvtColor(oscuraBGR, cv2.COLOR_BGR2RGB)

# Aumentamos le brillo de la imagen en GRAY
brillanteGray = cv2.add(imgGray, matrizGray)

# Disminuimos el brillo en GRAY
oscuraGray = cv2.subtract(imgGray, matrizGray)


imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)

# Mostramos Imagenes
fig = plt.figure()
# IMAGEN ORIGINAL
ax1 = fig.add_subplot(2,3,1)
ax1.imshow(imgRGB)
ax1.set_title("IMAGEN ORIGINAL")

# BRILLANTE RGB
ax3 = fig.add_subplot(2,3,2)
ax3.imshow(brillanterRGB)
ax3.set_title("BRILLANTE RGB")

# OSCURA RGB
ax4 = fig.add_subplot(2,3,3)
ax4.imshow(oscuraRGB)
ax4.set_title("OSCURA RGB")

# IMAGEN GRAY
ax2 = fig.add_subplot(2,3,4)
ax2.imshow(imgGray, cmap="gray")
ax2.set_title("ESCALA DE GRISES")

# BRILLANTE GRAY
ax3 = fig.add_subplot(2,3,5)
ax3.imshow(brillanteGray, cmap="gray")
ax3.set_title("BRILLANTE EDG")

# OSCURA GRAY
ax4 = fig.add_subplot(2,3,6)
ax4.imshow(oscuraGray, cmap="gray")
ax4.set_title("OSCURA EDG")

plt.show()

# Mostramos la imagen
cv2.imshow('IMAGEN BRILLANTE GRAY', brillanteGray)
cv2.imshow('IMAGEN OSCURA GRAY', oscuraGray)
cv2.imshow('IMAGEN BRILLANTE RGB', brillanteBGR)
cv2.imshow('IMAGEN OSCURA RGB', oscuraBGR)
cv2.waitKey(0)