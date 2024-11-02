import heapq
import time
import pygame
from heuristic import heuristic
from grid import grid, start, goal
from visualization import draw_grid

def get_neighbors(node, grid):
    neighbors = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        x, y = node[0] + dx, node[1] + dy
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
            if grid[x][y] == 0:
                neighbors.append((x, y))
    return neighbors

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path

#2. Implement Greedy Best-First Search:
#   Write a function that implements the Greedy Best-First Search algorithm. Use
#   a priority queue to explore the most promising nodes based on the heuristic.
def greedy_best_first_search(grid, start, goal, screen, cell_size):
    open_set = []
    heapq.heappush(open_set, (heuristic(start, goal), start))
    came_from = {}
    visited = set()

    while open_set:
        _, current = heapq.heappop(open_set)
        if current == goal:
            return reconstruct_path(came_from, current)

        if current in visited:
            continue
        visited.add(current)

        draw_grid(grid, visited, open_set, screen, cell_size, path=None)
        time.sleep(0.1)

        for neighbor in get_neighbors(current, grid):
            if neighbor not in visited:
                came_from[neighbor] = current
                heapq.heappush(open_set, (heuristic(neighbor, goal), neighbor))

    return None

#3. Implement A Search:
#   Write a function that implements the A* Search algorithm.
#   This will consider both the cost to reach the node and the heuristic.
def a_star_search(grid, start, goal, screen, cell_size):
    open_set = []
    heapq.heappush(open_set, (0 + heuristic(start, goal), 0, start))
    came_from = {}
    g_score = {start: 0}
    visited = set()

    while open_set:
        _, current_g, current = heapq.heappop(open_set)

        if current == goal:
            return reconstruct_path(came_from, current)

        if current in visited:
            continue
        visited.add(current)

        draw_grid(grid, visited, open_set, screen, cell_size, path=None)
        time.sleep(0.1)

        for neighbor in get_neighbors(current, grid):
            tentative_g_score = current_g + 1
            if neighbor in g_score and tentative_g_score >= g_score[neighbor]:
                continue

            came_from[neighbor] = current
            g_score[neighbor] = tentative_g_score
            f_score = tentative_g_score + heuristic(neighbor, goal)
            heapq.heappush(open_set, (f_score, tentative_g_score, neighbor))

    return None
