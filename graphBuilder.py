from pygraph.classes.graph import graph

OUTSIDE = "outside"
INSIDE = "inside"

def addEdge(gr, v1, v2, minutes, seconds, label):
    total_seconds = minutes * 60 + seconds
    gr.add_edge((v1, v2), wt=total_seconds, label=f"{total_seconds}s, {label}")

def constructRegularGraph():
    gr = graph()

    gr.add_nodes([
        "UC", "Hunt", "Wean", "Doherty", "Gates", "Hamerschlag", "Porter", "Baker",
        "Margaret Morrison\n(Tepper side)", "Margaret Morrison\n(UC side)",
        "Tepper\n(Margaret Morrison side)", "Tepper\n(Hunt side)", "Walkway To the Sky"
    ])

    edges = [
        ("UC", "Hunt", 3, 42, OUTSIDE),
        ("Hunt", "Wean", 3, 43, OUTSIDE),
        ("Wean", "Doherty", 2, 57, INSIDE),
        ("UC", "Doherty", 2, 34, OUTSIDE),
        ("UC", "Gates", 2, 47, OUTSIDE),
        ("Gates", "Wean", 6, 3, INSIDE),
        ("Wean", "Hamerschlag", 1, 10, OUTSIDE),
        ("Hamerschlag", "Porter", 0, 50, OUTSIDE),
        ("Porter", "Baker", 2, 35, INSIDE),
        ("Baker", "Hunt", 0, 35, OUTSIDE),
        ("Tepper\n(Margaret Morrison side)", "Hunt", 2, 48, OUTSIDE),
        ("Tepper\n(Margaret Morrison side)", "UC", 3, 12, OUTSIDE),
        ("Tepper\n(Margaret Morrison side)", "Margaret Morrison\n(Tepper side)", 0, 52, OUTSIDE),
        ("Margaret Morrison\n(Tepper side)", "Margaret Morrison\n(UC side)", 1, 10, INSIDE),
        ("Margaret Morrison\n(UC side)", "UC", 1, 40, OUTSIDE),
        ("Tepper\n(Hunt side)", "Tepper\n(Margaret Morrison side)", 2, 1, INSIDE),
        ("Tepper\n(Hunt side)", "Hunt", 1, 27, OUTSIDE),
        ("Porter", "Wean", 0, 53, OUTSIDE),
        ("Gates", "Walkway To the Sky", 1, 97, OUTSIDE),
        ("UC", "Walkway To the Sky", 0, 56, OUTSIDE),
    ]

    for edge in edges:
        addEdge(gr, *edge)

    return gr
