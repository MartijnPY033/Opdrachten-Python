import csv

hoogstegetal = 0
hoogsteproduct = ""
minstevoorraad = 271
minstevooraadnummer = 0
totaalinmagazijn = 0
mydict= [{'Artikelnummer': 121, 'Artikelcode': 'ABC123','naam': 'Highlight pen', 'voorraad': 231,'prijs':0.56},
        {'Artikelnummer': 123, 'Artikelcode': 'PQR678','naam': 'Nietmachine', 'voorraad': 587,'prijs':9.99},
        {'Artikelnummer': 128, 'Artikelcode': 'ZYX163','naam': 'Bureaulamp', 'voorraad': 34,'prijs':19.95},
        {'Artikelnummer': 137, 'Artikelcode': 'MLK709','naam': 'Monitorstandaard', 'voorraad': 66,'prijs':32.50},
        {'Artikelnummer': 271, 'Artikelcode': 'TRS665','naam': 'Ipad Hoes', 'voorraad': 155,'prijs':19.01}]


keys = ['Artikelnummer', 'Artikelcode', 'naam','voorraad','prijs']
with open("artikelen.csv", 'w') as output_file:
    dict_writer = csv.DictWriter(output_file, keys,lineterminator='\n')
    dict_writer.writeheader()
    dict_writer.writerows(mydict)

with open('artikelen.csv') as csvfile:
    spamreader = csv.reader(csvfile, quotechar='|')
    next(spamreader)
    for row in spamreader:
       hoeveelvoorrad = str(row).split(',')[3][:-1]
       hoeveelvoorrad = hoeveelvoorrad[2:]
       hoeveelvoorrad = int(hoeveelvoorrad)
       totaalinmagazijn = totaalinmagazijn + hoeveelvoorrad
       print(hoeveelvoorrad)
       string = str(row).split(',')[4][:-2]
       newstring = string[2:]
       newfloat = float(newstring)
       if newfloat > hoogstegetal:
           hoogstegetal = newfloat
           hoogsteproduct=str(row).split(',')[2]
       voorraad = str(row).split(',')[3][:-1]
       newvoorraad = voorraad.replace("'","")
       newvoorraadfloat = float(newvoorraad)
       if newvoorraadfloat < float(minstevoorraad):
           minstevoorraad = newvoorraad
           minstevooraadnummer=str(row).split(',')[0]
           minstevooraadnummer = minstevooraadnummer[:-1]
           minstevooraadnummer = minstevooraadnummer[2:]


print("Het hoogste getal komt van een",str(hoogsteproduct), "die kost", str(hoogstegetal))
print("Er zijn slechts",minstevoorraad,"exemplaren in voorraad van het product met nummer",minstevooraadnummer)
print("In totaal hebben wij",totaalinmagazijn,"producten in ons magazijn liggen" )
