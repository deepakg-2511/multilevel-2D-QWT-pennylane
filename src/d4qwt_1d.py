import pennylane as qml
import numpy as np
from src.permutations import P_2n_2, P_2_2n

S0 = np.array([
    [np.sin(2*np.pi/3), np.cos(2*np.pi/3)],
    [np.cos(2*np.pi/3), -np.sin(2*np.pi/3)]
])

S1 = np.array([
    [-np.sin(5*np.pi/12), np.cos(5*np.pi/12)],
    [np.cos(5*np.pi/12),  np.sin(5*np.pi/12)]
])


# -------------------------------------------------
# Gates
# -------------------------------------------------

def S0_gate(wire):
    qml.QubitUnitary(S0, wires=wire)


def S1_gate(wire):
    qml.QubitUnitary(S1, wires=wire)


# -------------------------------------------------
# Triangular control network Q_{2^n}
# -------------------------------------------------

def triangular_forward(wires):
    n = len(wires)
    for k in range(n-1):
        active = wires[-(k+2):][::-1]
        qml.MultiControlledX(
            wires=active,
            control_values=[0]*(len(active)-1)
        )


def triangular_reverse(wires):
    n = len(wires)
    for k in range(n-2, -1, -1):
        active = wires[-(k+2):][::-1]
        qml.MultiControlledX(
            wires=active,
            control_values=[0]*(len(active)-1)
        )


# -------------------------------------------------
# D_{2^n}^p operator (Fig.4)
# -------------------------------------------------

def Dp_2n(wires):

    qml.PauliX(wires[-1])
    triangular_forward(wires)
    S0_gate(wires[-1])
    triangular_reverse(wires)
    qml.PauliX(wires[-1])
    S1_gate(wires[-1])


def Dp_2n_inverse(wires):
    
    S1_gate(wires[-1])
    qml.PauliX(wires[-1])
    triangular_forward(wires)
    S0_gate(wires[-1])
    triangular_reverse(wires)
    qml.PauliX(wires[-1])

# -------------------------------------------------
# 1-D D4 QWT  (paper Eq.)
# -------------------------------------------------

def F_2n(wires):
    """
    Forward 1-D D4 quantum wavelet transform
    """
    Dp_2n(wires)
    P_2n_2(wires)


def F_2n_inverse(wires):
    """
    Inverse 1-D D4 quantum wavelet transform
    """
    P_2_2n(wires)
    Dp_2n_inverse(wires)