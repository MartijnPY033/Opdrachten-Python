'lijst met stations'
stationslijst = ['Schagen', 'Heerhugowaard','Alkmaar','Castricum','Zaandam','Amsterdam Sloterdijk','Amsterdam Centraal','Amsterdam Amstel',
            'Utrecht Centraal','’s-Hertogenbosch','Eindhoven', 'Weert','Roermond', 'Sittard', 'Maastricht']

def inlezen_beginstation(beginstation):
    'Functie laat invoer zien aan de gebruiker en vraagt om eindstation bij verkeerde invoer moet de gebruiker opnieuw'
    'het station invoeren'
    if beginstation in stationslijst:
        print('U heeft gekozen voor beginstation', beginstation)
        inlezen_eindstation(input('Geef een eindstation op'),beginstation)
        return beginstation
    else:
        inlezen_beginstation(input('Geef nogmaals het beginstation op: '))

def inlezen_eindstation(eindstation, beginstation):
    'functie laat de invoer van de gebruiker zien en stuurt de invoer (eindstation door naar de volgende functie'
    'wanneer de index groter is dan het begistation'
    print ('U heeft gekozen voor eindstation',eindstation,'\n')
    stations = stationslijst
    if eindstation in stationslijst:
        if stationslijst.index(eindstation)> stationslijst.index(beginstation):
            omroepen_reis(stations, beginstation, eindstation)
            return eindstation
        else:
            print ('De trein gaat niet achteruit')
    else:
        inlezen_eindstation(input(''),beginstation)

def omroepen_reis(stations, beginstation, eindstation):
    'Functie toont de stations die de reiziger tegenkomt op zijn reis, hiervoor gebruikt deze functie de waarde'
    'van de andere functies'
    TotaalStations = stationslijst.index(eindstation)- stationslijst.index(beginstation)

    print('Het beginstation',beginstation,'is het', str(stationslijst.index(beginstation)+1),'e station op het traject,'
    '\n'
    'Het eindstation',eindstation,'is het', str(stationslijst.index(eindstation)+1),'e station op het trajact'
    '\n'
    'De afstand is',str(TotaalStations),'stations'
    '\n'
    'De prijs van het kaartje bedraagt', str(TotaalStations * 5), 'euro.'
    '\n'
    '\n','Je stapt in op station:',beginstation)
    for i in range(stationslijst.index(beginstation)+1,stationslijst.index(eindstation)):
        print("-"+ stationslijst[i])
    print('Je stapt uit op station:', eindstation)



'Reiziger kan zijn beginstation invoeren'
Invoer = input('Geef het beginstation op: ')

'Functie word aangeroepen met de inveor van de reiziger'
inlezen_beginstation(Invoer)

