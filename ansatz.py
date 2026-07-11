
from qiskit.circuit.library import (

    EfficientSU2,

    TwoLocal,

    RealAmplitudes

)


def build_ansatz(

    hamiltonian,

    molecule

):

    choice = molecule["ansatz"]

    if choice == 1:

        ansatz = EfficientSU2(

            num_qubits=hamiltonian.num_qubits,

            reps=2,

            entanglement="linear"

        )

    elif choice == 2:

        ansatz = TwoLocal(

            num_qubits=hamiltonian.num_qubits,

            rotation_blocks="ry",

            entanglement_blocks="cx",

            reps=2

        )

    else:

        ansatz = RealAmplitudes(

            num_qubits=hamiltonian.num_qubits,

            reps=2

        )

    return ansatz
