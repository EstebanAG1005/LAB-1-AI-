import cv2
import numpy as np

# Cargar la imagen
image = cv2.imread("Prueba-Lab1.png")

# Dividir la imagen en canales R, G, B
b, g, r = cv2.split(image)

# Convertir los canales en matrices de una sola dimensión
colors = np.array([np.ravel(r), np.ravel(g), np.ravel(b)])

# Encontrar los valores únicos en la matriz de colores
unique_colors = np.unique(colors, axis=1)

# Crear un arreglo vacío para almacenar los colores en formato RGB
rgb_colors = []

# Recorrer cada color único
for color in unique_colors:
    # Crear un arreglo con el color en formato RGB
    rgb_color = [color[0], color[1], color[2]]
    # Agregar el color al arreglo de colores en formato RGB
    rgb_colors.append(rgb_color)

# Imprimir el arreglo de colores en formato RGB
print(rgb_colors)