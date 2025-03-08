#!/usr/bin/env python
# coding: utf-8

# In[5]:


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



def a_star_search(start, goal):
    priority_queue = [(heuristic[start], 0, start, [])]  # (f = g + h, g, current, path)
    visited = set()

    while priority_queue:
        _, g, current, path = heapq.heappop(priority_queue)

        if current in visited:
            continue
        visited.add(current)

        path = path + [current]

        if current == goal:
            print("Path found:", path, "with cost:", g)
            return path

        for neighbor, distance in graph[current].items():
            if neighbor not in visited:
                new_g = g + distance
                f = new_g + heuristic[neighbor]
                heapq.heappush(priority_queue, (f, new_g, neighbor, path))

    print("No path found.")
    return None

# Execute A*
a_star_search("Harrogate", "Pocklington")


# In[ ]:





# In[ ]:




