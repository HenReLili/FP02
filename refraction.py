"""
calculates the maximum and minimum of a measurement,
if on every maximum follows a minimum
"""

import numpy as np


def ncalc(minis, maxis, intmaxis, intminis):
    refracs = []
    increases = []
    increasesabw = []
    energies = []
    abwenergies = []
    medrefrac = 0
    abw = 0
    for i in range(len(maxis)-1):
        refrac = 1/(2*3*10**(-4)*(1/maxis[i]-1/maxis[i+1])*10**(9))
        refracs.append(refrac)
        medrefrac += refrac
    medrefrac = medrefrac/len(refracs)
    abws = (refracs - medrefrac)**2
    for j in range(len(refracs)):
        abw += abws[j]
    abw = np.sqrt(abw/(len(refracs)-1))
    R = ((refrac-1)/(refrac+1))**2
    Rabw = 2*R*(abw/(refrac-1)+abw/(refrac+1))

    for k in range(len(intminis)):
        increases.append((np.log((np.sqrt(intmaxis[k])-np.sqrt(intminis[k]))/(np.sqrt(intmaxis[k])+np.sqrt(intminis[k]))/R)/(3*10**(-4))+0.03)/100)
#        abwbruch = 0.015*(np.sqrt(intmaxis[k])+np.sqrt(intminis[k]))*(1/(intmaxis[k]+np.sqrt(intminis[k]))+1/(intmaxis[k]-np.sqrt(intminis[k])))+Rabw/R
        abwbruch = 0.015*((np.sqrt(intmaxis[k])+np.sqrt(intminis[k]))/(np.sqrt(intmaxis[k])-np.sqrt(intminis[k])))+Rabw/R
#        increasesabw.append(abwbruch/(((np.sqrt(intmaxis[k])-np.sqrt(intminis[k]))/(np.sqrt(intmaxis[k])+np.sqrt(intminis[k]))/R)*3*10**(-4)))
        increasesabw.append(abwbruch)
    for l in range(len(minis)):
        energy = 299792458 * 6.626*10**(-34)/minis[l]/(1.602*10**(-19))*10**9
        energies.append(energy)
        abwenergy = 0.0001 * energy
        abwenergies.append(abwenergy)

    return medrefrac, abw, R, Rabw, increases, increasesabw, energies, abwenergies
