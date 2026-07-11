
from qiskit_nature.second_q.drivers import PySCFDriver
from qiskit_nature.units import DistanceUnit

from qiskit_nature.second_q.mappers import (
    JordanWignerMapper,
    ParityMapper,
    BravyiKitaevMapper
)


def build_hamiltonian(molecule, distance):

    atom1 = molecule["atoms"][0]
    atom2 = molecule["atoms"][1]

    atom_string = (
        f"{atom1} 0 0 0;"
        f"{atom2} 0 0 {distance}"
    )

    atomic_numbers = {
        "H": 1,
        "He": 2,
        "Li": 3
    }

    electrons = (
        atomic_numbers[atom1]
        + atomic_numbers[atom2]
        - molecule["charge"]
    )

    # Spin المناسب تلقائيًا
    spin = electrons % 2

    driver = PySCFDriver(

        atom=atom_string,

        basis="sto3g",

        charge=molecule["charge"],

        spin=spin,

        unit=DistanceUnit.ANGSTROM

    )

    problem = driver.run()

    fermionic_hamiltonian = problem.hamiltonian.second_q_op()

    mapper_choice = molecule["mapper"]

    if mapper_choice == 1:

        mapper = JordanWignerMapper()

    elif mapper_choice == 2:

        mapper = ParityMapper()

    else:

        mapper = BravyiKitaevMapper()

    qubit_hamiltonian = mapper.map(
        fermionic_hamiltonian
    )

    return qubit_hamiltonian
