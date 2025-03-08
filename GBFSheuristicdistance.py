#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import heapq

# Graph representation (adjacency list with road distances)
graph = {
    "Malton": {"Scarborough": 17, "Thirsk": 5, "York": 12, "Pocklington": 10},
    "Thirsk": {"Malton": 5, "York": 6, "Harrogate": 12},
    "York": {"Malton": 12, "Thirsk": 6, "Pocklington": 11, "Leeds": 16},
    "Pocklington": {"Malton": 10, "York": 11, "Wakefield": 15},
    "Harrogate": {"Thirsk": 12, "Leeds": 10},
    "Leeds": {"Harrogate": 10, "York": 16, "Wakefield": 8},
    "Wakefield": {"Leeds": 8, "Pocklington": 15},
    "Scarborough": {"Malton": 17}
}

# Euclidean distances to Pocklington (heuristic values)
heuristic = {
    "Scarborough": 19,
    "Malton": 10,
    "York": 8,
    "Thirsk": 12,
    "Harrogate": 20,
    "Leeds": 17,
    "Wakefield": 12,
    "Pocklington": 0
}

def greedy_best_first_search(start, goal, steps=4):
    frontier = []  # Priority queue
    heapq.heappush(frontier, (heuristic[start], start))
    explored = set()
    final_frontier = []
    
    for step in range(steps):
        if not frontier:
            print("No path found.")
            return
        
        _, current = heapq.heappop(frontier)  # Choose the node with the lowest heuristic
        explored.add(current)
        print(f"Step {step + 1}: Expanding {current}")
        
        if current == goal:
            print("Goal reached!")
            break
        
        # Add neighbors to the frontier
        for neighbor in graph[current]:
            if neighbor not in explored:
                heapq.heappush(frontier, (heuristic[neighbor], neighbor))
        
        # Show the frontier in alphabetical order
        final_frontier = sorted(node for _, node in frontier)
        print(f"New Frontier: {''.join(final_frontier)}")
    
    # Print the final frontier after reaching the goal
    final_frontier = sorted(node for _, node in frontier)
    print(f"Final Frontier after reaching goal: {''.join(final_frontier)}")

# Execute the search
greedy_best_first_search("Harrogate", "Pocklington")

