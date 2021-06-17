"""
Executing the programm.
"""

import dataorganisator
import calculator
import refraction
import plot

import matplotlib.pyplot as plt


def main():
    for datanumber in range(1, 7):
        data = dataorganisator.datareader(datanumber)
        minis, maxis, intmaxis, intminis = calculator.maxcalc(data)
        medrefrac, abw, R, Rabw, increases, increasesabw, energies, abwenergies =refraction.ncalc(minis, maxis, intmaxis, intminis)
        print(increasesabw)
#        print(R)
#        print(Rabw)
        plot.plotting(data[1,:], increasesabw, 299792458 * 6.626*10**(-34)/data[0,:]/(1.602*10**(-19))*10**9, abwenergies)
    plt.plot(data[0,800:1000], data[1,800:1000])
    plt.show()
    plt.plot(data[0,:], data[1,:])
    plt.show()
#    print(abwenergies)
#    print(increasesabw)
#    print(len(increases))
#    print(energies)
#    print("maxi: ", maxis)
#    print("energy: ", energies[0])

if __name__ == "__main__":
    main()
