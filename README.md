# Digital-Circuit-Critical-Path-Analysis

## Overview

The Digital Circuit Critical Path Analyzer is a Python-based tool that analyzes digital circuits to determine their critical paths. The critical path is the longest path through combinational logic elements, which determines the maximum operating frequency of the circuit.

This tool supports both combinational and sequential circuits, and it:

- Calculates the critical path and its delay.
- Outputs the individual components of the critical path with their delays.
- Visualizes the circuit and highlights the critical path using NetworkX.

## Features

- Parses circuit descriptions from text files.
- Calculates delays for various circuit components:
  - Adder (ADD): 1.0 time unit
  - Multiplier (MUL): 1.0 time unit
  - Register (REG): 0.2 time unit
  - Multiplexor (MUX): 1.0 time unit
- Handles sequential circuits with registers.
- Visualizes the circuit graph and highlights the critical path.

## File Structure

```project/
├── circuit_parser.py # Handles parsing circuit files and building the graph
├── critical_path.py # Analyzes the circuit and calculates the critical path
├── visualizer.py # Visualizes the circuit and critical path
├── main.py # Entry point for the program
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/styxofsyntax/Digital-Circuit-Critical-Path-Analysis
cd Digital-Circuit-Critical-Path-Analysis
```

2.  Install dependencies:

```bash
pip install -r requirements.txt
```

3. Save your circuit files in the project directory.

## Usage

1. Place your circuit description files in the project directory (e.g., circuit1.txt, circuit2.txt).

2. Run the program:

```bash
python main.py
```

3. The program will:
   - Parse each circuit file.
   - Calculate the critical path and its delay.
   - Print the results to the console.
   - Display a visualization of the circuit with the critical path highlighted.

## Circuit Description Format

Circuit files must follow this format:

- **Inputs**: Defined with INPUT followed by a node ID.
- **Outputs**: Defined with OUTPUT followed by a node ID and its input node.
- **Components**: Adders, multipliers, registers, and multiplexors are specified as follows:

```plaintext
<component_type> <node_id> <input_nodes...>
```

## Example Circuit File

```plaintext
INPUT in1
INPUT in2
INPUT in3
ADD add1 in1 in2
MUL mul1 add1 in3
REG reg1 mul1
ADD add2 reg1 in2
MUX mux1 add2 in3
OUTPUT out1 mux1
```

## Example Output

For the above circuit, the output will be:

Critical Path: in1 -> add1 -> mul1 -> reg1 -> add2 -> mux1 -> out1
Total Delay: 6.20 time units
Path Components:

- INPUT (in1): 1.0 tu
- ADD (add1): 1.0 tu
- MUL (mul1): 1.0 tu
- REG (reg1): 0.2 tu
- ADD (add2): 1.0 tu
- MUX (mux1): 1.0 tu
- OUTPUT (out1): 1.0 tu

A visualization of the circuit with the critical path highlighted in red will also be displayed.

## Dependencies

- networkx: For graph representation and topological sorting.
- matplotlib: For visualizing the circuit.

Install these dependencies using:

```bash
pip install networkx matplotlib
```
