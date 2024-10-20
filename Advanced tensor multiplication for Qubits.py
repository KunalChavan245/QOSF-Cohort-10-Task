import numpy as np
import time
import matplotlib.pyplot as plt

# Define the quantum gates as matrices
X = np.array([[0, 1], [1, 0]])  
H = (1 / np.sqrt(2)) * np.array([[1, 1], [1, -1]])  
CNOT = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
I = np.eye(2)  # Identity gate

def apply_1qubit_gate(state_tensor, gate, qubit, n_qubits):
    axes = list(range(n_qubits))
    axes.remove(qubit)
    return np.tensordot(gate, state_tensor, axes=([1], [qubit])).transpose(axes)

def apply_2qubit_gate(state_tensor, gate, control_qubit, target_qubit, n_qubits):
    axes = list(range(n_qubits))
    axes.remove(control_qubit)
    axes.remove(target_qubit)
    return np.tensordot(gate, state_tensor, axes=([1, 0], [control_qubit, target_qubit])).transpose(axes)

def initialize_state_tensor(n_qubits):
    state_tensor = np.zeros((2,) * n_qubits)
    state_tensor[(0,) * n_qubits] = 1  
    return state_tensor

# Function to simulate the quantum circuit with tensor multiplication
def simulate_circuit(n_qubits):
    state_tensor = initialize_state_tensor(n_qubits)
    
    state_tensor = apply_1qubit_gate(state_tensor, H, 0, n_qubits)
    
    if n_qubits > 1:
        state_tensor = apply_1qubit_gate(state_tensor, X, 1, n_qubits)
    
    if n_qubits > 1:
        state_tensor = apply_2qubit_gate(state_tensor, CNOT, 0, 1, n_qubits)
    
    return state_tensor

# Measure runtime
num_qubits = list(range(1, 12))  # From 1 to 11 qubits
runtimes = []

for n in num_qubits:
    start_time = time.time()
    simulate_circuit(n)
    end_time = time.time()
    runtimes.append(end_time - start_time)

# Plot runtime as a function of number of qubits
plt.plot(num_qubits, runtimes, label="Tensor Simulation Runtime")
plt.xlabel("Number of Qubits")
plt.ylabel("Runtime (seconds)")
plt.title("Quantum Circuit Simulation Runtime (Tensor Method)")
plt.legend()
plt.show()
