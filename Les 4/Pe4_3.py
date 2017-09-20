

def lang_genoeg(length):

    if length >= 120:
        return 'Je bent lang genoeg'


    else:
        return 'Sorry je bent te klein'

lengte = eval(input('Geef je lengte op in centimeter: '))
print(lang_genoeg(lengte))
