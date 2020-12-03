# qiskit2tex

## About
This python program aims at easing the workflow of everybody who wishes to create TeX-based graphics of Quantum circuits from [Qiskit](https://github.com/Qiskit/qiskit) source code files to include in complex TeX documents in an effortless manner.

For this purpose, it leverages the built-in function `QuantumCircuit.draw()` of the Qiskit package terra. It takes one Qiskit (`.py`) input file including the target circuit and outputs a `.tex` file ready to be included in a TeX document structure.

## Prerequisites
- python3
- usage of package `qcircuit` in preambel of tex document
```
\usepackage[qm]{qcircuit} % for qcircuits
```


## Setup
1. download the `qiskit2tex.py` file
1. move it into the folder where the qiskit circuit files reside (NOTE: one file per circuit, each circuit needs to be assigned to a variable named 'qc', the folder must be declared a python module requiring the existence of a `__init__.py` file (can be empty))
1. open command line interface, move to directory of qiskit files and `qiskit2tex.py`
```
cd /my/dir/
```
1. execute qiskit2tex.py passing the file name (w/o ending) of the target circuit to be compiled into a tex file and the output directory as arguments (leaving the output directory empty will save the tex file in the input directory)
```
# python3 qiskit2tex.py "my_circuit"
python3 qiskit2tex.py "my_circuit" "my/out/dir/"
```
1. include the tex files in your TeX document, e.g.
```
\begin{figure}
\input{my_circuit.tex}
\caption[My circuit created qiskit2tex]{My circuit created qiskit2tex}
\end{figure}
```

---
This package was created by Lennart Schulze, IBM Quantum Ambassador and Qiskit Advocate.
