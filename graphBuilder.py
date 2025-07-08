import networkx as nx

OUTSIDE = "outside"
INSIDE = "inside"

def construct_regular_graph():
    G = nx.Graph()  # or nx.DiGraph() if paths are directional

    # Define edges with (from, to, time in sec, label)
    edges = [
        ("UC", "Hunt", 3 * 60 + 42, OUTSIDE),
        ("Hunt", "Wean", 3 * 60 + 43, OUTSIDE),
        ("Wean", "Doherty", 2 * 60 + 57, INSIDE),
        ("UC", "Doherty", 2 * 60 + 34, OUTSIDE),
        ("UC", "Gates", 2 * 60 + 47, OUTSIDE),
        ("Gates", "Wean", 6 * 60 + 3, INSIDE),
        ("Wean", "Hamerschlag", 1 * 60 + 10, OUTSIDE),
        ("Hamerschlag", "Porter", 0 * 60 + 50, OUTSIDE),
        ("Porter", "Baker", 2 * 60 + 35, INSIDE),
        ("Baker", "Hunt", 0 * 60 + 35, OUTSIDE),
        ("Tepper (MM side)", "Hunt", 2 * 60 + 48, OUTSIDE),
        ("Tepper (MM side)", "UC", 3 * 60 + 12, OUTSIDE),
        ("Tepper (MM side)", "Margaret Morrison (Tepper)", 0 * 60 + 52, OUTSIDE),
        ("Margaret Morrison (Tepper)", "Margaret Morrison (UC)", 1 * 60 + 10, INSIDE),
        ("Margaret Morrison (UC)", "UC", 1 * 60 + 40, OUTSIDE),
        ("Tepper (Hunt)", "Tepper (MM side)", 2 * 60 + 1, INSIDE),
        ("Tepper (Hunt)", "Hunt", 1 * 60 + 27, OUTSIDE),
        ("Porter", "Wean", 0 * 60 + 53, OUTSIDE),
        ("Gates", "Walkway to the Sky", 1 * 60 + 48, OUTSIDE),
        ("UC", "Walkway to the Sky", 0 * 60 + 56, OUTSIDE),
    ]

    # Add edges to the graph
    for u, v, time_sec, path_type in edges:
        G.add_edge(u, v, weight=time_sec, label=path_type)

    return G
