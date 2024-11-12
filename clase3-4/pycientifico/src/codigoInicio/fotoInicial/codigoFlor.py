import cv2
import numpy as np
import matplotlib.pyplot as plt

def howis(img):
  print('size = ',img.shape)
  print('max  = ',np.max(img))
  print('min  = ',np.min(img))

Icv = cv2.imread('../img/flowers.jpeg')    # lectura en formato opencv (BGR)
cv2.imshow('Icv',Icv)
howis(Icv)
print(Icv)

plt.imshow(Icv)
plt.show()

I = Icv[:,:,[2,1,0]]             # conversion a formato estándar (RGB)
plt.imshow(I)
plt.show()


R = I[:,:,0]
G = I[:,:,1]
B = I[:,:,2]
RGB = np.concatenate((R,G,B),axis=1)
cv2.imshow('RGB',RGB)


Rd = R.astype(float)
Gd = G.astype(float)
Bd = B.astype(float)
#k  = (1/3,1/3,1/3)
k  = (0.1,0.4,0.5)
Zd = k[0]*Rd+k[1]*Gd+k[2]*Bd
Z  = Zd.astype(int)
howis(Z)
#cv2.imshow('Z',Z)

def imhist(X):
  (N,M) = X.shape
  n = 256
  h = np.zeros((256,))
  for i in range(N):
    for j in range(M):
      x = X[i,j]
      h[x] = h[x]+1
  plt.plot(range(n),h[0:n])
  plt.show()