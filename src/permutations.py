import pennylane as qml


def P_2n_2(wires):
    """
    Perfect shuffle permutation P_(2^(n-1),2)
    """

    n = len(wires)

    for i in reversed(range(n - 1)):
        qml.SWAP(wires=[wires[i], wires[i + 1]])


def P_2_2n(wires):
    """
    Perfect shuffle permutation P_(2,2^(n-1))
    """

    n = len(wires)

    for i in range(n - 1):
        qml.SWAP(wires=[wires[i], wires[i + 1]])