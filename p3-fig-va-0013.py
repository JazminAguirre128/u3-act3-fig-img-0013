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