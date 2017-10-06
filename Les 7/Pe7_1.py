
def sum():
    total = 0
    while True:
        getal = eval(input('Geef een getal: '))
        if getal == 0:
            break
        total += int(getal)
    print(total)

sum()





