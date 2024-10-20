import numpy as np
import time
import matplotlib.pyplot as plt

# Define the quantum gates as matrices
X = np.array([[0, 1], [1, 0]])
H = (1 / np.sqrt(2)) * np.array([[1, 1], [1, -1]])
CNOT = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
I = np.eye(2)

# Define the quantum circuit
def apply_circuit(n_qubits):
    # Create the initial state vector
    state_vector = np.zeros(2**n_qubits)
    state_vector[0] = 1  # Set the initial state to |000>

    # Apply the quantum gates sequentially
    for i in range(n_qubits):
        # Apply H gate to the i-th qubit
        state_vector = np.kron(np.eye(2**i), np.kron(H, np.eye(2**(n_qubits-i-1)))) @ state_vector

        # Apply CNOT gate with control qubit as the i-th qubit and target qubit as the (i+1)-th qubit
        if i < n_qubits - 1:
            state_vector = np.kron(np.eye(2**i), np.kron(CNOT, np.eye(2**(n_qubits-i-2)))) @ state_vector

        # Apply X gate to the i-th qubit
        state_vector = np.kron(np.eye(2**i), np.kron(X, np.eye(2**(n_qubits-i-1)))) @ state_vector

    return state_vector

# Measure the runtime for different number of qubits
n_qubits_list = range(1, 10)
runtimes = []

for n_qubits in n_qubits_list:
    start_time = time.time()
    apply_circuit(n_qubits)
    end_time = time.time()
    runtime = end_time - start_time
    runtimes.append(runtime)

# Plot the runtime as a function of the number of qubits
plt.plot(n_qubits_list, runtimes)
plt.xlabel('Number of Qubits')
plt.ylabel('Runtime (seconds)')
plt.title('Runtime of Quantum Circuit Simulation')
plt.show()



