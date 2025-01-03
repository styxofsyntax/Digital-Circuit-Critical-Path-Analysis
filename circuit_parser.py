from collections import defaultdict
from typing import Dict, Tuple

class CircuitParser:
    def __init__(self, filename: str):
        self.filename = filename

    def parse(self) -> Tuple[Dict, Dict]:
        """
        Parses the circuit file and creates a graph representation.
        Returns:
            graph: A dictionary where keys are nodes and values are lists of neighbors.
            node_types: A dictionary mapping each node to its type.
        """
        graph = defaultdict(list)
        node_types = {}

        with open(self.filename, 'r') as file:
            for line in file:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue

                parts = line.split()
                node_type = parts[0]
                node_id = parts[1]
                inputs = parts[2:]

                node_types[node_id] = node_type
                for input_node in inputs:
                    graph[input_node].append(node_id)

        return graph, node_types
