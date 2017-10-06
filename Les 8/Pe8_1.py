Groen = {'Boxtel', 'Best', 'Beukenlaan', 'Eindhoven', 'Geldrop', 'Heeze', 'Weert'}
Bruin = {'Boxtel', 'Best', 'Beukenlaan', 'Eindhoven', 'Helmond t Hout', 'Helmond Brouwhuis', 'Deurne'}

print('Overeenkomst trajecten: ', Groen & Bruin)
print ('Traject Groen: ', Groen - Bruin, 'Traject Bruin ', Bruin - Groen)
print('Alle stations: ', Groen | Bruin)
