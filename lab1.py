import image_processing as mz
import algorithms as al

#maze = mz.get_maze("p2.jpeg")
maze = mz.get_maze("Prueba-Lab1.png")

laberinto = maze[0]
inicio = maze[1]
finales = maze[2]


# Verificar si se encontró un inicio y al menos un final
if inicio is None:
    print("No se encontró un cuadro rojo como inicio")
elif len(finales) == 0:
    print("No se encontraron cuadros verdes como finales")
else:
    #SHORTEST PATH BFS
    for x in al.shortest_path_bfs(inicio, finales,laberinto):
        laberinto[x[1]][x[0]] = 5

    #for x in bfs(inicio, [], [], laberinto)
    #    laberinto[x[1]][x[0]] = 5

for x in laberinto:
    print (x)