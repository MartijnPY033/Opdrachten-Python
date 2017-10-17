print('8_3A: A', 'Mijn antwoord fout omdat de functie nog niet was aangeroepen')
a = 3
def f(y):
    global a
    a = 9
    return 2*y + a
print(a, 'Antwoord B')
print('\n')

print('8_3B: D', 'Mijn antwoord goed')
x = 1
y = 4
def fun():
    x =2
    global y
    y =3
    print (y, end=' ')
fun()
print (y,end=' ')

print('8_3C: A', 'Mijn antwoord goed')
x = 2
y = 5
def fun():
    y = 3
    global x
    x = 1
    print(x*y, end = ' ')
    return x*y
x = fun()
print(x*y, end = ' ')
print('\n')
print('8_3D: C', 'Mijn antwoord goed')
a = 3
def fun1():
    global a
    print   ("a:", a, end = '  ')
    b = 7
    a =0
    return b

def fun2(y):
    a = y + fun1()
    b = 7
    a +=1
    return
    a
a = 9
fun2(5)
print ("a:", a)
print('8_3E: A', 'Mijn antwoord fout', 'De waarde van local Y word wel in X gestopt')
x = 1
y = 4
def doe1():
    global x
    y = 7
    x = 0
    return y

def doe2():
    x = doe1()
    x +=1
    return x
x = doe1()
print(x)
print('8_3F: D', 'Mijn antwoord goed')
a = 5
def fun1():
    global a
    b = 2
    a =4
    return a+b
def fun2(y):
    global a
    a = y + fun1()
    a +=1
    return a
print ("a:", a, end = ' ')
a = fun2(3)
print ("a:", a)

print('8_3G: A', 'Mijn antwoord goed')

x = 1
y = 3
def doe1():
    global x
    y = 4
    x = 0
    return x+y
def doe2():
    x = doe1()
    x += 2
    return x
doe2()
print (x)

print('8_3H: D', 'Mijn antwoord goed omdat er een globale x word aangemaakt in de functie')
def doe1():
    y = 7
    x = 0
    return y
def doe2():
    global x
    x = doe1()
    x += 1
doe2()
print (x)
