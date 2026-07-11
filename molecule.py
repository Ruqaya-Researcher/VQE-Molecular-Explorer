
def choose_molecule():

    molecules = {

        1: {

            "name": "H2",

            "atoms": ["H", "H"]

        },

        2: {

            "name": "LiH",

            "atoms": ["Li", "H"]

        },

        3: {

            "name": "HeH+",

            "atoms": ["He", "H"]

        }

    }

    print("Available Molecules\n")

    for key, value in molecules.items():

        print(f"{key}. {value['name']}")

    choice = int(input("\nChoose Molecule: "))

    molecule = molecules[choice]

    charge = int(input("Charge: "))

    print("\nChoose Mapper")

    print("1. Jordan-Wigner")
    print("2. Parity")
    print("3. Bravyi-Kitaev")

    mapper = int(input("Choice: "))

    print("\nChoose Ansatz")

    print("1. EfficientSU2")
    print("2. TwoLocal")
    print("3. RealAmplitudes")

    ansatz = int(input("Choice: "))

    print("\nChoose Optimizer")

    print("1. COBYLA")
    print("2. SLSQP")
    print("3. SPSA")

    optimizer = int(input("Choice: "))

    return {

        "name": molecule["name"],

        "atoms": molecule["atoms"],

        "charge": charge,

        "mapper": mapper,

        "ansatz": ansatz,

        "optimizer": optimizer

    }
