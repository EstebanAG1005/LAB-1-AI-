import heapq
import math
from typing import Tuple, List


def get_neighbours(
    node: Tuple[int, int], laberinto: List[List[int]]
) -> List[Tuple[int, int]]:
    # Se crea el ambiente en donde se movera la IA y aqui se maneja su movimiento
    neighbours = []
    x, y = node
    if y > 0 and laberinto[y - 1][x] != 1:
        neighbours.append((x, y - 1))
    if y < len(laberinto) - 1 and laberinto[y + 1][x] != 1:
        neighbours.append((x, y + 1))
    if x > 0 and laberinto[y][x - 1] != 1:
        neighbours.append((x - 1, y))
    if x < len(laberinto[0]) - 1 and laberinto[y][x + 1] != 1:
        neighbours.append((x + 1, y))
    return neighbours


# Manhattan es la suma de los valores absolutos de las diferencias en las coordenadas x e y del objetivo y las coordenadas de la celda actual.
# Se usa esta heuristica cuando se nos permite movernos solo en cuatro direcciones (derecha, izquierda, arriba, abajo).
def manhattan_distance(a: Tuple[int, int], b: Tuple[int, int]) -> int:
    x1, y1 = a
    x2, y2 = b
    return abs(x1 - x2) + abs(y1 - y2)


# Euclidean es la distancia entre la celda actual y la celda objetivo usando la fórmula de distancia
# Se usa esta heuristica cuando se nos permite movernos en cualquier dirección.
def euclidean_distance(a: Tuple[int, int], b: Tuple[int, int]) -> float:
    x1, y1 = a
    x2, y2 = b
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def shortest_path_a_star(
    start: Tuple[int, int],
    goal: Tuple[int, int],
    laberinto: List[List[int]],
    heuristic: str = "manhattan",
) -> List[Tuple[int, int]]:
    # Se verifica que los parametros esten correctos
    if not (isinstance(start, tuple) and len(start) == 2):
        raise ValueError("El parametro start debe ser una tupla de dos elementos")
    if not (isinstance(goal, tuple) and len(goal) == 2):
        raise ValueError("El parametro goal debe ser una tupla de dos elementos")
    if not (
        isinstance(laberinto, list) and all(isinstance(row, list) for row in laberinto)
    ):
        raise ValueError("El parametro laberinto debe ser una matriz")
    if heuristic not in {"manhattan", "euclidean"}:
        raise ValueError(f"Heuristic {heuristic} not supported")

    heap = []
    visited = set()
    came_from = {}
    cost_so_far = {}
    # Se verifica que heuristica es la que se usara
    if heuristic == "manhattan":
        heap.append((manhattan_distance(start, goal), start))
        cost_so_far[start] = 0
    elif heuristic == "euclidean":
        heap.append((euclidean_distance(start, goal), start))
        cost_so_far[start] = 0

    # Se utiliza el costo de la ruta desde su origen y costo estimado de la ruta para llegar al destino
    while heap:
        (current_cost, current) = heapq.heappop(heap)
        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            return reconstruct_path(current, came_from)

        for neighbour in get_neighbours(current, laberinto):
            if heuristic == "manhattan":
                new_cost = cost_so_far[current] + 1
                priority = new_cost + manhattan_distance(goal, neighbour)
            elif heuristic == "euclidean":
                new_cost = cost_so_far[current] + 1
                priority = new_cost + euclidean_distance(goal, neighbour)

            if neighbour not in cost_so_far or new_cost < cost_so_far[neighbour]:
                cost_so_far[neighbour] = new_cost
                heapq.heappush(heap, (priority, neighbour))
                came_from[neighbour] = current
    return []


def reconstruct_path(current, came_from):
    # Funcion para ayudar a devolver el laberinto con el cambio
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1]
