print ('Dames en Heren, Welkom bij de kostenberekener van de NS')
print('Om u zo goed mogelijk van dienst te zijn hebben wij deze rijskosten berekener gemaakt.')
input('Druk op enter om door te gaan: ')
input()
afstand = eval(input('Dien hier het aantal KM in dat je gaat reizen: '))

def standaardprijs(afstandKM):
    'Functie berekent normale prijs van een rit.'
    if afstandKM < 0:
        afstandKM = 0

    if afstandKM <= 50:
        prijs = afstandKM * 0.80
        return prijs
    if afstandKM > 50:
        prijs = afstandKM * 0.60 + 15
        return prijs


weekend = input(str('Wilt u in het weekend reizen, ja of nee: '))
leeftijdweekend = eval(input('Dien hier je leeftijd in: '))


def ritprijs(afstandKM, weekend):
    'functie berekent eventuele kortingen voor bepaalde groepen reizigers.'
    kosten = standaardprijs(afstandKM)
    if weekend == 'ja':
        if leeftijdweekend > 11 and leeftijdweekend < 65:
            return kosten * 0.60
        else:
            return kosten * 0.65
    if weekend == 'nee':
        if leeftijdweekend > 11 and leeftijdweekend < 65:
            return kosten
        else:
            return kosten * 0.70

print ('Je betaald ', "%.2f" % ritprijs(afstand, weekend), ' euro.')





