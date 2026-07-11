
import numpy as np

from hamiltonian import build_hamiltonian
from ansatz import build_ansatz
from optimizer import build_optimizer
from estimator import build_estimator
from vqe import run_vqe


def optimize_geometry(molecule):

    # Default Geometry Scan

    distances = np.linspace(

        0.5,

        2.0,

        20

    )

    estimator = build_estimator()

    optimizer = build_optimizer(

        molecule

    )

    energies = []

    print("\nStarting Geometry Optimization...\n")

    for distance in distances:

        print(

          f"[{len(energies)+1}/20] Running VQE at {distance:.3f} Å"

)

        hamiltonian = build_hamiltonian(

            molecule,

            distance

        )

        ansatz = build_ansatz(

            hamiltonian,

            molecule

        )

        result = run_vqe(

            hamiltonian,

            ansatz,

            optimizer,

            estimator

        )

        energies.append(

            result.fun

        )

    best_index = np.argmin(

        energies

    )

    return {

        "distances": distances,

        "energies": energies,

        "best_distance": distances[best_index],

        "best_energy": energies[best_index]

    }
