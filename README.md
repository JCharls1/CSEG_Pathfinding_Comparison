

# 1. Programming Activity: Pathfinding Algorithms in Python

## **Presented by:**

Abayari, Rob Fritz <br/>
De jesus, Michael Ivan <br/>
Duhaylungsod, Kyziah Mae <br/>
Elomina, Marc Ryzon <br/>
Garcia, John Charles <br/>
Guevarra, Shane Ashley <br/>
Pantonia, John Carlo <br/>
Salamat, Rolph <br/>
Saturno, M-jey <br/>


# Contents
1. [Programming Activity: Pathfinding Algorithms in Python](#programming-activity-pathfinding-algorithms-in-python)
   - [Overview of the algorithms implemented](#21-overview-of-the-algorithms-implemented)
   - [Instructions on how to run the code](#22-instructions-on-how-to-run-the-code-)
   - [Description of your approach and any challenges faced](#23-description-of-your-approach-and-any-challenges-faced)
2. [Screenshots](#3-screenshots)
   - [Paths found by both algorithms](#31-the-paths-found-by-both-algorithms)
   - [Time taken for each algorithm](#32-the-time-taken-for-each-algorithm)
   - [Lengths of the paths](#33-the-lengths-of-the-paths)


## 2.1 Overview of the algorithms implemented.

**Greedy Best-First Search Algorithm**

The Greedy Best-First Search algorithm is a pathfinding algorithm that aims to find the shortest path by exploring the most promising nodes first, based solely on a heuristic estimate to the goal.

**A-Star Algorithm**

The A* algorithm is a pathfinding and graph traversal algorithm that finds the shortest path between two points. It is widely used in games, navigation systems, and AI applications due to its efficiency in finding paths in complex environments.<br/>

## 2.2 Instructions on how to run the code. <br/>

**1. clone this repository**


```console 
$ git clone https://github.com/JCharls1/CSEG_Pathfinding_Comparison.git
```

**2. Open the folder in vs code**

**3. run the python code**
```console 
$ python src/main.py
```
or
```console 
$ python3 src/main.py
```

## Dependencies


**python** 

- https://www.python.org/ 
<br/>

**pygame**
- https://pypi.org/project/pygame/


```console 
$ pip install pygame
```

or

```console 
$ pip3 install pygame
```

## 2.3 Description of your approach and any challenges faced.

This implementation efficiently finds the shortest path by focusing on cells with the lowest total estimated path cost, minimizing unnecessary exploration and improving speed. It also offers visualization to make the search progress easy to follow, especially for learning or debugging purposes.<br/>

Our main challenge is how we can visualize the algorithms and where to put the functionality without costing us the efficiency of the algorithm.

# 3. Screenshots: Include screenshots of the output from your program showing:

## 3.1 The paths found by both algorithms.

Grid<br/>

![screenshot](./Screenshots/Grid.png)<br/>

Greedy<br/>
![screenshot](./Screenshots/Greedy.png)<br/>

![screenshot](./Screenshots/Greedy_paths.png)<br/>

A*<br/>
![screenshot](./Screenshots/Astar.png)<br/>

![screenshot](./Screenshots/Astar_paths.png)<br/>


## 3.2 The time taken for each algorithm.

![screenshot](./Screenshots/Efficiency_comparison.png)<br/>


## 3.3 The lengths of the paths.


![screenshot](./Screenshots/path_quality.png)<br/>
