import networkx as nx
from typing import List, Dict, Tuple

class CriticalPathAnalyzer:
    COMPONENT_DELAYS = {
        'ADD': 1.0,
        'MUL': 1.0,
        'REG': 0.2,
        'MUX': 1.0,
    }

    def __init__(self, graph: Dict, node_types: Dict):
        self.graph = graph
        self.node_types = node_types

    def identify_node_type(self, node_id: str) -> str:
        """
        Identifies the type of a given node.
        """
        return self.node_types.get(node_id, 'UNKNOWN')

    def calculate_path_delay(self, path: List[str]) -> Tuple[float, List[str]]:
        """
        Calculates the delay of a given path.
        """
        total_delay = 0.0
        path_components = []

        for node in path:
            node_type = self.identify_node_type(node)
            delay = self.COMPONENT_DELAYS.get(node_type, 1.0)
            path_components.append(f"{node_type} ({node}): {delay} tu")
            total_delay += delay

        return total_delay, path_components

    def find_critical_path(self) -> Tuple[List[str], float, List[str]]:
        """
        Finds the critical path using topological sort.
        """
        topo_sorted_nodes = list(nx.topological_sort(nx.DiGraph(self.graph)))
        delay_to_node = {node: 0.0 for node in topo_sorted_nodes}
        previous_node = {node: None for node in topo_sorted_nodes}

        for node in topo_sorted_nodes:
            for neighbor in self.graph[node]:
                new_delay = delay_to_node[node] + self.COMPONENT_DELAYS.get(self.identify_node_type(neighbor), 1.0)
                if new_delay > delay_to_node[neighbor]:
                    delay_to_node[neighbor] = new_delay
                    previous_node[neighbor] = node

        critical_node = max(delay_to_node, key=delay_to_node.get)
        critical_path = []

        while critical_node is not None:
            critical_path.append(critical_node)
            critical_node = previous_node[critical_node]

        critical_path.reverse()
        total_delay, path_components = self.calculate_path_delay(critical_path)
        return critical_path, total_delay, path_components
