import pennylane as qml
import numpy as np


class QuantumImageEncoder:
    """
    Prepare NASS quantum state for grayscale matrix
    or RGB tensor.

    Designed to integrate directly with QWT circuits.
    """

    # ----------------------------
    # Utility
    # ----------------------------

    @staticmethod
    def _is_power_of_two(x):
        return (x & (x - 1) == 0) and x != 0

    @staticmethod
    def _normalize(v):
        norm = np.linalg.norm(v)
        if norm == 0:
            raise ValueError("Input cannot be zero")
        return v / norm


    # ----------------------------
    # Grayscale Encoding
    # ----------------------------

    @staticmethod
    def encode_grayscale(matrix):

        matrix = np.array(matrix, dtype=float)

        H, W = matrix.shape

        if not QuantumImageEncoder._is_power_of_two(H):
            raise ValueError("Height must be power of 2")

        if not QuantumImageEncoder._is_power_of_two(W):
            raise ValueError("Width must be power of 2")

        nx = int(np.log2(H))
        ny = int(np.log2(W))

        flat = matrix.flatten()

        state = QuantumImageEncoder._normalize(flat)

        n_qubits = nx + ny

        dev = qml.device("default.qubit", wires=n_qubits)

        @qml.qnode(dev)
        def circuit():

            qml.AmplitudeEmbedding(
                features=state,
                wires=range(n_qubits),
                normalize=False
            )

            return qml.state()

        return circuit, n_qubits, (nx, ny)


    # ----------------------------
    # RGB Encoding
    # ----------------------------

    @staticmethod
    def encode_rgb(tensor):

        tensor = np.array(tensor, dtype=float)

        H, W, C = tensor.shape

        if C != 3:
            raise ValueError("Tensor must be H×W×3")

        if not QuantumImageEncoder._is_power_of_two(H):
            raise ValueError("Height must be power of 2")

        if not QuantumImageEncoder._is_power_of_two(W):
            raise ValueError("Width must be power of 2")

        nx = int(np.log2(H))
        ny = int(np.log2(W))

        spatial_states = H * W
        total_states = spatial_states * 4

        state = np.zeros(total_states)

        for x in range(H):
            for y in range(W):

                base = (x * W + y) * 4

                state[base + 1] = tensor[x, y, 0]  # Red
                state[base + 2] = tensor[x, y, 1]  # Green
                state[base + 3] = tensor[x, y, 2]  # Blue

        state = QuantumImageEncoder._normalize(state)

        n_qubits = nx + ny + 2

        dev = qml.device("default.qubit", wires=n_qubits)

        @qml.qnode(dev)
        def circuit():

            qml.AmplitudeEmbedding(
                features=state,
                wires=range(n_qubits),
                normalize=False
            )

            return qml.state()

        return circuit, n_qubits, (nx, ny)