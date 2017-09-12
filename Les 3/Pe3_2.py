leeftijd = eval(input('Geef je leeftijd: '))
paspoort = str(input('Nederlands Paspoort ja of nee: '))



if  paspoort == 'ja' and leeftijd >= 18:
    print('Gefeliciteerd! je mag stemmen')

else:
    wachtTijd = 18 - leeftijd
    print ('Je mag niet stemmen je moet nog ' + str(wachtTijd) + ' jaar wachten')
