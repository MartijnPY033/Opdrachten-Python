invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
invoer.replace("", '')
gesorteerd = list(invoer)
print (gesorteerd)
gesorteerd.sort()
del gesorteerd[0:11]



print (type(gesorteerd))
print (eval(sum(gesorteerd)))
print (len(gesorteerd))
print(gesorteerd)

print ('grootste getal:', max(gesorteerd), 'kleinste getal:',  min(gesorteerd))
print ('aantal getallen:', len(gesorteerd), 'Som van de getallen:', sum(gesorteerd))


