


def namen():
    klas = {}
    while True:
        naam = input('Volgende naam: ')
        if len(naam) > 0:
            if naam in klas:
                klas[naam] += 1
            else:
                klas[naam] = 1
        else:
            break
    for key, value in klas.items():
        if value == 1:
            print('Er is 1 student met de naam {}'.format(key))
        else:
            print('Er zijn {} studenten met de naam{}'.format(value, key))
namen()

