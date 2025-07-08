import networkx as nx

OUTSIDE = "outside"
INSIDE = "inside"

def construct_regular_graph():
    G = nx.Graph()  # or nx.DiGraph() if paths are directional

    # Define edges with (from, to, time in sec, label)
    edges = [
        ("CS Admin Building", "MSI", 3 * 60 + 45, OUTSIDE),
        ("MSI", "NISMED", 2*60+56, OUTSIDE),
        ("CS Admin Building", "MSI", 225, OUTSIDE),
        ("MSI", "NISMED", 176, OUTSIDE),
        ("MSI", "NSRI", 176, OUTSIDE),
        ("NISMED", "Palma Hall (Velasquez)", 80, OUTSIDE),
        ("NSRI", "Palma Hall (Velasquez)", 80, OUTSIDE),
        ("Palma Hall (Velasquez)", "PA-Diwata", 69, OUTSIDE),
        ("PA-Diwata", "TC", 194, OUTSIDE),
        ("TC", "Yakal RH", 197, OUTSIDE),
        ("Area 2", "Epsilon Chi Center", 143, OUTSIDE),
        ("Epsilon Chi Center", "UFI", 69, OUTSIDE),
        ("UFI", "Molave RH", 34, OUTSIDE),
        ("UFI", "Gimenez Gallery", 34, OUTSIDE),
        ("Molave RH", "JEEP-Yakal", 93, OUTSIDE),
        ("JEEP-Yakal", "JEEP-Sanggumay/Kalayaan", 104, OUTSIDE),
        ("JEEP-Sanggumay/Kalayaan", "Area 2", 66, OUTSIDE),
        ("Area 2", "JEEP-Sanggumay/Kalayaan", 77, OUTSIDE),
        ("JEEP-Sanggumay/Kalayaan", "JEEP-Yakal", 91, OUTSIDE),
        ("JEEP-Yakal", "Yakal RH", 49, OUTSIDE),
    ]

    # Add edges to the graph
    for u, v, time_sec, path_type in edges:
        G.add_edge(u, v, weight=time_sec, label=path_type)

    return G