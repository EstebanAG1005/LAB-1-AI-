def up(x,y,laberinto):
    if y < len(laberinto)-1 and laberinto[y+1][x] != 1:
        return [x,y+1]
    else:
        return None

def down(x,y,laberinto):
    if y >0 and laberinto[y-1][x] != 1:
        return [x,y-1]
    else:
        return None

def left(x,y,laberinto):
    if x>0 and laberinto[y][x-1] !=1:
        return [x-1,y]
    else:
        return None

def right(x,y,laberinto):
    if x< len(laberinto[0])-1 and laberinto[y][x+1] != 1:
        return [x+1,y]
    else:
        return None

def shortest_path_bfs(node1, node2, laberinto):
    path_list = [[node1]]
    path_index = 0
    # To keep track of previously visited nodes
    previous_nodes = [node1]
    if node1 in node2:
        return path_list[0]
        
    while path_index < len(path_list):
        current_path = path_list[path_index]
        last_node = current_path[-1]
        next_nodes = []

        next_nodes.append(up(last_node[0],last_node[1],laberinto))
        next_nodes.append(down(last_node[0],last_node[1],laberinto))
        next_nodes.append(left(last_node[0],last_node[1],laberinto))
        next_nodes.append(right(last_node[0],last_node[1],laberinto))
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
                path_list.append(new_path)
                # To avoid backtracking
                previous_nodes.append(next_node)
        # Continue to next path in list
        path_index += 1
    # No path is found
    return []

def bfs(node, visited, queue, laberinto): #function for BFS
    visited.append(node)
    queue.append(node)
    found = False
    while queue and not found:          # Creating loop to visit each node
        m = queue.pop(0) 

        neighbours = []

        neighbours.append(up(m[0],m[1], laberinto))
        neighbours.append(down(m[0],m[1], laberinto))
        neighbours.append(left(m[0],m[1], laberinto))
        neighbours.append(right(m[0],m[1], laberinto))

        for neighbour in neighbours:
            if neighbour != None and neighbour not in visited:
                if laberinto[neighbour[1]][neighbour[0]] != 2:
                    visited.append(neighbour)
                    queue.append(neighbour)
                else:
                    found = True
                    break
    return visited

import heapq

def a_star(graph, start, goal, heuristic='manhattan'):
    # Create an empty priority queue
    frontier = []
    heapq.heappush(frontier, (0, start))
    # Create a dictionary to store the cost of each node
    came_from = {}
    cost_so_far = {}
    came_from[(start)] = None
    cost_so_far[(start)] = 0

    while frontier:
        current = heapq.heappop(frontier)[1]

        if current == goal:
            break

        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                # Select the heuristic to use based on the parameter
                if heuristic == 'manhattan':
                    priority = new_cost + manhattan_distance(goal, next)
                elif heuristic == 'euclidean':
                    priority = new_cost + euclidean_distance(goal, next)
                heapq.heappush(frontier, (priority, next))
                came_from[next] = current

    return came_from, cost_so_far

def manhattan_distance(a, b):
    # Example of a Manhattan distance heuristic
    return abs(a.x - b.x) + abs(a.y - b.y)

def euclidean_distance(a, b):
    # Example of a Euclidean distance heuristic
    return ((a.x - b.x) ** 2 + (a.y - b.y) ** 2) ** 0.5
