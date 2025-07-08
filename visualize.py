from graphBuilder import construct_regular_graph
import networkx as nx
import matplotlib.pyplot as plt

# Build the graph
G = construct_regular_graph()

# Get positions for a nice layout
pos = nx.shell_layout(G)  # You can try others: kamada_kawai_layout, circular_layout

# Draw nodes
nx.draw_networkx_nodes(G, pos, node_size=2000, node_color='lightblue')

# Draw node labels
nx.draw_networkx_labels(G, pos, font_size=9, font_weight='bold')

# Draw edges with different colors based on 'label' (inside/outside)
inside_edges = [(u, v) for u, v, d in G.edges(data=True) if d['label'] == 'inside']
outside_edges = [(u, v) for u, v, d in G.edges(data=True) if d['label'] == 'outside']

nx.draw_networkx_edges(G, pos, edgelist=inside_edges, edge_color='green', width=2, style='solid', label='Inside')
nx.draw_networkx_edges(G, pos, edgelist=outside_edges, edge_color='orange', width=2, style='dashed', label='Outside')

# Add edge labels (travel time in seconds)
edge_labels = {(u, v): f"{d['weight']}s" for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

# Add legend
plt.legend(["Inside", "Outside"], loc="upper left")

# Display
plt.title("Campus Graph with Travel Time and Path Type")
plt.axis('off')
plt.tight_layout()
plt.show()