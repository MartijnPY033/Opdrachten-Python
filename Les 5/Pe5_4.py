import datetime
vandaag = datetime.datetime.today()
s = vandaag.strftime("%a %d %b %Y")
e = vandaag.strftime("%H:%M:%S")
print(s, e)

file = open('hardlopers.txt', 'a')

for i in range(0, 1):
    name = input('Geef een naam op: ')
    file.write(s + ', ' + e + ', ' + name + "\n")


file.close()
