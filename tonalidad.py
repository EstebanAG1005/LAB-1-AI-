import cv2
import numpy as np

# Cargar la imagen
img = cv2.imread("Test.bmp")

# Convertir la imagen a HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define el rango de tonos de rojo
lower_red = np.array([0, 0, 150])
upper_red = np.array([50, 50, 255])

# Aplicar la función inRange para verificar si hay rojo en la imagen
red_mask = cv2.inRange(hsv, lower_red, upper_red)

# Contar la cantidad de píxeles blancos (rojos) en la máscara
red_pixels = cv2.countNonZero(red_mask)

# Verificar si hay rojo en la imagen
if red_pixels > 0:
    print("La imagen contiene rojo.")
else:
    print("La imagen no contiene rojo.")
