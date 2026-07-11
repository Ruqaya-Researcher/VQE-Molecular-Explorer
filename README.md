
A modular implementation of the Variational Quantum Eigensolver (VQE) using Qiskit Nature to estimate the ground-state energy of the hydrogen molecule.

---

## Workflow

Molecule
↓
Electronic Structure
↓
Fermionic Hamiltonian
↓
Jordan–Wigner Mapping
↓
Pauli Hamiltonian
↓
Ansatz
↓
Estimator
↓
Classical Optimizer
↓
Ground State Energy

---

## Project Structure


```
project/

│── main.py
│── hamiltonian.py
│── ansatz.py
│── estimator.py
│── optimizer.py
│── vqe.py

│── README.md
│── requirements.txt
│── .gitignore
```

---

## Technologies

- Python
- Qiskit
- Qiskit Nature
- Qiskit IBM Runtime
- NumPy
- SciPy

---

## Goal

Estimate the electronic ground-state energy of the hydrogen molecule using the Variational Quantum Eigensolver (VQE).

---

## Future Improvements

- Support arbitrary molecules
- Geometry optimization
- Multiple ansätze
- Multiple optimizers
- Hardware execution on IBM Quantum
