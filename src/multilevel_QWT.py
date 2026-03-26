import pennylane as qml
from .D4QWT_2D import qd4_2d, qd4_2d_inverse
from .permutations import P_2n_2, P_2_2n


# ------------------------------------------------
# helper
# ------------------------------------------------

def split_registers(wires, spatial):

    n, m = spatial

    wires = list(wires)

    x_wires = wires[:n]
    y_wires = wires[n:n+m]

    return x_wires, y_wires


# ------------------------------------------------
# T_nm_j  (Fig.8a)
# ------------------------------------------------

def T_nm_j(wires, spatial, j):

    n, m = spatial
    x_wires, y_wires = split_registers(wires, spatial)

    # controls (open circles)
    controls = x_wires[:j-1] + y_wires[:j-1]

    # active qubits
    active_x = x_wires[j-1:]
    active_y = y_wires[j-1:]

    active = active_x + active_y

    # permutation
    P_2n_2(active)

    # apply kernel
    if len(controls) == 0:

        qd4_2d(active, (len(active_x), len(active_y)))

    else:

        qml.ctrl(
            qd4_2d,
            control=controls,
            control_values=[0]*len(controls)
        )(active, (len(active_x), len(active_y)))


# ------------------------------------------------
# inverse T_nm_j  (Fig.8c)
# ------------------------------------------------

def T_nm_j_inverse(wires, spatial, j):

    n, m = spatial
    x_wires, y_wires = split_registers(wires, spatial)

    controls = x_wires[:j-1] + y_wires[:j-1]

    active_x = x_wires[j-1:]
    active_y = y_wires[j-1:]

    active = active_x + active_y

    if len(controls) == 0:

        qd4_2d_inverse(active, (len(active_x), len(active_y)))

    else:

        qml.ctrl(
            qd4_2d_inverse,
            control=controls,
            control_values=[0]*len(controls)
        )(active, (len(active_x), len(active_y)))

    P_2_2n(active)


# ------------------------------------------------
# R_nm_j (Fig.8b)
# ------------------------------------------------

def R_nm_j(wires, spatial, j):

    n, m = spatial

    x_wires, y_wires = split_registers(wires, spatial)

    active = x_wires[j-1:]

    P_2_2n(active)


# ------------------------------------------------
# inverse R_nm_j (Fig.8d)
# ------------------------------------------------

def R_nm_j_inverse(wires, spatial, j):

    n, m = spatial

    x_wires, y_wires = split_registers(wires, spatial)

    active = x_wires[j-1:]

    P_2n_2(active)


# ------------------------------------------------
# D_nm_j  (Fig.9a)
# ------------------------------------------------

def D_nm_j(wires, spatial, j):

    n, m = spatial

    if j == 1:

        # first level = full transform
        qd4_2d(wires, spatial)

    else:

        T_nm_j(wires, spatial, j)


# ------------------------------------------------
# inverse D_nm_j
# ------------------------------------------------

def D_nm_j_inverse(wires, spatial, j):

    n, m = spatial

    if j == 1:

        qd4_2d_inverse(wires, spatial)

    else:

        T_nm_j_inverse(wires, spatial, j)


# ------------------------------------------------
# L_nm_j  (Fig.9b)
# ------------------------------------------------

def L_nm_j(wires, spatial, j):

    if j >= 2:

        R_nm_j(wires, spatial, j)


# ------------------------------------------------
# inverse L_nm_j
# ------------------------------------------------

def L_nm_j_inverse(wires, spatial, j):

    if j >= 2:

        R_nm_j_inverse(wires, spatial, j)


# ------------------------------------------------
# MULTILEVEL TRANSFORM  (Fig.11)
# ------------------------------------------------

def multilevel_qwt(wires, spatial, levels):

    # forward stage
    for j in range(1, levels+1):

        D_nm_j(wires, spatial, j)

    # shuffle stage
    for j in range(1, levels+1):

        L_nm_j(wires, spatial, j)


# ------------------------------------------------
# inverse multilevel transform
# ------------------------------------------------

def multilevel_qwt_inverse(wires, spatial, levels):

    for j in reversed(range(1, levels+1)):

        L_nm_j_inverse(wires, spatial, j)

    for j in reversed(range(1, levels+1)):

        D_nm_j_inverse(wires, spatial, j)