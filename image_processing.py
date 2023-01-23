import cv2
import numpy as np
from PIL import Image, ImageDraw


def get_maze(file):

    # Cargar la imagen del laberinto
    image = cv2.imread(file)

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_green_bound = np.array([36, 50, 0])
    upper_green_bound = np.array([86, 255, 255])

    # find the colors within the boundaries
    green_mask = cv2.inRange(hsv, lower_green_bound, upper_green_bound)

    lower_red_bound_1 = np.array([0, 50, 20])
    upper_red_bound_1 = np.array([5, 255, 255])
    lower_red_bound_2 = np.array([175, 50, 20])
    upper_red_bound_2 = np.array([180, 255, 255])

    lower_black_bound = np.array([0, 0, 0])
    upper_black_bound = np.array([50, 50, 100])

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

    start_x, start_y = -1, -1
    goals = []
    for x in range(cuadros_x):
        for y in range(cuadros_y):
            cuadro_green = green_mask[y*cuadro_size:(
                y+1)*cuadro_size, x*cuadro_size:(x+1)*cuadro_size]
            cuadro_red_1 = red_mask_1[y*cuadro_size:(
                y+1)*cuadro_size, x*cuadro_size:(x+1)*cuadro_size]
            cuadro_red_2 = red_mask_2[y*cuadro_size:(
                y+1)*cuadro_size, x*cuadro_size:(x+1)*cuadro_size]
            cuadro_black = black_mask[y*cuadro_size:(
                y+1)*cuadro_size, x*cuadro_size:(x+1)*cuadro_size]

            if (255 in cuadro_green):
                laberinto[y][x] = 2
                goals.append([x, y])
            if (255 in cuadro_red_1 and start_x*start_y == 1):
                laberinto[y][x] = 3
                start_x, start_y = x, y
            if (255 in cuadro_red_2 and start_y*start_x == 1):
                laberinto[y][x] = 3
                start_x, start_y = x, y
            if (255 in cuadro_black):
                laberinto[y][x] = 1

    return [laberinto, [start_x, start_y], goals]


def paint_maze(maze, name):
    # se obtienen las dimensiones del laberinto
    rows = len(maze)
    cols = len(maze[0])
    # se crea la imagen con las dimensiones
    img = Image.new("RGB", (cols * 12, rows * 12), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    # se recorre cada celda del laberinto
    for row in range(rows):
        for col in range(cols):
            # obtenemos el num de la celda
            num = maze[row][col]
            # se pinta la celda
            if num == 1:
                color = (0, 0, 0)
            elif num == 0:
                color = (255, 255, 255)
            elif num == 2:
                color = (0, 255, 0)
            elif num == 3:
                color = (255, 0, 0)
            elif num == 5:
                color = (255, 165, 0)
            else:
                color = (255, 255, 255)
            x1 = col * 12 + 1
            y1 = row * 12 + 1
            x2 = x1 + 10
            y2 = y1 + 10
            draw.rectangle([(x1, y1), (x2, y2)], fill=color)
    img.save(name)
