import time
import pygame
from grid import grid, start, goal
from pathfinding import greedy_best_first_search, a_star_search
from visualization import draw_grid

#   6. Testing the Algorithms:
#   Write test cases to run both algorithms and compare their performance:
def comparison_and_visualization():
    pygame.init()
    cell_size = 50
    grid_width = len(grid[0]) * cell_size
    grid_height = len(grid) * cell_size
    screen = pygame.display.set_mode((grid_width, grid_height))
    pygame.display.set_caption("Search Algorithm Visualization")

    # greedy best-first search
    start_time = time.time()
    path_greedy = greedy_best_first_search(grid, start, goal, screen, cell_size)
    time_greedy = time.time() - start_time
    print("Greedy Best-First Search:")
    print("Path found:", path_greedy)
    print("Time taken: {:.6f} seconds".format(time_greedy))

    time.sleep(1)

    # A* search
    start_time = time.time()
    path_a_star = a_star_search(grid, start, goal, screen, cell_size)
    time_a_star = time.time() - start_time
    print("A* Search:")
    print("Path found:", path_a_star)
    print("Time taken: {:.6f} seconds".format(time_a_star))

    # Efficiency Comparison
    print("\nEfficiency Comparison:")
    print("Greedy Best-First Search took {:.6f} seconds".format(time_greedy))
    print("A* Search took {:.6f} seconds".format(time_a_star))
    # Path Quality Comparison
    print("\nPath Quality Comparison:")
    print("Length of path found by Greedy:", len(path_greedy) if path_greedy else "No path found")
    print("Length of path found by A*:", len(path_a_star) if path_a_star else "No path found")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()

if __name__ == "__main__":
    comparison_and_visualization()
