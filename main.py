from circuit_parser import CircuitParser
from critical_path import CriticalPathAnalyzer
from visualizer import CircuitVisualizer

def main():
    circuit_files = ["circuit1.txt", "circuit2.txt",
                     "circuit3.txt", "circuit4.txt", "circuit5.txt"]

    for filename in circuit_files:
        print(f"Analyzing circuit: {filename}")

        parser = CircuitParser(filename)
        graph, node_types = parser.parse()

        analyzer = CriticalPathAnalyzer(graph, node_types)
        critical_path, total_delay, path_components = analyzer.find_critical_path()

        print(f"Critical Path: {' -> '.join(critical_path)}")
        print(f"Total Delay: {total_delay:.2f} time units")
        print("Path Components:")
        for component in path_components:
            print(f"- {component}")

        visualizer = CircuitVisualizer(graph)
        visualizer.visualize(critical_path)

if __name__ == "__main__":
    main()
