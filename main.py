import networkx as nx
from collections import defaultdict
from typing import List, Dict, Tuple
import matplotlib.pyplot as plt

# Define component delays
COMPONENT_DELAYS = {
    'ADD': 1.0,
    'MUL': 1.0,
    'REG': 0.2,
    'MUX': 1.0,
    # Define any other components here
}


def parse_circuit(filename: str) -> Dict:
    """
    Parses the circuit file and creates a graph representation.
    The graph will map each node to its outgoing connections and the component type.
    """
    graph = defaultdict(list)
    node_types = {}

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith("#"):
                continue  # Skip empty lines and comments

            parts = line.split()
            node_type = parts[0]
            node_id = parts[1]
            inputs = parts[2:]

            # Store the node type and connections
            node_types[node_id] = node_type
            for input_node in inputs:
                # Add edges from inputs to current node
                graph[input_node].append(node_id)

    return graph, node_types


def identify_node_type(node_id: str, node_types: Dict) -> str:
    """
    Given a node ID, return the type of node (e.g., 'INPUT', 'ADD', 'REG', etc.).
    """
    return node_types.get(node_id, 'UNKNOWN')


def calculate_path_delay(path: List[str], node_types: Dict) -> float:
    """
    Given a path (list of node IDs), calculate the total delay along this path.
    """
    total_delay = 0.0
    path_components = []

    for node in path:
        node_type = identify_node_type(node, node_types)
        # Default delay is 1.0 if type is unknown
        delay = COMPONENT_DELAYS.get(node_type, 1.0)
        path_components.append(f"{node_type} ({node}): {delay} tu")
        total_delay += delay

    return total_delay, path_components


def find_critical_path(graph: Dict, node_types: Dict) -> Tuple[List[str], float]:
    """
    Perform a topological sort to calculate the longest path in terms of accumulated delay.
    """
    # Topologically sort the nodes (this ensures we process each node only after its dependencies)
    topo_sorted_nodes = list(nx.topological_sort(nx.DiGraph(graph)))

    # Dictionary to store maximum delays to each node
    delay_to_node = {node: 0.0 for node in topo_sorted_nodes}
    # For path reconstruction
    previous_node = {node: None for node in topo_sorted_nodes}

    # Process nodes in topological order
    for node in topo_sorted_nodes:
        for neighbor in graph[node]:
            new_delay = delay_to_node[node] + COMPONENT_DELAYS.get(
                identify_node_type(neighbor, node_types), 1.0)
            if new_delay > delay_to_node[neighbor]:
                delay_to_node[neighbor] = new_delay
                previous_node[neighbor] = node

    # Find the node with the maximum delay
    critical_node = max(delay_to_node, key=delay_to_node.get)

    # Reconstruct the path
    critical_path = []
    while critical_node is not None:
        critical_path.append(critical_node)
        critical_node = previous_node[critical_node]

    critical_path.reverse()  # Since we reconstructed the path backwards

    # Calculate the total delay and the components in the critical path
    total_delay, path_components = calculate_path_delay(
        critical_path, node_types)

    return critical_path, total_delay, path_components


def visualize_circuit(graph: Dict, critical_path: List[str]):
    """
    Visualizes the circuit using NetworkX, highlighting the critical path.
    """
    G = nx.DiGraph(graph)
    pos = nx.spring_layout(G)

    # Draw the circuit
    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, with_labels=True, node_size=2000,
            node_color='lightblue', font_size=10, font_weight='bold')

    # Highlight the critical path
    critical_edges = [(critical_path[i], critical_path[i+1])
                      for i in range(len(critical_path) - 1)]
    nx.draw_networkx_edges(
        G, pos, edgelist=critical_edges, edge_color='r', width=2)

    plt.title("Circuit Visualization with Critical Path")
    plt.show()


def main():
    circuit_files = ["circuit1.txt", "circuit2.txt",
                     "circuit3.txt", "circuit4.txt", "circuit5.txt"]

    for filename in circuit_files:
        print(f"Analyzing circuit: {filename}")
        graph, node_types = parse_circuit(filename)

        critical_path, total_delay, path_components = find_critical_path(
            graph, node_types)

        # Print the critical path and delays
        print(f"Critical Path: {' -> '.join(critical_path)}")
        print(f"Total Delay: {total_delay:.2f} time units")
        print("Path Components:")
        for component in path_components:
            print(f"- {component}")

        # Visualize the circuit
        visualize_circuit(graph, critical_path)


if __name__ == "__main__":
    main()
