import heapq

def up(x, y, laberinto):
    if y > 0 and laberinto[y-1][x] != 1:
        return (x, y-1)
    return None

def down(x, y, laberinto):
    if y < len(laberinto)-1 and laberinto[y+1][x] != 1:
        return (x, y+1)
    return None

def left(x, y, laberinto):
    if x > 0 and laberinto[y][x-1] != 1:
        return (x-1, y)
    return None

def right(x, y, laberinto):
    if x < len(laberinto[0])-1 and laberinto[y][x+1] != 1:
        return (x+1, y)
    return None

current_from = None
visited = set()

def shortest_path_a_star(start, goal, laberinto):
    heap = [(0, start)]
    visited.clear()
    came_from = {}
    while heap:
        (cost, current) = heapq.heappop(heap)
        current = tuple(current)
        if current in visited:
            continue
        visited.add(current)
        came_from[current] = current_from
        if current == goal:
            return reconstruct_path(current, came_from)
        for neighbour in get_neighbours(current, laberinto):
            if neighbour in visited:
                continue
            heapq.heappush(heap, (cost + 1 + manhattan_distance(neighbour, goal), neighbour))
    return []



def reconstruct_path(current, came_from):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1]

def manhattan_distance(a, b):
    x1, y1 = int(a[0]), int(a[1])
    x2, y2 = int(b[0][0]), int(b[0][1])
    return abs(x1 - x2) + abs(y1 - y2)

def get_neighbours(node, laberinto):
    neighbours = []
    neighbours.append(up(node[0], node[1], laberinto))
    neighbours.append(down(node[0], node[1], laberinto))
    neighbours.append(left(node[0], node[1], laberinto))
    neighbours.append(right(node[0], node[1], laberinto))
    return [n for n in neighbours if n]
