# Multilevel 2D Quantum Wavelet Transform (QWT) using PennyLane

This repository contains an implementation of **Quantum Wavelet Transforms (QWT)** based on the paper:

**H.-S. Li, P. Fan, H. Peng, S. Song, G.-L. Long,**
*"Multilevel 2-d quantum wavelet transforms"*,
IEEE Transactions on Cybernetics, 52 (8) (2021) 8467–8480.
---

##  Overview

Wavelet transforms are fundamental tools in classical signal and image processing. This project implements their **quantum counterparts**, which provide **exponential speedup** by operating on quantum states.

The focus of this repository is:

* Quantum circuit construction of wavelet transforms
* Implementation of core operators such as `D_{2^n}^p` and permutation operators
* Extension from **1D QWT → 2D QWT → Multilevel QWT**

---

##  Background (Simplified Theory)

### 1. Quantum State Representation (NASS)

A classical image or signal is encoded into a quantum state:

ψ = Σ₍x,y₎ θ₍x,y₎ |x⟩|y⟩

This is called a **Normal Arbitrary Superposition State (NASS)**.

 Advantage:
A (2^n × 2^m) image is stored using only (n + m) qubits.

---

### 2. Key Operator: D₂ⁿᵖ

The D-operator is the **core building block** of the Daubechies (D4) quantum wavelet transform:

D₂ⁿᵖ = (I ⊗ S₁) · Q₂ⁿ · (I ⊗ S₀) · Q₂ⁿ⁻¹

* Q₂ⁿ → permutation operator (triangular controlled circuit)
* S₀, S₁ → single-qubit rotations

 In this project, this operator is implemented using:

* Multi-controlled X gates (control on 0)
* Decomposition of S₀ and S₁ into rotation gates (RY + Z)

---

### 3. 1D Quantum Wavelet Transform

Two main types:

#### Haar QWT

W₂ⁿᴴ = P₂ⁿ⁻¹,₂ (I ⊗ H)

#### Daubechies D4 QWT

F₂ⁿ = P₂ⁿ⁻¹,₂ · D₂ⁿᵖ

---

### 4. 2D Quantum Wavelet Transform

The 2D QWT is constructed as:

W₂ⁿ ⊗ W₂ᵐ

 This applies wavelet transform along both spatial dimensions.

---

### 5. Multilevel QWT

The transform is applied **recursively**, producing multi-scale decomposition:

* Level 1 → coarse + detail components
* Level 2 → further decomposition
* Higher levels → hierarchical structure

In this implementation, multilevel QWT is achieved by:

* Applying QWT on the full system (level 1)
* Recursively applying QWT on reduced subsets of qubits
* Restricting operations to progressively smaller subspaces (low-frequency components)

This avoids explicit control-based constructions and follows a **domain-reduction approach** consistent with circuit constraints.

---

##  Implemented Components

###  Core Operators

* `D_{2^n}^p` operator (fully implemented)
* `Q_{2^n}` permutation operator (triangular circuit)
* Controlled gates with control on 0

---

###  1D Quantum Wavelet Transforms

* Haar QWT
* Daubechies D4 QWT

---

###  2D Quantum Wavelet Transform

* Tensor-product construction: W₂ⁿ ⊗ W₂ᵐ
* Circuit-level implementation using PennyLane

---

###  Multilevel QWT

* Multilevel Haar QWT (1D and 2D)
* Multilevel D4 QWT (1D and 2D)
* Inverse multilevel transforms implemented
* Reconstruction validation (forward + inverse consistency)

---

###  Circuit Design Features

* Multi-controlled gates with ancilla support
* Gate decomposition (no large unitary matrices)
* Fully compatible with PennyLane simulation

---

##  Project Structure

```
src/
    d4qwt_1d.py
    d4qwt_2d.py
    hqwt_1d.py
    hqwt_2d.py
    permutations.py
    encoding.py
    multilevel_qwt.py

notebooks/
    test.ipynb
```

---

## ▶ How to Run

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

##  Key Insights from Paper

Quantum wavelet transforms achieve:

O((n + m)^3)

compared to classical complexity:

O(2^(n + m))

 This provides **exponential speedup**.

---

## 📖 Reference

Li, H.-S., Fan, P., Peng, H., Song, S., & Long, G.-L. (2022).
**Multilevel 2-D Quantum Wavelet Transforms**.
IEEE Transactions on Cybernetics.

---

##  Author

Deepak Gupta
Computational & data Sciences
Indian Institute of Science (IISc)

---