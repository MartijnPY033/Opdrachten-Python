

def code(invoerstring):
    for karakter in invoerstring:
        asciivertaling = (ord(karakter) + 3)
        vertaling = chr(asciivertaling)
        print(vertaling, end='')


print (code('HenkWillemsAmsterdam Centraal'))
