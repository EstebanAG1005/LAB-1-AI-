from PIL import Image
from collections import deque
import pygame

# Open image
im = Image.open("p2.jpeg")

# Get image width and height
width, height = im.size

# Create a 2D array to represent the maze
maze = [[0 for x in range(width)] for y in range(height)]

# Identify the starting point and goal points in the image
start_x, start_y = -1, -1
goals = []
for x in range(width):
    for y in range(height):
        # Get pixel color
        pixel = im.getpixel((x, y))
        if pixel == (255, 255, 255):  # White
            maze[x][y] = 0
        elif pixel == (0, 0, 0):  # Black
            maze[x][y] = 1
        elif pixel == (0, 255, 0):  # Green
            maze[x][y] = 2
            goals.append((x, y))
        elif pixel == (255, 0, 0):  # Red
            start_x, start_y = x, y

if start_x == -1 or start_y == -1:
    print("Error: Starting point not found in the image")
    exit()

# Create visited array
visited = [[False for x in range(width)] for y in range(height)]

# Store the solution path
solution_path = []

# Function to implement DFS algorithm
def dfs(x, y, visited, maze, width, height, solution_path):
    # Check if current position is out of bounds or a wall
    if x < 0 or x >= width or y < 0 or y >= height or maze[x][y] == 1:
        return False
    # Check if current position is the goal
    if maze[x][y] == 2:
        solution_path.append((x, y))
        return True
    # Mark current position as visited
    visited[x][y] = True
    solution_path.append((x, y))
    # Check north, south, east, and west
    if (
        dfs(x - 1, y, visited, maze, width, height, solution_path)
        or dfs(x + 1, y, visited, maze, width, height, solution_path)
        or dfs(x, y - 1, visited, maze, width, height, solution_path)
        or dfs(x, y + 1, visited, maze, width, height, solution_path)
    ):
        return True
    # Backtrack
    visited[x][y] = False
    solution_path.pop()
    return False


# Start DFS from the starting point
if dfs(start_x, start_y, visited, maze, width, height, solution_path):
    print("Solution found!")
else:
    print("No solution found.")

# Initialize Pygame
pygame.init()

# Set the window size
size = (width * 10, height * 10)
screen = pygame.display.set_mode(size)

# Draw the maze
for x in range(width):
    for y in range(height):
        if maze[x][y] == 1:
            pygame.draw.rect(screen, (0, 0, 0), (x * 10, y * 10, 10, 10))
        elif maze[x][y] == 2:
            pygame.draw.rect(screen, (0, 255, 0), (x * 10, y * 10, 10, 10))
        else:
            pygame.draw.rect(screen, (255, 255, 255), (x * 10, y * 10, 10, 10))

# Draw the solution path
for pos in solution_path:
    pygame.draw.rect(screen, (255, 0, 0), (pos[0] * 10, pos[1] * 10, 10, 10))

# Update the screen
pygame.display.flip()

# Wait for user to close the window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
