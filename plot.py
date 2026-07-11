
import matplotlib.pyplot as plt


def plot_energy(result):

    plt.figure(figsize=(8,5))

    plt.plot(

        result["distances"],

        result["energies"],

        marker="o",

        linewidth=2

    )

    plt.scatter(

        result["best_distance"],

        result["best_energy"],

        s=120

    )

    plt.xlabel(

        "Bond Length (Å)"

    )

    plt.ylabel(

        "Ground State Energy (Ha)"

    )

    plt.title(

        "Geometry Optimization"

    )

    plt.grid(True)

    plt.show()
