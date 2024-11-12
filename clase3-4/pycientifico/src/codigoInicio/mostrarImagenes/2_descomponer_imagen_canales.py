import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar la imagen en color
imagen = cv2.imread('../img/ninos.jpg')

# Ver la imagen en su forma original
cv2.imshow('Imagen Original', imagen)

# Descomponer la imagen en canales R, G, B
canal_b, canal_g, canal_r = cv2.split(imagen)

# Mostrar los canales R, G, B por separado
cv2.imshow('Canal Rojo', canal_r)
cv2.imshow('Canal Verde', canal_g)
cv2.imshow('Canal Azul', canal_b)

# Esperar hasta que se presione una tecla y luego cerrar todas las ventanas
cv2.waitKey(0)
#cv2.destroyAllWindows()

# También puedes mostrar los canales usando matplotlib para una visualización más conveniente
plt.figure(figsize=(10, 5))

# Mostrar la imagen original
plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
plt.title('Imagen Original')
plt.axis('off')

# Mostrar los canales R, G, B
plt.subplot(2, 2, 2)
plt.imshow(canal_r, cmap='Reds')
plt.title('Canal Rojo')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(canal_g, cmap='Greens')
plt.title('Canal Verde')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(canal_b, cmap='Blues')
plt.title('Canal Azul')
plt.axis('off')

plt.tight_layout()
plt.show()


cv2.imshow('canal_b', canal_b)
cv2.imshow('canal_g', canal_g)
cv2.imshow('canal_r', canal_r)


imagen_color = cv2.merge((canal_b, canal_g, canal_r))
cv2.imshow('image merge', imagen_color)


cv2.waitKey(0)
