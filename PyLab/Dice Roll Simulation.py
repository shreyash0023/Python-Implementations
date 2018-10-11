'''Basic Simulation Model of Dice Roll'''

import random
import pylab as py

values = []
def printDice(n):
    for i in range(n):
        values.append(random.choice([0.0,1,],0.5))
        print str(values[i]) + '',


def plotDice():
    py.plot(values, 'ob')
    py.show()



printDice(100)
plotDice()
