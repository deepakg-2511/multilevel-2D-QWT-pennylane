from src.d4qwt_1d import F_2n, F_2n_inverse


def qd4_2d(wires, spatial):
    """
    Single-level 2-D D4 quantum wavelet transform
    """

    nx, ny = spatial

    x_wires = wires[:nx]
    y_wires = wires[nx:nx+ny]

    F_2n(x_wires)
    F_2n(y_wires)


def qd4_2d_inverse(wires, spatial):
    """
    Inverse 2-D D4 quantum wavelet transform
    """

    nx, ny = spatial

    x_wires = wires[:nx]
    y_wires = wires[nx:nx+ny]

    F_2n_inverse(y_wires)
    F_2n_inverse(x_wires)