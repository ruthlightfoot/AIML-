#!/usr/bin/env python
# coding: utf-8

# In[3]:


from collections import deque
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


def dfs(start, goal, path=None, visited=None):
    if path is None:
        path = [start]
    if visited is None:
        visited = set()

    if start == goal:
        print("Path found:", path)
        return path

    visited.add(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            new_path = dfs(neighbor, goal, path + [neighbor], visited)
            if new_path:
                return new_path

    return None

# Execute DFS
dfs("Harrogate", "Pocklington")


# In[ ]:




