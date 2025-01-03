import networkx as nx
import matplotlib.pyplot as plt
from typing import Dict, List

class CircuitVisualizer:
    def __init__(self, graph: Dict):
        self.graph = graph

    def visualize(self, critical_path: List[str]):
        """
        Visualizes the circuit graph and highlights the critical path.
        """
        G = nx.DiGraph(self.graph)
        pos = nx.spring_layout(G)

        plt.figure(figsize=(12, 8))
        nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=10, font_weight='bold')

        critical_edges = [(critical_path[i], critical_path[i + 1]) for i in range(len(critical_path) - 1)]
        nx.draw_networkx_edges(G, pos, edgelist=critical_edges, edge_color='r', width=2)

        plt.title("Circuit Visualization with Critical Path")
        plt.show()
