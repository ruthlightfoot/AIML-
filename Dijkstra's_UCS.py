#!/usr/bin/env python
# coding: utf-8

# In[4]:


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



def dijkstra(start, goal):
    priority_queue = [(0, start, [])]  # (cost, current node, path)
    visited = set()

    while priority_queue:
        cost, current, path = heapq.heappop(priority_queue)
        
        if current in visited:
            continue
        visited.add(current)

        path = path + [current]

        if current == goal:
            print("Path found:", path, "with cost:", cost)
            return path

        for neighbor, distance in graph[current].items():
            if neighbor not in visited:
                heapq.heappush(priority_queue, (cost + distance, neighbor, path))

    print("No path found.")
    return None

# Execute Dijkstra's
dijkstra("Harrogate", "Pocklington")


# In[ ]:





# In[ ]:




