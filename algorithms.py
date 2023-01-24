
def up(x, y, laberinto):
    if y < len(laberinto) - 1 and laberinto[y + 1][x] != 1:
        return [x, y + 1]
    else:
        return None


def down(x, y, laberinto):
    if y > 0 and laberinto[y - 1][x] != 1:
        return [x, y - 1]
    else:
        return None


def left(x, y, laberinto):
    if x > 0 and laberinto[y][x - 1] != 1:
        return [x - 1, y]
    else:
        return None


def right(x, y, laberinto):
    if x < len(laberinto[0]) - 1 and laberinto[y][x + 1] != 1:
        return [x + 1, y]
    else:
        return None


def shortest_path_bfs(node1, node2, laberinto):
    path_list = [[node1]]
    path_index = 0
    # Con el objetivo de tener un registro de todos los nodos anteriores
    previous_nodes = [node1]
    if node1 in node2:
        return path_list[0]

    # Iteramos sobre todos los caminos posibles
    while path_index < len(path_list):
        current_path = path_list[path_index]
        last_node = current_path[-1]
        next_nodes = []

        # Se buscan todos los nodos siguientes, en caso de este sistema, todos los pixeles al rededor
        next_nodes.append(up(last_node[0], last_node[1], laberinto))
        next_nodes.append(down(last_node[0], last_node[1], laberinto))
        next_nodes.append(left(last_node[0], last_node[1], laberinto))
        next_nodes.append(right(last_node[0], last_node[1], laberinto))
        
        # Verificamos si el nodo destino se encuentra en uno de los nodos conectores
        for dest in node2:
            if dest in next_nodes:
                current_path.append(dest)
                return current_path

        # Agregamos nuevos caminos
        for next_node in next_nodes:
            if next_node != None and not next_node in previous_nodes:
                new_path = current_path[:]
                new_path.append(next_node)
                path_list.append(new_path)
                # mantenemos registro de los nodos visitados para evitar backtracking
                previous_nodes.append(next_node)
        # Continuamos el siguiente camino
        path_index += 1
    # Si no encontramos ningun camino
    return []


def bfs(node, visited, queue, laberinto):
    visited.append(node)
    queue.append(node)
    found = False
    #Vamos iterando sobre cada uno de los nodos
    while queue and not found:
        m = queue.pop(0)

        # Llevamos control de todos los nodos visitados
        neighbours = []

        # Se buscan todos los nodos siguientes, en caso de este sistema, todos los pixeles al rededor
        neighbours.append(up(m[0], m[1], laberinto))
        neighbours.append(down(m[0], m[1], laberinto))
        neighbours.append(left(m[0], m[1], laberinto))
        neighbours.append(right(m[0], m[1], laberinto))

        # Por cada uno de los siguientes nodos verificamos si estan en los visitados para evitar backtracking
        # Tambien verificamos si es nodo final
        for neighbour in neighbours:
            if neighbour != None and neighbour not in visited:
                if laberinto[neighbour[1]][neighbour[0]] != 2:
                    visited.append(neighbour)
                    queue.append(neighbour)
                else:
                    found = True
                    break
    # Retornamos todos los nodos visitados
    return visited


def shortest_path_dfs(node1, node2, laberinto):
    path_stack = [[node1]]
    # To keep track of previously visited nodes
    previous_nodes = [node1]
    if node1 in node2:
        return path_stack[0]

    while path_stack:
        current_path = path_stack.pop()
        last_node = current_path[-1]
        next_nodes = []

        next_nodes.append(up(last_node[0], last_node[1], laberinto))
        next_nodes.append(down(last_node[0], last_node[1], laberinto))
        next_nodes.append(left(last_node[0], last_node[1], laberinto))
        next_nodes.append(right(last_node[0], last_node[1], laberinto))
        # Search goal node
        for dest in node2:
            if dest in next_nodes:
                current_path.append(dest)
                return current_path
        # Add new paths
        for next_node in next_nodes:
            if next_node != None and not next_node in previous_nodes:
                new_path = current_path[:]
                new_path.append(next_node)
                path_stack.append(new_path)
                # To avoid backtracking
                previous_nodes.append(next_node)
    # No path is found
    return []


def dfs(node, visited, stack, laberinto):
    visited.append(node)
    stack.append(node)
    found = False
    while stack and not found:
        m = stack.pop()

        neighbours = []
        neighbours.append(up(m[0], m[1], laberinto))
        neighbours.append(down(m[0], m[1], laberinto))
        neighbours.append(left(m[0], m[1], laberinto))
        neighbours.append(right(m[0], m[1], laberinto))

        for neighbour in neighbours:
            if neighbour != None and neighbour not in visited:
                if laberinto[neighbour[1]][neighbour[0]] != 2:
                    visited.append(neighbour)
                    stack.append(neighbour)
                else:
                    found = True
                    break
    return visited
