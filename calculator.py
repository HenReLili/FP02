"""
calculates the maximum and minimum of a measurement,
if on every maximum follows a minimum
"""


def maxcalc(data):
    """
    Args:

    Returns:
    """

    maxis = []
    minis = []
    intmaxis = []
    intminis = []
    minmax = True
    counter = 0
    xmin = 100
    xmax = 0

    for i in range(int(data.size/len(data))-xmin-xmax-1):
        if minmax:
            if data[1, i+1+xmin] > data[1, i+xmin]:
                maxi = data[0, i+1+xmin]
                intmaxi = data[1, i+1+xmin]
            else:
                counter += 1
        else:
            if data[1, i+1+xmin] < data[1, i+xmin]:
                mini = data[0, i+1+xmin]
                intmini = data[1, i+1+xmin]
            else:
                counter += 1

        if counter == 10:
            counter = 0
            if minmax:
                maxis.append(maxi)
                intmaxis.append(intmaxi)
                minmax = False
            else:
                minis.append(mini)
                intminis.append(intmini)
                minmax = True
    return minis, maxis, intmaxis, intminis
