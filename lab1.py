import cv2
import numpy as np

# Cargar la imagen del laberinto
image = cv2.imread("p2.jpeg")

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_green_bound = np.array([36, 50, 0])	 
upper_green_bound = np.array([86, 255, 255])

# find the colors within the boundaries
green_mask = cv2.inRange(hsv, lower_green_bound, upper_green_bound)

lower_red_bound_1 = np.array([0, 50, 20])	 
upper_red_bound_1 = np.array([5, 255, 255])
lower_red_bound_2 = np.array([175, 50, 20])	 
upper_red_bound_2 = np.array([180, 255, 255])

lower_black_bound = np.array([0,0,0])
upper_black_bound = np.array([50,50,100])

# find the colors within the boundaries
red_mask_1 = cv2.inRange(hsv, lower_red_bound_1, upper_red_bound_1)
red_mask_2 = cv2.inRange(hsv, lower_red_bound_2, upper_red_bound_2)
black_mask = cv2.inRange(hsv, lower_black_bound, upper_black_bound)

# Definir el tamaño de los cuadros
cuadro_size = 12

# Discretizar la imagen
rows, cols = image.shape[:2]
cuadros_x = int(cols / cuadro_size)
cuadros_y = int(rows / cuadro_size)

# Crear una matriz de cuadros vacíos
laberinto = [[0 for x in range(cuadros_x)] for y in range(cuadros_y)]

# Variables para guardar la posición del inicio y los finales
inicio = None
finales = []


#print(np.unique(red_mask))
for x in range(cuadros_x):
    for y in range(cuadros_y):
        cuadro_green = green_mask[y*cuadro_size:(y+1)*cuadro_size, x*cuadro_size:(x+1)*cuadro_size]
        cuadro_red_1 = red_mask_1[y*cuadro_size:(y+1)*cuadro_size, x*cuadro_size:(x+1)*cuadro_size]
        cuadro_red_2 = red_mask_2[y*cuadro_size:(y+1)*cuadro_size, x*cuadro_size:(x+1)*cuadro_size]
        cuadro_black = black_mask[y*cuadro_size:(y+1)*cuadro_size, x*cuadro_size:(x+1)*cuadro_size]

        if (255 in cuadro_green):
            laberinto[y][x] = 2
        if (255 in cuadro_red_1):
            laberinto[y][x] = 3
        if (255 in cuadro_red_2):
            laberinto[y][x] = 3
        if (255 in cuadro_black):
            laberinto[y][x] = 1

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