import pennylane as qml
from src.hqwt_1d import qhaar_1d
from src.hqwt_1d import qhaar_1d_inverse
from src.hqwt_2d import qhaar_2d
from src.hqwt_2d import qhaar_2d_inverse

from src.d4qwt_2d import qd4_2d
from src.d4qwt_2d import qd4_2d_inverse
from src.d4qwt_1d import F_2n
from src.d4qwt_1d import F_2n_inverse





def controlled_block(unitary_fn, wires, control_qubits):
    """
    Apply unitary_fn controlled on control_qubits == 0
    """
    def block():
        unitary_fn(wires)
    qml.ctrl(block, control=control_qubits,
             control_values=[0]*len(control_qubits))()
    
################# Multilevel Haar 1D Transforms #################

def multilevel_haar_1d(wires, levels):
    n = len(wires)
    for level in range(levels):
        active_wires = wires[level:]  
        if len(active_wires) <= 1:
            break
        qhaar_1d(active_wires)

def multilevel_haar_1d_inverse(wires, levels):
    wires = list(wires)
    for level in reversed(range(levels)):
        active_wires = wires[level:]
        if len(active_wires) <= 1:
            continue
        qhaar_1d_inverse(active_wires)


################# Multilevel Haar 2D Transforms #################

def multilevel_haar_2d(wires, spatial, levels):
    wires = list(wires)   
    n, m = spatial
    for level in range(levels):
        x_active = wires[level:n]
        y_active = wires[n+level:n+m]
        active_wires = list(x_active) + list(y_active)   
        active_spatial = (len(x_active), len(y_active))
        if len(active_wires) <= 2:
            break
        qhaar_2d(active_wires, active_spatial)



def multilevel_haar_2d_inverse(wires, spatial, levels):
    wires = list(wires)
    n, m = spatial
    for level in reversed(range(levels)):
        x_active = wires[level:n]
        y_active = wires[n+level:n+m]
        active_wires = list(x_active) + list(y_active)
        active_spatial = (len(x_active), len(y_active))
        if len(active_wires) <= 2:
            continue
        qhaar_2d_inverse(active_wires, active_spatial)





################# Multilevel D4 1D Transforms #################

def multilevel_d4_1d(wires, levels):
    n = len(wires)
    for level in range(levels):
        active_wires = wires[level:]
        if len(active_wires) <= 1:
            break
        F_2n(active_wires)


def multilevel_d4_1d_inverse(wires, levels):
    wires = list(wires)
    for level in reversed(range(levels)):
        active_wires = wires[level:]
        if len(active_wires) <= 1:
            continue
        F_2n_inverse(active_wires)




################# Multilevel Haar 2D Transforms #################

def multilevel_d4_2d(wires, spatial, levels):
    wires = list(wires)   
    n, m = spatial
    for level in range(levels):
        x_active = wires[level:n]
        y_active = wires[n+level:n+m]
        active_wires = list(x_active) + list(y_active)
        active_spatial = (len(x_active), len(y_active))
        if len(active_wires) <= 2:
            break
        qd4_2d(active_wires, active_spatial)


def multilevel_d4_2d_inverse(wires, spatial, levels):
    wires = list(wires)
    n, m = spatial
    for level in reversed(range(levels)):
        x_active = wires[level:n]
        y_active = wires[n+level:n+m]
        active_wires = list(x_active) + list(y_active)
        active_spatial = (len(x_active), len(y_active))
        if len(active_wires) <= 2:
            continue
        qd4_2d_inverse(active_wires, active_spatial)
        
