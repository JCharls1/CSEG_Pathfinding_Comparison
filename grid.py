#   1. Create the Grid:
#   Define a grid with obstacles. For example:

# Large Grid with Mixed Obstacles
grid = [
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
]

start = (0, 0)
goal = (9, 9)

# grid = [
#     [0, 0, 1, 0, 0],
#     [0, 1, 0, 1, 0],
#     [0, 0, 0, 0, 1],
#     [0, 1, 1, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
# ]

# start = (0, 0)
# goal = (4, 4)

# # Simple Path
# grid = [
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
# ]

# start = (0, 0)
# goal = (4, 4)

# # Basic Obstacles
# grid = [
#     [0, 0, 1, 0, 0],
#     [0, 1, 0, 1, 0],
#     [0, 0, 0, 0, 1],
#     [0, 1, 1, 0, 0],
#     [0, 0, 0, 0, 0],
# ]

# start = (0, 0)
# goal = (4, 4)


# # Dense Obstacles
# grid = [
#     [0, 1, 1, 1, 1],
#     [0, 0, 0, 1, 1],
#     [1, 1, 0, 1, 1],
#     [1, 1, 0, 0, 0],
#     [1, 1, 1, 1, 0],
# ]

# start = (0, 0)
# goal = (4, 4)

# # Fully Blocked Path
# grid = [
#     [0, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1],
#     [1, 1, 0, 1, 1],
#     [1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 0],
# ]

# start = (0, 0)
# goal = (4, 4)



