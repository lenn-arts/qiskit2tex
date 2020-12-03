ghz_backend1 = QuantumCircuit(3,3, name=f"sample") # note usage of 5 qubits to match the configuration of the device
ghz_backend1.h(1) # map qubit 0 to qubit 1 and qubit 1 to qubit 0 ..
ghz_backend1.x(0) # .. to ensure that all logical CNOT gates are performed on physical connections
ghz_backend1.y(2)
ghz_backend1.measure(range(3), range(3)) # readout in order of mapping
qc = ghz_backend1
