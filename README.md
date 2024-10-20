<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Quantum Circuit Simulation Tasks</title>
</head>
<body>
    <h1>Quantum Circuit Simulation: Tasks</h1>
    <h2>Task 1: Naive Simulation using Matrix Multiplication</h2>
    <p>
        Implement a statevector simulator for quantum circuits using matrix multiplication. You will define quantum gates like X, H, and CNOT, 
        and apply them to a quantum state represented as a vector of length 2<sup>n</sup>. The gates will be applied sequentially to the statevector 
        via matrix multiplication using the Kronecker product (or similar functionality).
    </p>    
    <h3>Steps:</h3>
    <ol>
        <li>
            Define the common quantum gates (Identity, X, Hadamard, CNOT) as matrix representations.
        </li>
        <li>
            Use the Kronecker product (<code>np.kron</code> in NumPy) to create an n-qubit quantum statevector of length 2<sup>n</sup>.
        </li>
        <li>
            Initialize the statevector in the all-zero state <code>|00...0&gt;</code>.
        </li>
        <li>
            Sequentially apply the quantum gates (X, H, CNOT) to the statevector using matrix multiplication.
        </li>
        <li>
            Plot the runtime of the code as a function of the number of qubits.
        </li>
    </ol>
    <p>Answer the following:</p>
    <ul>
        <li>How many qubits can you simulate with this method?</li>
    </ul>
    <h2>Task 2: Advanced Simulation using Tensor Multiplication</h2>
    <p>
        Implement an advanced quantum circuit simulation using tensor multiplication. Instead of representing the quantum state as a vector, 
        you will use an n-dimensional tensor of shape (2, 2, ..., 2) to represent the n-qubit state. Apply 1-qubit and 2-qubit gates 
        (X, H, CNOT) via tensor contraction using <code>np.tensordot</code> or <code>np.einsum</code>.
    </p>
    <h3>Steps:</h3>
    <ol>
        <li>
            Define the quantum gates (Identity, X, H, CNOT) as matrices.
        </li>
        <li>
            Create a tensor to represent the initial quantum state with shape (2, 2, ..., 2).
        </li>
        <li>
            Apply the quantum gates sequentially to the state tensor using tensor multiplication.
        </li>
        <li>
            Plot the runtime of the code as a function of the number of qubits.
        </li>
    </ol>
    <p>Answer the following:</p>
    <ul>
        <li>How many qubits can you simulate using tensor multiplication?</li>
        <li>Compare the runtime results of this method with the matrix multiplication method in Task 1.</li>
    </ul>
</body>
</html>

