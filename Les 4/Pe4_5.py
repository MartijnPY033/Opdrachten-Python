import math
grondgetallen = [4,5,3,-81]


def kwadraten_som():
    nummers = []
    for i in grondgetallen:
        if i >= 0:
            nummers.append(i**2)
            x = sum(nummers)
    print(nummers)
    print(x)


kwadraten_som()

