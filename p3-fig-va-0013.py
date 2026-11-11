import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2

# Meredith Aguirre NC = 0013
print("Meredith Aguirre NC = 0013")
print("UIII Act3 colocar puntos a una imagen  en blanco y negro")
mi_imagen = cv2.imread('PrincesaDiana.jpg')
plt.imshow(mi_imagen)
plt.title('Princesa Diana y Meredith Aguirre 0013')
plt.show()
print("-+-+-+- Puntos en la imagen -+-+-+-")
plt.imshow(mi_imagen)
x = [100, 100, 300]
y = [100, 100, 300]
plt.scatter(x, y, s = 20, c = "Red")
plt.show()
print("-+-+-+- Cuadro azul en la imagen -+-+-+-")
img_PrincesaDiana = cv2.imread('PrincesaDiana.jpg')
plt.imshow(img_PrincesaDiana)
x = [100, 100, 500, 500, 100]
y = [500, 100, 100, 500, 500]
plt.plot(x, y, c = "Blue")
plt.show()
print("-+-+-+-Circulo verde en la imagen -+-+-+-")
imagenez = cv2.imread('PrincesaDiana.jpg')
plt.imshow(imagenez)
N = 30
x = np.zeros((N+1,))
y = np.zeros((N+1,))
(xc, yc) = (300, 300)
r = 150 # radio 
for i in range(N+1):
    t = 2*np.pi/N*i
    x[i] = xc + r*np.cos(t)
    y[i] = yc + r*np.sin(t)
plt.plot(x, y, c = 'green')
plt.show()
