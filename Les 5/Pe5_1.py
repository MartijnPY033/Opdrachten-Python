


def convert(Temp):
    Fahrenheit = (Temp *1.8) + 32
    return Fahrenheit



def table():
    for celsius in range (-30, 50, 10):
        Fahr = convert(celsius)
        print ('{:8}   {:6}'.format("%.1f" % Fahr,  celsius))
print ('F             C')
table()
