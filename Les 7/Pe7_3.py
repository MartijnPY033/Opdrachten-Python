studenten = {'Klaas': 4, 'Henk': 8, 'Willie': 9, 'Andrew': 9,
             'Joost': 2, 'Wilfried': 7, 'Romie': 9, 'Mesut': 9}

for cijfers in studenten.items():
    if cijfers[1] == 9:
        print(str(cijfers[0]), cijfers[1])
