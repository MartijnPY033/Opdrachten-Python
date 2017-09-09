import math

x = input('Wat verdien je per uur?: ')

y = input('Hoeveel uur heb je gewerkt?: ')

result = math.ceil((float(y) * float(x)*100)/100)

print ("Je verdient " + str(result) +" euro")
