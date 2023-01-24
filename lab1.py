import image_processing as mz
import algorithms as al
import algoritmoA as am

# ELIJA LA IMAGEN DESEADA AQUI
# maze = mz.get_maze("p2.jpeg")
# maze = mz.get_maze("p1.png")
maze = mz.get_maze("p3.bmp")

laberinto = maze[0]
inicio = maze[1]
finales = maze[2]

single = finales[1]
tuplai = tuple(inicio)
tuplaf = tuple(single)

mz.paint_maze(laberinto, "laberinto_discretizado.png")

# Verificar si se encontró un inicio y al menos un final
if inicio is None:
    print("No se encontró un cuadro rojo como inicio")
elif len(finales) == 0:
    print("No se encontraron cuadros verdes como finales")
else:
    # Menú del programa
    bandera = True
    while bandera:
        print("\nQué algoritmo desea aplicar?\n1. BFS\n2. DFS\n3. A*\n4. Salir")
        opcion = int(input("-> "))

        # BFS
        if opcion == 1:
            # SHORTEST PATH BFS
            # for x in al.shortest_path_bfs(inicio, finales, laberinto):
            #     laberinto[x[1]][x[0]] = 5
            mz.paint_maze(laberinto, "solucion_bfs.png")

        # DFS
        elif opcion == 2:
            for x in al.shortest_path_dfs(inicio, finales, laberinto):
                laberinto[x[1]][x[0]] = 5
            mz.paint_maze(laberinto, "solucion_dfs.png")

        # A*
        elif opcion == 3:
            for x in am.shortest_path_a_star(tuplai, tuplaf, laberinto):
                laberinto[x[1]][x[0]] = 5
            mz.paint_maze(laberinto, "solucion_astar.png")

        # Salir
        elif opcion == 4:
            bandera = False

        else:
            print("\nNo eligió ninguna opción, ingrese de nuevo.")

print("Eligió salir, Adiós!")
