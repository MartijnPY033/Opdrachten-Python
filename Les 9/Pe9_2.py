import datetime
import csv
vandaag = datetime.datetime.today()
s = vandaag.strftime("%a %d %b %Y")
bestand = open('inloggers.csv', 'a', newline='')
#gebruik hier een herhalingslus:

while True:
    naam = input("Wat is je achternaam?: ")
    if naam == 'einde':
        bestand.close()
        break
    else:
        voorl = input("Wat zijn je voorletters?: ")
        gbdatum = input("Wat is je geboortedatum?: ")
        email = input("Wat is je e-mail adres?: ")
        bestand.writelines([s, ';', voorl, ';', naam, ';', gbdatum, ';', email])
        continue



#wanneer de volgende persoon inlogt is onbekend, dus schrijf meteen naar file
