
def toon_aantal_kluizen_vrij():  # toont aantal vrije kluizen
    beschikbaar = 12 - len(aantal)  # 12 kluizen in totaal min het aantal dat al in gebruik is (leest uit file)
    if beschikbaar <= 0:
        vrijKluis = 'er zijn geen kluizen meer vrij'  # als beschikbaar 0 is, dan zijn er geen kluizen meer
    elif beschikbaar == 1:
        vrijKluis = 'er is nog 1 kluis beschikbaar' # 1 kluis over
    else:
        vrijKluis = ('Er zijn {} kluizen beschikbaar'.format(beschikbaar)) # kluizen die beschikbaar zijn > 0

    return vrijKluis  # returned het resultaat


def nieuwe_kluis():
    kluisnummers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]  # lijst met alle kluisnummers
    bezet = []  # nieuwe lijst met de bezette kluizen
    kluizen = open('kluizen.txt', 'r+')
    aantal = kluizen.readlines()
    for lijn in aantal:
        nummers = lijn.split('; ')  # split de regels in kluizen.txt en maakt een lijst met elke regel erin.
        cijfers = int(nummers[0])  # de cijfers worden uit de lijst gepakt.
        bezet.append(cijfers)  # lijst met bezette kluisjes word aangevuld

    for kluis in bezet:  # word gekeken welke kluisjes in bezet staan
        kluisnummers.remove(kluis)  # alle bezette kluisjes worden uit kluisnummers verwijderd.

    if len(kluisnummers) > 0:  # als kluisnnummers meer dan 0 getallen erin heeft staan, zijn er kluizen beschikbaar.
        print('Er zijn nog vrije kluizen over.')
        wachtwoord = input('Voer een wachtwoord in en ontvang een kluis: ')  # voer dan een wachtwoord in
        kluizen.write('{}; {}\n'.format(kluisnummers[0], wachtwoord))  # het eerste kluisje in de lijst word gekoppeld
        # met het wachtwoord en in de text file geschreven.
        kluizen.close()
        return ('Je krijgt kluisnummer: ' + str(kluisnummers[0]))
    else:
        kluizen.close()
        return ('een kluizen meer beschikbaar')


def kluis_openen():
    kluizen = open('kluizen.txt', 'r+')
    aantal = kluizen.readlines()
    kluisNum = eval(input('geef je kluisnummer: '))  # kluisNum invoeren
    kluisww = input('geef je wachtwoord: ')  # kluisww invoeren
    for lijn in aantal:  # for loop voor regels in kluizen.txt
        gesplit = lijn.split('; ')  # kluisnummer en code word gesplit
        cijfers = int(gesplit[0])  # kluisnr wordt intwaarde
        wachtwoord = gesplit[1].strip(
            '\n')  # verwijderd de enter aan het eind van een regel, zodat het password zonder \n ingelezen word.
        if cijfers == kluisNum and wachtwoord == kluisww:  # als de invoer gelijk is aan de kluisnummer en wachtwoord:
            gevonden = 'Dat is correct'  # geeft gevonden de waarde dat is correct
            break  # wanneer de waarde gevonden is, stopt de for loop met zoeken.
        else:
            gevonden = 'Niets gevonden'  # als er niks gevonden word, word de waarde van gevonden 'niets gevonden'
    kluizen.close()
    return (gevonden)  # returned gevonden

kluizen = open('kluizen.txt', 'r+')
aantal = kluizen.readlines()

def trigger_functie(nummer):  # hiermee roep ik de juiste functie aan bij de keuze
    if nummer == 1:
        print(toon_aantal_kluizen_vrij())
    if nummer == 2:
        print(nieuwe_kluis())
    if nummer == 3:
        print(kluis_openen())
    if nummer == 4:
        pass


while True:
    print('') # print lege lijn tussen keuzemenu en functie output
    print("""1.Ik wil weten hoeveel kluizen nog vrij zijn.
2.Ik wil een nieuwe kluis.
3.Ik wil even iets uit mijn kluis halen.
4.Ik geef mijn kluis terug.
5.Stop""")
    print('')
    nummer = int(input("Kies een nummer tussen de 1 en de 5" '\n'))
    trigger_functie(nummer)
    if nummer == 5:
        print('Het programma word afgesloten...')
        break
    else:
        continue

trigger_functie(nummer)

kluizen.close()  # text file word gesloten
