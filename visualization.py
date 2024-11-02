import pygame
import time
from grid import grid, start, goal

#4. Node Representation:
#   Create a way to represent nodes, including their coordinates, cost from the
#   start, and heuristic value.
def draw_grid(grid, visited, open_set, screen, cell_size, path=None):
    color_0 = (200, 200, 200)
    color_1 = (50, 50, 250)
    color_start = (0, 255, 0)
    color_goal = (255, 0, 0)
    color_visited = (200, 50, 50)
    color_open = (50, 200, 50)
    color_path = (255, 255, 0)

    screen.fill((0, 0, 0))
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            color = color_1 if grid[row][col] == 1 else color_0
            if (row, col) == start:
                color = color_start
            elif (row, col) == goal:
                color = color_goal
            elif (row, col) in visited:
                color = color_visited
            elif (row, col) in [node[1] for node in open_set]:
                color = color_open
            elif path and (row, col) in path:
                color = color_path

            pygame.draw.rect(
                screen,
                color,
                (col * cell_size, row * cell_size, cell_size, cell_size)
            )
            pygame.draw.rect(
                screen,
                (0, 0, 0),
                (col * cell_size, row * cell_size, cell_size, cell_size),
                1
            )
    pygame.display.flip()
