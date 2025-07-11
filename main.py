from graphBuilder import construct_regular_graph
import networkx as nx

G = construct_regular_graph()

# Print nodes and edge info
print("Nodes:", G.nodes())
print("\nEdges:")
for u, v, data in G.edges(data=True):
    print(f"{u} — {v} : {data['weight']}s, {data['label']}")

# Example: find shortest path based on time
shortest_path = nx.shortest_path(G, "CS Admin Building", "Area 2", weight='weight')
total_time = nx.shortest_path_length(G, "CS Admin Building", "Area 2", weight='weight')

print("\nShortest path from CS Admin Building to Area 2:")
print(" → ".join(shortest_path))
print(f"Total time: {total_time} seconds")