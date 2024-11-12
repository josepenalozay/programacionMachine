#1_lecturaImagenes.py
import cv2

"""
La función cv2.imread() se utiliza para leer imágenes desde un archivo en la memoria y cargarlas en una estructura de datos en Python que OpenCV pueda manipular. Los enteros que se pasan como argumento a esta función se utilizan para especificar cómo se debe cargar la imagen. Aquí hay una descripción detallada de los enteros que puedes utilizar:

Nombre de archivo y ruta de la imagen: El primer argumento de la función cv2.imread() es el nombre del archivo de imagen que deseas leer. Debes proporcionar la ruta completa o relativa al archivo de imagen que deseas cargar.

Modo de lectura (Flag): El segundo argumento de la función cv2.imread() es un valor entero que especifica cómo se debe leer la imagen. Los valores más comunes que puedes usar son:

cv2.IMREAD_COLOR (o simplemente 1): Carga la imagen en su forma original con todos los canales de color (BGR, Blue-Green-Red). Esta es la opción predeterminada si no se proporciona un segundo argumento.

cv2.IMREAD_GRAYSCALE (o simplemente 0): Carga la imagen en blanco y negro (escala de grises).

cv2.IMREAD_UNCHANGED (o simplemente -1): Carga la imagen en su forma original con todos los canales de color, incluidos los canales alfa si están presentes. Esto es útil para imágenes con transparencia.

Entonces, cuando usas cv2.imread('imagen.jpg', 0), estás cargando la imagen "imagen.jpg" en modo escala de grises. Si usas cv2.imread('imagen.jpg', 1) o simplemente cv2.imread('imagen.jpg'), cargarás la imagen en color.

Aquí tienes un ejemplo de cómo se usaría la función cv2.imread():

python
Copy code
import cv2

# Cargar una imagen en color
imagen_color = cv2.imread('imagen.jpg')

# Cargar la misma imagen en escala de grises
imagen_escala_de_grises = cv2.imread('imagen.jpg', cv2.IMREAD_GRAYSCALE)
Es importante elegir el modo de lectura adecuado según tus necesidades, ya que determinará cómo se almacena y manipula la imagen en tu aplicación.

"""

# Cargar una imagen en color
I = cv2.imread('../img/ninos.jpg', cv2.IMREAD_COLOR)  #BGR o 1
print(I.shape)
cv2.imshow('foto', I)
cv2.waitKey(5000)

# Cargar la misma imagen en escala de grises
G = cv2.imread('../img/ninos.jpg', cv2.IMREAD_GRAYSCALE)  #gris o 0
print(G.shape)
cv2.imshow('foto', G)
cv2.waitKey(1000)

U = cv2.imread('../img/ninos.jpg', cv2.IMREAD_UNCHANGED)  #sin cambio
print(U.shape)
cv2.imshow('foto', U)
cv2.waitKey(1000)



cv2.imwrite('../img/ninosgris.png', G)

cv2.waitKey(5000)
