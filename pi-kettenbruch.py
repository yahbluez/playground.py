

Tiefe = 42
def Kettenbruch(Summand, Nenner):
    if(Nenner == Tiefe):
        return(Summand + Nenner **2)
    else:
        return(Summand + Nenner **2 / Kettenbruch(Summand +2, Nenner +1))


def KettenbruchPI(Tiefe = 42):
    return(4 / Kettenbruch(1, 1))

print(KettenbruchPI())



