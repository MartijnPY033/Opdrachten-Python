
def prijs_hotel(AantalPersonen):
    HotelKosten = 4356
    Kosten = HotelKosten / int(AantelPersonen)
    return Kosten


try:
    AantelPersonen = int(input('Met hoeveel personen wil je gaan: '))
    if AantelPersonen > 0:
        print (prijs_hotel(AantelPersonen))
    elif AantelPersonen == 0:
        print('Delen door 0 kan niet')
    elif AantelPersonen < 0:
        print('Negatieve getallen zijn niet toegestaan')
    else:
        print('Ongeldige invoer probeer opnieuw')

except ValueError as f:
    print('Gebruik cijfers voor het invoeren van getallen ', f)
except:
    print('Onjuiste invoer')
