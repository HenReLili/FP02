"""

"""

import matplotlib.pyplot as plt


def plotting(increases, increasesabw, energies, abwenergies):

    plt.rcParams["figure.figsize"] = [9, 11]
#    plt.xlim(energies[72], energies[0])
#    plt.xlim(1.933, 1.95)
#    plt.ylim(-310, -130)
    plt.plot(energies, increases)
#    plt.errorbar(energies, increases, yerr=increasesabw, xerr=abwenergies, marker=".", linewidth=0, elinewidth=2)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.xlabel("Energie der Photonen in eV", fontsize=20)
    plt.ylabel("Intensität (willkürliche Einheiten)", fontsize=20)
    plt.show()
