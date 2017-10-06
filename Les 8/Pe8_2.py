import random


def monopolyworp():
    Dubbel = 0
    while True:
        Dobbel1 = random.randint(1,6)
        Dobbel2 = random.randint(1,6)

        uitkomst = Dobbel1 + Dobbel2
        if Dobbel1 == Dobbel2 and Dubbel <3:
            print(Dobbel1, '+', Dobbel2, '=', uitkomst, 'dubbel')
            Dubbel = Dubbel + 1
            continue
        elif Dobbel1 != Dobbel2 and Dubbel <3:
            print(Dobbel1, '+', Dobbel2, '=', uitkomst)
            gooien = input('Wil je nog een keer gooien: ')
            if gooien == 'ja' or 'JA' or 'Ja':
                continue
            else:
                break
        elif Dubbel >=3:
            print ('Je gaat naar de gevangenis')
            break

        return uitkomst








#def gooi_opnieuw():
    #while True:
        #OpnieuwGooien = str(input('Wil je op nieuw gooien Y OF N : '))
        #if OpnieuwGooien == 'Y':
            #monopolyworp()
        #else:
            #break


monopolyworp()
#gooi_opnieuw()

