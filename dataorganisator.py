"""
reads data
"""

import os.path
import numpy as np


def datareader(datanumber):
    """Reads the data of a measurement from dataname
    Args: dataname is the name of the .txt-file wich data is to be read

    Returns: data is the data of the measurement in a numpy-array
    """

    wavelengths = []
    intensity = []

    dataname = "spektrum{number}.txt".format(number=datanumber)
    fp = open(os.path.join("measurements", dataname))
    readdata = fp.read().split()
    fp.close
    for i in range(len(readdata)):
        readdata[i] = float(readdata[i].replace(",", "."))
        if i % 2 == 0:
            wavelengths.append(readdata[i])
        else:
            intensity.append(readdata[i])
    data = np.zeros((2, len(wavelengths)))
    data[0, :] = wavelengths
    data[1, :] = intensity

    return data
