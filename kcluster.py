#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

# Given data points
points = np.array([
    [3, 1],
    [4, 3],
    [4, 4],
    [5, 3],
    [5, 4]
])

# Initial cluster centers
centroids = np.array([
    [2, 1],  # A
    [3, 3]   # B
])

def euclidean_distance(p1, p2):
    return np.sqrt(np.sum((p1 - p2) ** 2))

# Assign points to the nearest cluster
clusters = {0: [], 1: []}  # 0 for A, 1 for B
for point in points:
    distances = [euclidean_distance(point, centroid) for centroid in centroids]
    closest_cluster = np.argmin(distances)
    clusters[closest_cluster].append(point)

# Compute new centroids as the mean of assigned points
new_centroids = np.array([
    np.mean(clusters[0], axis=0),
    np.mean(clusters[1], axis=0)
])

print("Updated cluster centers:")
print(f"A: {new_centroids[0]}")
print(f"B: {new_centroids[1]}")

