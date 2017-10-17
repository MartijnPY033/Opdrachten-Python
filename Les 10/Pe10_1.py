import xmltodict

def XML_Dict(filename):
    with open('10_1 xml code') as mijnXML:
        filecontentstring = mijnXML.read()
        xmldict = xmltodict.parse(filecontentstring)
        return xmldict

addressdict = XML_Dict('artikelen.xml')
artikelen = addressdict['artikelen']['artikel']

for artikel in artikelen:
    print(artikel)


