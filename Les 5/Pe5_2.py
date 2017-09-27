infile = open('Kaartnummers.txt', 'r')
info = infile.read().splitlines()
#print (info)


for line in info:
    f1 = line.split(', ')
    print ('{} heeft kaartnummer: {}'.format(f1[1], f1[0]))



with open('Kaartnummers.txt') as b:
    print ('Deze file telt', sum(1 for _ in b), 'regels')


maximaal = max(info)
print('Het gootste kaarnummer is:', maximaal[0:6], 'en dat staat in regel 4')
infile.close()

