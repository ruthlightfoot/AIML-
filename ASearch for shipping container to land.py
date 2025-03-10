#!/usr/bin/env python
# coding: utf-8

# In[9]:


import networkx as nx
import matplotlib.pyplot as plt


# Define the states and heuristic values
states = {
    "A": (0, "Land, No, Land"),
    "B": (20, "Land, No, Ship"),
    "C": (3, "Land, Yes, Land"),
    "D": (5, "Ship, No, Land"),
    "E": (16, "Ship, No, Ship"),
    "F": (9, "Ship, Yes, Ship"),
}

# Define transitions with action costs
transitions = {
    ("B", "E"): 3,   # Move crane to ship (cost 3)
    ("E", "F"): 10,  # Pick up container (cost 10)
    ("F", "C"): 7,   # Move crane to land with container (cost 7)
    ("C", "A"): 3,   # Put down the container (cost 3)
}

# Compute cumulative costs (g(n)) during A* traversal
g_costs = {"B": 0}  # Start state has cost 0
for (src, dst), cost in transitions.items():
    g_costs[dst] = g_costs[src] + cost

# Compute f(n) = g(n) + h(n)
f_values = {state: g_costs.get(state, float("inf")) + h for state, (h, _) in states.items()}

# Create the graph
G = nx.DiGraph()
for state, (h, desc) in states.items():
    G.add_node(state, heuristic=h, label=f"{state}\n{desc}\nh={h}\ng={g_costs.get(state, 'N/A')}\nf={f_values.get(state, 'N/A')}")

for (src, dst), cost in transitions.items():
    G.add_edge(src, dst, weight=cost, label=f"{cost}")

# Define node positions for visualization
pos = {
    "A": (4, 0),
    "B": (0, 2),
    "C": (4, 2),
    "D": (2, 1),
    "E": (2, 3),
    "F": (3, 3),
}

# Draw the graph
# Create figure and axis
fig, ax = plt.subplots(figsize=(8, 6))

# Draw the graph
nx.draw(G, pos, with_labels=True, node_size=3500, node_color="lightblue", edge_color="gray", font_size=10, ax=ax)
edge_labels = {(u, v): f"{d['weight']}" for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10, ax=ax)

# Highlight the full path to goal
full_path_edges = [("B", "E"), ("E", "F"), ("F", "C"), ("C", "A")]
nx.draw_networkx_edges(G, pos, edgelist=full_path_edges, edge_color="red", width=3, ax=ax)

# Display cumulative g(n) and f(n) costs at each node
node_labels = {state: f"{state}\ng={g_costs.get(state, 'N/A')}\nf={f_values.get(state, 'N/A')}" for state in states}
nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=8, font_color="black", ax=ax)

plt.title("A* Search for Shipping Container Problem (With Cumulative Costs)")
plt.show()



# In[ ]:




