import image_processing as mz
import algorithms as al
import algoritmoA as am

# maze = mz.get_maze("p2.jpeg")
# maze = mz.get_maze("p1.png")
maze = mz.get_maze("p3.bmp")

laberinto = maze[0]
inicio = maze[1]
finales = maze[2]

al.paint_maze(laberinto, "laberinto_discretizado.png")

# Verificar si se encontró un inicio y al menos un final
if inicio is None:
    print("No se encontró un cuadro rojo como inicio")
elif len(finales) == 0:
    print("No se encontraron cuadros verdes como finales")
else:
    # SHORTEST PATH BFS
    for x in al.shortest_path_bfs(inicio, finales, laberinto):
        laberinto[x[1]][x[0]] = 5
    # DFS
    # for x in al.shortest_path_dfs(inicio, finales, laberinto):
    #     laberinto[x[1]][x[0]] = 5
    # for x in al.dfs(inicio, [], [], laberinto):
    #     laberinto[x[1]][x[0]] = 5
    # A*
    # for x in am.shortest_path_a_star(inicio, finales, laberinto):
    #    laberinto[x[1]][x[0]] = 5

    # for x in bfs(inicio, [], [], laberinto)
    #    laberinto[x[1]][x[0]] = 5

al.paint_maze(laberinto, "solucion_laberinto_BFS3.png")
