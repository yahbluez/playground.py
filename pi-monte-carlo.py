from random import random

def MonteCarloPI(versuche = 1000000):
    im = 0
    for loop in range(versuche):
        Xcord = random()
        Ycord = random()
        if(Xcord * Xcord + Ycord * Ycord <= 1):
            im += 1
    return(4 * im / versuche)


print(MonteCarloPI())
