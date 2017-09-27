


def gemmidelde():
    woorden = input('Geef een zin op: ')
    woorden = woorden.split()
    gemmideld = sum(len(woord) for woord in woorden) /len(woorden)
    print (gemmideld)


gemmidelde()
