# Multilevel 2D Quantum Wavelet Transform (QWT) using PennyLane

This repository contains an implementation of **Quantum Wavelet Transforms (QWT)** based on the paper:

**Hai-Sheng Li et al.,**
*"Multilevel 2-D Quantum Wavelet Transforms"*,
IEEE Transactions on Cybernetics, 2022.

---

## 📌 Overview

Wavelet transforms are fundamental tools in classical signal and image processing. This project implements their **quantum counterparts**, which provide **exponential speedup** by operating on quantum states.

The focus of this repository is:

* Quantum circuit construction of wavelet transforms
* Implementation of core operators such as ( D_{2^n}^{p} ) and permutation operators
* Extension from **1D QWT → 2D QWT → Multilevel QWT**

---

## 🧠 Background (Simplified Theory)

### 1. Quantum State Representation (NASS)

A classical image or signal is encoded into a quantum state:

[
|\psi\rangle = \sum_{x,y} \theta_{x,y} |x\rangle |y\rangle
]

This is called a **Normal Arbitrary Superposition State (NASS)**.

👉 Advantage:
A (2^n \times 2^m) image is stored using only (n+m) qubits.

---

### 2. Key Operator: ( D_{2^n}^{p} )

The D-operator is the **core building block** of the Daubechies (D4) quantum wavelet transform:

[
D_{2^n}^{p} = (I \otimes S_1), Q_{2^n}, (I \otimes S_0), Q_{2^n}^{-1}
]

* (Q_{2^n}): permutation operator (implemented via triangular controlled gates)
* (S_0, S_1): single-qubit rotations

👉 In this project, this operator is implemented using:

* Multi-controlled X gates (with control on 0)
* Decomposition of (S_0, S_1) into native rotation gates

---

### 3. 1D Quantum Wavelet Transform

Two main types:

#### Haar QWT:

[
W_{2^n}^{H} = P_{2^{n-1},2} (I \otimes H)
]

#### Daubechies D4 QWT:

[
F_{2^n} = P_{2^{n-1},2} \cdot D_{2^n}^{p}
]

---

### 4. 2D Quantum Wavelet Transform

The 2D QWT is constructed as:

[
W_{2^n} \otimes W_{2^m}
]

👉 This applies wavelet transform across both spatial dimensions.

---

### 5. Multilevel QWT

The transform is applied **recursively**, producing multi-scale decomposition:

* Level 1 → coarse + detail components
* Level 2 → further decomposition of coarse part
* …

This is implemented using operators:

[
Q_f^i(2^n,2^m), \quad Q_s^i(2^n,2^m)
]

which involve:

* permutation operators
* tensor structures
* recursive circuit construction

---

## ✅ Implemented Components

### ✔ Core Operators

* ( D_{2^n}^{p} ) operator (fully implemented)
* ( Q_{2^n} ) permutation operator (triangular circuit)
* Controlled gates with control on 0

---

### ✔ 1D Quantum Wavelet Transforms

* Haar QWT
* Daubechies D4 QWT

---

### ✔ 2D Quantum Wavelet Transform

* Tensor-product construction ( W_{2^n} \otimes W_{2^m} )
* Circuit-level implementation using PennyLane

---

### ✔ Circuit Design Features

* Multi-controlled gates with ancilla support
* Gate decomposition (no use of large unitary matrices)
* Fully compatible with PennyLane simulation

---

## 📂 Project Structure

```
src/
    d4qwt_1d.py
    d4qwt_2d.py
    hqwt_1d.py
    hqwt_2d.py
    permutations.py
    encoding.py
    multilevel_QWT.py

notebooks/
    test.ipynb

results/
    IISc.png
```

---

## ▶️ How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run example:

```python
import pennylane as qml

qml.draw_mpl(circuit)()
```

---

## 📊 Key Insights from Paper

* Quantum wavelet transforms achieve:
  [
  \mathcal{O}((n+m)^3)
  ]
  complexity

compared to classical:
[
\mathcal{O}(2^{n+m})
]

👉 This gives **exponential speedup**.

---

## 🚀 Future Work

* [ ] Full multilevel 2D QWT implementation
* [ ] Iterative circuit construction (Section III-C of paper)
* [ ] Quantum image compression algorithm
* [ ] Performance benchmarking vs classical wavelets
* [ ] Integration with quantum machine learning models

---

## 📖 Reference

Li, H.-S., Fan, P., Peng, H., Song, S., & Long, G.-L. (2022).
**Multilevel 2-D Quantum Wavelet Transforms**.
IEEE Transactions on Cybernetics.

---

## 🙌 Author

Deepak Gupta
Indian Institute of Science (IISc)

---

## ⭐ Note

This project is part of ongoing research in:

* Quantum signal processing
* Quantum machine learning
* Quantum PDE solvers
