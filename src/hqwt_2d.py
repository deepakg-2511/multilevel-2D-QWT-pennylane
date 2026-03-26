from HQWT_1D import qhaar_1d, qhaar_1d_inverse


def qhaar_2d(wires, spatial):
    """
    Single-level 2-D Haar Quantum Wavelet Transform
    """

    nx, ny = spatial

    x_wires = wires[:nx]
    y_wires = wires[nx:nx + ny]

    qhaar_1d(x_wires)

    qhaar_1d(y_wires)


def qhaar_2d_inverse(wires, spatial):

    nx, ny = spatial

    x_wires = wires[:nx]
    y_wires = wires[nx:nx + ny]

    qhaar_1d_inverse(y_wires)

    qhaar_1d_inverse(x_wires)