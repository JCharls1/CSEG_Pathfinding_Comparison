# 2. Heuristic Function:
# Define a heuristic function (Manhattan distance) to evaluate the estimated
# cost from a node to the treasure.
def heuristic(a, b):
    # calculate distance between 2 points
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
