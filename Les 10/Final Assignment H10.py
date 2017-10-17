import xmltodict

def XmlToDict(file):
    'zet xml file om naar een dictionary'
    with open(file) as XMLStations:
        XMLContent = XMLStations.read()
        XMLDict = xmltodict.parse(XMLContent)
        return XMLDict
'haalt de tags uit de xml file'
stationsdict = XmlToDict('XML_stations')
stations = stationsdict['Stations']['Station']



print('Dit zijn de codes en types van de 4 stations:')
for station in stations:
    'output code en type'
    print(station['Code'], end=' ')
    print('-', station['Type'], sep=' ')
print()
print('Dit zijn alle stations met 1 of meer synoniemen:')
for station in stations:
    'output synoniem en code'
    if station['Synoniemen'] is not None:
        print(station['Code'], end=' ')
        stationsynoniemen = station['Synoniemen']
        print('{} '.format(stationsynoniemen['Synoniem']), end='')
print()
print()
print('Dit is de lange naam van elk station:')
for station in stations:
    'output code en lange naam'
    print(station['Code'], end='')
    stationlangenamen = station['Namen']
    print('  -{}'.format(stationlangenamen['Lang']))








