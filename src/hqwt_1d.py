import pennylane as qml
from permutations import P_2n_2, P_2_2n


def qhaar_1d(wires):
    """
    Single-level 1-D Haar Quantum Wavelet Transform
    """

    n = len(wires)

    if n == 1:
        qml.Hadamard(wires=wires[0])
        return

    qml.Hadamard(wires=wires[-1])

    P_2n_2(wires)


def qhaar_1d_inverse(wires):
    """
    Inverse Haar QWT
    """

    n = len(wires)

    if n == 1:
        qml.Hadamard(wires=wires[0])
        return

    P_2_2n(wires)

    qml.Hadamard(wires=wires[-1])