import cv2
import numpy as np

# Cargar la imagen del laberinto
image = cv2.imread("p2.jpeg")

# Definir el tamaño de los cuadros
cuadro_size = 15

# Discretizar la imagen
rows, cols = image.shape[:2]
cuadros_x = int(cols / cuadro_size)
cuadros_y = int(rows / cuadro_size)

# Crear una matriz de cuadros vacíos
laberinto = [[0 for x in range(cuadros_x)] for y in range(cuadros_y)]

# Variables para guardar la posición del inicio y los finales
inicio = None
finales = []


# Recorrer cada cuadro para identificar los obstáculos, inicio y finales
print(np.unique(image))
for x in range(cuadros_x):
    for y in range(cuadros_y):
        cuadro = image[y*cuadro_size:(y+1)*cuadro_size, x*cuadro_size:(x+1)*cuadro_size]
        
        # Utilizar algoritmos de procesamiento de imágenes para encontrar obstáculos
        if (5 in cuadro):
            laberinto[y][x] = 3
            inicio = (x, y)
        elif (254 in cuadro):
            laberinto[y][x] = 2
            finales.append((x, y))
        elif ([0,0,0] in cuadro):
            laberinto[y][x] = 1
        else:
            laberinto[y][x] = 0
# Verificar si se encontró un inicio y al menos un final
if inicio is None:
    print("No se encontró un cuadro rojo como inicio")
elif len(finales) == 0:
    print("No se encontraron cuadros verdes como finales")
else:
    pass
    # Resolver el laberinto utilizando un algoritmo de búsqueda
    # Dibujar la solución en pantalla
    # Guardar la solución en un archivo

for x in laberinto:
    print (x)